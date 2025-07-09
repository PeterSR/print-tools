from pathlib import Path
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics, ttfonts


def hex_to_colour(hexcode: str):
    """#RRGGBB → reportlab colour object"""
    hexcode = hexcode.lstrip("#")
    r, g, b = (int(hexcode[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return colors.Color(r, g, b)


def register_font(name: str):
    """Register external TTF if given a filename; otherwise assume built-in."""
    if Path(name).suffix.lower() in {".ttf", ".otf"}:
        short = Path(name).stem
        pdfmetrics.registerFont(ttfonts.TTFont(short, name))
        return short
    return name


def gather_files(input_files: list[Path], ext: str = ".pdf") -> list[Path]:
    """Gather and validate input files, ensuring they are all PDF files."""
    pdf_files = []

    for file in input_files:
        if file.is_dir():
            # Add all files with the specified extension from the directory
            pdf_files.extend(list(file.glob(f"*{ext}")))
        else:
            if file.suffix.lower() != ext:
                raise ValueError(f"File {file} is not a {ext} file.")

            pdf_files.append(file)

    return pdf_files
