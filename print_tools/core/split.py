from pypdf import PageObject, PdfWriter


def split_pdf_pages_by_size(
    pages: list[PageObject],
    target_size_pt: tuple[float, float],
    *,
    epsilon: float = 2.0,
):
    writer = PdfWriter()

    t_w, t_h = target_size_pt

    for page in pages:
        w, h = float(page.mediabox.width), float(page.mediabox.height)

        cols = int((w + epsilon) // t_w)
        rows = int((h + epsilon) // t_h)

        for r in range(rows):
            for c in range(cols):
                llx, lly = c * t_w, r * t_h
                urx, ury = min(llx + t_w, w), min(lly + t_h, h)

                # skip slivers
                if (urx - llx) < epsilon or (ury - lly) < epsilon:
                    continue

                page.mediabox.lower_left = (llx, lly)
                page.mediabox.upper_right = (urx, ury)
                writer.add_page(page)

    return writer
