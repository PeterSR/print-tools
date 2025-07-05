#!/usr/bin/env python3
"""
Templating utilities for overlaying text blocks on PDF templates.
"""

import io
from pathlib import Path
from typing import Iterator

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PyPDF2 import PdfReader, PdfWriter

from print_tools.utils import hex_to_colour, register_font


def parse_blocks(path: Path) -> Iterator[list[str]]:
    """Yield list[str] blocks separated by --- lines (ignoring blank lines)."""
    with path.open(encoding="utf-8") as fh:
        buf = []
        for line in fh:
            line = line.rstrip("\n")
            if line.strip() == "---":
                if buf:
                    yield buf
                    buf = []
            elif line.strip():
                buf.append(line)
        if buf:
            yield buf


def create_labeled_pdfs(
    template_path: Path,
    blocks_path: Path,
    output_dir: Path,
    font_name: str = "Helvetica",
    font_size: int = 18,
    line_spacing: int = 4,
    text_colour: str = "#000000",
) -> None:
    """
    Create labeled PDFs by overlaying text blocks on a template.

    Args:
        template_path: Path to the PDF template file
        blocks_path: Path to the text file containing blocks separated by ---
        output_dir: Directory to save the generated PDFs
        font_name: Font name or path to TTF/OTF file
        font_size: Size of the text in points
        line_spacing: Extra space between lines in points
        text_colour: Color name or hex code (#RRGGBB)
    """
    fontname = register_font(font_name)
    colour = getattr(colors, text_colour, None)
    colour = colour or hex_to_colour(text_colour)

    output_dir.mkdir(parents=True, exist_ok=True)

    tpl_reader = PdfReader(str(template_path))
    tpl_page = tpl_reader.pages[0]
    w = float(tpl_page.mediabox.width)
    h = float(tpl_page.mediabox.height)

    for idx, lines in enumerate(parse_blocks(blocks_path), 1):
        base_page = PdfReader(str(template_path)).pages[0]  # fresh copy of the template

        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(w, h))

        c.setFont(fontname, font_size)
        c.setFillColor(colour)

        line_height = font_size
        total_height = line_height * len(lines) + line_spacing * (len(lines) - 1)
        first_y = (h + total_height) / 2 - line_height  # top line y

        for i, txt in enumerate(lines):
            y = first_y - i * (line_height + line_spacing)
            c.drawCentredString(w / 2, y, txt)  # centre‑aligned horizontally

        c.save()

        # merge overlay with the template
        overlay_reader = PdfReader(buf)
        overlay_page = overlay_reader.pages[0]
        base_page.merge_page(overlay_page)  # draw overlay onto the fresh copy

        out_writer = PdfWriter()
        out_writer.add_page(base_page)
        out_path = output_dir / f"block_{idx:03d}.pdf"
        with out_path.open("wb") as fh:
            out_writer.write(fh)

        print(f"Wrote {out_path}")
