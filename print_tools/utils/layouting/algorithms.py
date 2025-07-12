from .models import (
    AppliedBox,
    BaseLayouter,
    Box,
    Container,
    ContainerSpec,
    LayoutResult,
)


class GridLayouter(BaseLayouter):
    """
    A layouter that arranges boxes in a grid layout within the available containers.
    It supports padding and gap between boxes.
    The padding is applied around the entire grid, while the gap is applied between boxes.
    """

    def __init__(self, padding: float = 0.0, gap: float = 0.0):
        self.padding = padding
        self.gap = gap

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
            if x + box.width > container.width - self.padding:
                x = self.padding
                y += row_height + self.gap
                row_height = 0

            # Move to next container if the box does not fit vertically
            if y + box.height > container.height - self.padding:
                used_containers.append(container)
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
