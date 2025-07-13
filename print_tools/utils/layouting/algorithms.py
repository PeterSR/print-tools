import math

from .models import (
    AppliedBox,
    BaseLayouter,
    Box,
    Container,
    ContainerSpec,
    LayoutResult,
)
from .helpers import imposition_order


class GridLayouter(BaseLayouter):
    """
    A layouter that arranges boxes in a grid layout within the available containers.
    It supports padding and gap between boxes.
    The padding is applied around the entire grid, while the gap is applied between boxes.
    Leeway can be used when boxes that pretty much fit, but not exactly. Leeway is in points.
    The layout is performed in a left-to-right, bottom-to-top manner.
    """

    def __init__(self, padding: float = 0.0, gap: float = 0.0, leeway: float = 1.0):
        self.padding = padding
        self.gap = gap
        self.leeway = leeway

    def perform_layout(
        self, available_containers: list[Container] | ContainerSpec, boxes: list[Box]
    ) -> LayoutResult:
        containers = (
            available_containers.generate_containers()
            if isinstance(available_containers, ContainerSpec)
            else list(available_containers)
        )

        applied_boxes: list[AppliedBox] = []
        used_containers: list[Container] = []

        ci = 0  # current container index
        x = y = self.padding  # cursor within the current container
        row_height = 0  # tallest box in the current row

        for box_index, box in enumerate(boxes):
            container = containers[ci]

            # Start a new row if the box does not fit horizontally
            if x + box.width > container.width - self.padding + self.leeway:
                x = self.padding
                y += row_height + self.gap
                row_height = 0

            # Move to next container if the box does not fit vertically
            print(y + box.height, container.height)
            if y + box.height > container.height - self.padding + self.leeway:
                ci += 1
                if ci >= len(containers):
                    raise ValueError("Not enough containers to fit all boxes.")
                container = containers[ci]
                x = y = self.padding
                row_height = 0

            # Place the box
            applied_boxes.append(
                AppliedBox(
                    box_index=box_index,
                    container_index=ci,
                    position=(x, y),
                )
            )

            # Advance cursor
            x += box.width + self.gap
            row_height = max(row_height, box.height)

        # Record the final container in use
        used_containers.extend(containers[: ci + 1])

        return LayoutResult(
            used_containers=used_containers,
            applied_boxes=applied_boxes,
            custom_fields={
                "padding": self.padding,
                "gap": self.gap,
            },
        )



class PackLayouter(BaseLayouter):
    """
    A layouter that tries to pack boxes into the available containers as tightly as possible.
    It supports padding and gap between boxes.
    The padding is applied around the entire grid, while the gap is applied between boxes.
    Leeway can be used when boxes that pretty much fit, but not exactly. Leeway is in points.
    """

    def __init__(self, padding: float = 0.0, gap: float = 0.0, leeway: float = 1.0):
        self.padding = padding
        self.gap = gap
        self.leeway = leeway


    # --------------------------------------------------------------------- #
    # internal helpers                                                      #
    # --------------------------------------------------------------------- #
    def _fits(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        container: Container,
        placed: list[tuple[float, float, float, float]],
    ) -> bool:
        """Return True if a w x h rectangle can be placed at (x,y)."""
        # inside inner rectangle defined by padding
        if (
            x + w > container.width - self.padding + self.leeway
            or y + h > container.height - self.padding + self.leeway
        ):
            return False

        # keep `gap` distance to every already‑placed rectangle
        for px, py, pw, ph in placed:
            if not (
                x >= px + pw + self.gap
                or px >= x + w + self.gap
                or y >= py + ph + self.gap
                or py >= y + h + self.gap
            ):
                return False
        return True

    # --------------------------------------------------------------------- #
    # main entry                                                             #
    # --------------------------------------------------------------------- #
    def perform_layout(
        self,
        available_containers: list[Container] | ContainerSpec,
        boxes: list[Box],
    ) -> LayoutResult:
        # normalise container input ------------------------------------------------
        containers = (
            available_containers.generate_containers()
            if isinstance(available_containers, ContainerSpec)
            else list(available_containers)
        )
        if not containers:
            raise ValueError("No containers available.")

        # prepare state for every container ---------------------------------------
        states = [
            {
                "placed": [],  # list[(x,y,w,h)]
                "candidates": [(self.padding, self.padding)],  # bottom‑left seed
            }
            for _ in containers
        ]

        applied_boxes: list[AppliedBox] = []
        ci = 0  # current container index

        # pack largest boxes first -------------------------------------------------
        for idx, box in sorted(
            enumerate(boxes),
            key=lambda t: max(t[1].width, t[1].height) * min(t[1].width, t[1].height),
            reverse=True,
        ):
            placed = False

            while not placed:
                if ci >= len(containers):
                    raise ValueError("Not enough containers to fit all boxes.")

                state = states[ci]
                cont = containers[ci]
                cand_list = state["candidates"]

                # iterate through candidate points (sorted by y, then x)
                while cand_list and not placed:
                    cx, cy = cand_list.pop(0)

                    for rot, (w, h) in (
                        (0, (box.width, box.height)),
                        (90, (box.height, box.width)),
                    ):
                        if self._fits(cx, cy, w, h, cont, state["placed"]):
                            # record placement ------------------------------------
                            final_cx = cx + w if rot == 90 else cx
                            applied_boxes.append(
                                AppliedBox(
                                    box_index=idx,
                                    container_index=ci,
                                    position=(final_cx, cy),
                                    rotation=rot,
                                )
                            )
                            state["placed"].append((cx, cy, w, h))

                            # new candidate points: to the right, above -----------
                            cand_list.extend(
                                [
                                    (cx + w + self.gap, cy),
                                    (cx, cy + h + self.gap),
                                ]
                            )
                            # keep candidates ordered (bottom‑left priority) ------
                            cand_list.sort(key=lambda p: (p[1], p[0]))
                            placed = True
                            break  # break rotation loop

                if not placed:
                    # move on to next container ----------------------------------
                    ci += 1

        used_containers = containers[: ci + 1]

        return LayoutResult(
            used_containers=used_containers,
            applied_boxes=applied_boxes,
            custom_fields={
                "padding": self.padding,
                "gap": self.gap,
            },
        )


class BookletLayouter(BaseLayouter):
    """
    Imposes A5-sized pages on A4 sheets in printer-spread order.
    Assumes every container is an A4 side and each box is half-width (A5).
    """

    def __init__(self, padding: float = 0.0, gap: float = 0.0):
        self.grid = GridLayouter(padding=padding, gap=gap)

    def perform_layout(
        self,
        available_containers: list[Container] | ContainerSpec,
        boxes: list[Box],
    ) -> LayoutResult:
        pages = list(boxes)
        num_blanks = 0
        if len(pages) % 4:  # pad blanks if needed
            num_blanks = 4 - (len(pages) % 4)
            pages.extend(
                [
                    Box(
                        width=pages[0].width,
                        height=pages[0].height,
                        custom_fields={"blank": True},
                    )
                ]
                * num_blanks
            )

        containers = (
            available_containers.generate_containers()
            if isinstance(available_containers, ContainerSpec)
            else available_containers
        )

        # one A4 *side* per container, make sure we have enough
        needed_containers = math.ceil(len(pages) / 2)
        if needed_containers > len(containers):
            raise ValueError("Not enough sheet sides supplied")

        # reorder pages for imposition
        imposed_order = imposition_order(len(pages))
        ordered_boxes = [pages[i - 1] for i in imposed_order]  # to 0‑based

        # run the existing two‑up grid
        result = self.grid.perform_layout(containers, ordered_boxes)

        # Remove the boxes created in this function that represent blanks
        blank_indices = set(
            i
            for i, box in enumerate(ordered_boxes)
            if box.custom_fields.get("blank", False)
        )
        result.applied_boxes = [
            ab for ab in result.applied_boxes if ab.box_index not in blank_indices
        ]

        # Re-index the result.applied_boxes.box_index to the original boxes
        for ab in result.applied_boxes:
            if ab.box_index < len(pages):
                ab.box_index = imposed_order[ab.box_index] - 1

        # Add custom fields to the result
        result.custom_fields["num_blanks"] = num_blanks
        result.custom_fields["imposed_order"] = imposed_order
        result.custom_fields["padding"] = self.grid.padding
        result.custom_fields["gap"] = self.grid.gap

        return result


if __name__ == "__main__":
    # Example usage
    from .models import Container, Box, ContainerSpec

    container = Container(width=200, height=200)
    boxes = [Box(width=50, height=50) for _ in range(10)]

    layouter = GridLayouter(padding=10, gap=5)
    result = layouter.perform_layout(
        ContainerSpec(container=container, max_amount=len(boxes)), boxes
    )

    print(result.model_dump_json(indent=2))
