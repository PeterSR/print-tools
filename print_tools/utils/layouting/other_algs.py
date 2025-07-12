"""
TODO: Make these usuable
"""

from .algorithms import GridLayouter
from .models import BaseLayouter, Box, Container, ContainerSpec, LayoutResult
from .helpers import quarter_fold_order, saddle_order


class SignatureLayouter(BaseLayouter):
    """
    Generic saddle-stitch layouter.

    Args:
        signature_pages: size of one folded signature (must be /4). 0 = auto-pad.
        mirror_back: flip back side horizontally (short-edge duplex helper).
        rotate_back_180: rotate every page on the back side 180°.
        padding, gap: forwarded to GridLayouter.
    """
    def __init__(
        self,
        signature_pages: int = 0,
        mirror_back: bool = False,
        rotate_back_180: bool = False,
        padding: float = 0.0,
        gap: float = 0.0,
    ):
        if signature_pages and signature_pages % 4:
            raise ValueError("signature_pages must be a multiple of 4.")
        self.signature_pages = signature_pages
        self.mirror_back = mirror_back
        self.rotate_back = rotate_back_180
        self.grid = GridLayouter(padding=padding, gap=gap)

    # ------------------------------------------------------------
    def perform_layout(
        self,
        available_containers: list[Container] | ContainerSpec,
        boxes: list[Box],
    ) -> LayoutResult:
        pages = list(boxes)
        target = self.signature_pages or len(pages)
        # pad out blanks
        if target % 4:
            target += 4 - (target % 4)
        while len(pages) < target:
            pages.append(Box(width=pages[0].width, height=pages[0].height))

        imposed = saddle_order(len(pages), self.mirror_back)
        ordered_boxes = [pages[i - 1] for i in imposed]

        result = self.grid.perform_layout(available_containers, ordered_boxes)

        if self.rotate_back:
            # every second pair belongs to the back side
            for i, app in enumerate(result.applied_boxes):
                if (i // 2) % 2 == 1:        # rows of front/back pairs
                    app.rotation = (app.rotation + 180) % 360
        return result
    # ------------------------------------------------------------


class QuarterFoldLayouter(BaseLayouter):
    """
    Very small 4-up quarter-fold layouter (16-page signatures typical).
    Bottom quadrants are rotated 180° so text is upright after the folds.
    """
    def __init__(self, padding: float = 0.0, gap: float = 0.0):
        self.grid = GridLayouter(padding=padding, gap=gap)

    def perform_layout(
        self,
        available_containers: list[Container] | ContainerSpec,
        boxes: list[Box],
    ) -> LayoutResult:
        pages = list(boxes)
        if len(pages) % 8:
            blanks = 8 - (len(pages) % 8)
            pages.extend([Box(width=pages[0].width, height=pages[0].height)] * blanks)

        imposed = quarter_fold_order(len(pages))
        ordered_boxes = [pages[i - 1] for i in imposed]

        result = self.grid.perform_layout(available_containers, ordered_boxes)

        # rotate bottom row on every side
        cols = 2
        for idx, app in enumerate(result.applied_boxes):
            # idx % 4: 0 TL,1 TR,2 BL,3 BR  → rotate BL & BR
            if idx % 4 in (2, 3):
                app.rotation = (app.rotation + 180) % 360
        return result
