from pypdf import PdfWriter
from pypdf._page import PageObject

from ..utils.embed import embed_page
from ..utils.layouting.models import BaseLayouter, Box, Container, ContainerSpec
from ..utils.paper import PaperRef, get_paper_size
from ..utils.layouting.algorithms import GridLayouter


def impose_pages_general(
    pages: list[PageObject], layouter: BaseLayouter, paper: PaperRef
):
    w_sheet, h_sheet = get_paper_size(paper)

    result = layouter.perform_layout(
        available_containers=ContainerSpec(
            container=Container(width=w_sheet, height=h_sheet),
            max_amount=100,
        ),
        boxes=[
            Box(width=page.mediabox.width, height=page.mediabox.height)
            for page in pages
        ],
    )

    writer = PdfWriter()

    sheets = [
        writer.add_blank_page(width=container.width, height=container.height)
        for container in result.used_containers
    ]

    for applied_box in result.applied_boxes:
        page = pages[applied_box.box_index]
        sheet = sheets[applied_box.container_index]

        # Embed the page onto the sheet with the specified transformation
        embed_page(
            sheet,
            page,
            position=applied_box.position,
            rotation=applied_box.rotation,
            mirror_horizontal=applied_box.mirror_horizontal,
            mirror_vertical=applied_box.mirror_vertical,
        )

    return writer


def impose_pages_grid(pages: list[PageObject], paper: PaperRef):
    """
    Impose pages in a grid layout on a single PDF sheet.
    """
    layouter = GridLayouter(padding=10, gap=10)
    return impose_pages_general(pages, layouter, paper=paper)
