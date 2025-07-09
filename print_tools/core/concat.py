from pathlib import Path
from PyPDF2 import PdfMerger

from ..utils import gather_files


def concat_pdfs(input_files: list[Path], output_file: Path):
    """Concatenate multiple PDF files into a single PDF."""
    input_files = gather_files(input_files)

    if not input_files:
        raise ValueError("input_files must contain at least one path")

    print(f"Concatenating {len(input_files)} PDF files into one...")

    for p in input_files:
        if not p.exists():
            raise FileNotFoundError(p)

    merger = PdfMerger()  # or PdfFileMerger()

    for pdf in input_files:
        merger.append(str(pdf))  # copies all pages in order

    with output_file.open("wb") as f:
        merger.write(f)

    merger.close()

    return output_file
