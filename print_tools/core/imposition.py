from PyPDF2 import PdfWriter, Transformation, PageObject
from reportlab.lib.pagesizes import A3, A4, A5, LETTER   # only for ready‑made sizes

PAGE_SIZES = {
    "A3": A3, "A4": A4, "A5": A5, "LETTER": LETTER,
}


def impose_pages_grid(pages: list[PageObject], paper="A3"):
    w_sheet, h_sheet = PAGE_SIZES.get(paper, paper)
    w_page, h_page   = float(pages[0].mediabox.width), float(pages[0].mediabox.height)

    print(f"Source page size: {w_page}x{h_page}, Sheet size: {w_sheet}x{h_sheet}")

    cols, rows = int(w_sheet // w_page), int(h_sheet // h_page)
    if not (cols and rows):
        raise ValueError("Source page is bigger than the chosen sheet")

    writer = PdfWriter()
    sheet   = writer.add_blank_page(w_sheet, h_sheet)
    cap     = cols * rows
    slot    = 0

    for src in pages:
        if slot == cap:                # start new sheet
            sheet, slot = writer.add_blank_page(w_sheet, h_sheet), 0

        c, r  = slot % cols, slot // cols
        tx, ty = c * w_page, r * h_page
        print(f"Placing page {slot + 1} at {tx}, {ty}")
        src.add_transformation(Transformation().translate(-tx, -ty))
        sheet.merge_page(src)
        slot += 1

    return writer