from pypdf import PdfWriter
from pypdf._page import PageObject

from ..utils.embed import embed_page
from ..utils.layouting.models import BaseLayouter, Box, Container, ContainerSpec
from ..utils.paper import PaperRef, get_paper_size


def impose_pages_general(
    pages: list[PageObject], layouter: BaseLayouter, paper: PaperRef
):
    w_sheet, h_sheet = get_paper_size(paper)

    print(w_sheet)

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
        page = (
            pages[applied_box.box_index] if applied_box.box_index < len(pages) else None
        )

        if page is None:
            continue

        print(
            f"Embedding page {applied_box.box_index} onto sheet {applied_box.container_index} at position {applied_box.position}"
        )

        sheet = sheets[applied_box.container_index]

        # Embed the page onto the sheet with the specified transformation
        embed_page(
            sheet,
            page,
            position=applied_box.position,
            scale=applied_box.scale,
            rotation=applied_box.rotation,
            mirror_horizontal=applied_box.mirror_horizontal,
            mirror_vertical=applied_box.mirror_vertical,
        )

    return writer
