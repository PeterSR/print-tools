import rich_click as click
from pathlib import Path


from ..utils.paper import get_paper_size
from ..utils.utils import gather_pdf_pages
from ..core.split import split_pdf_pages_by_size


@click.command(name="split")
@click.argument("input_files", nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option(
    "-o",
    "--output-file",
    type=click.Path(path_type=Path),
    default=Path("output.pdf"),
    help="Output file path for the split PDF",
)
@click.option(
    "-p",
    "--target-paper",
    type=click.Choice(
        ["A3", "A3-landscape", "A4", "A4-landscape", "A5", "A5-landscape"],
        case_sensitive=False,
    ),
    default="A4",
    help="Target paper size for splitting the PDF",
)
def cli(input_files: list[Path], output_file: Path, target_paper: str):
    """Split a PDF into multiple files."""

    pages = gather_pdf_pages(input_files)

    target_size_pt = get_paper_size(target_paper)

    writer = split_pdf_pages_by_size(pages, target_size_pt=target_size_pt)

    writer.write(output_file)
