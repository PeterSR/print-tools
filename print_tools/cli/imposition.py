from pathlib import Path
import rich_click as click

from ..utils import gather_pdf_pages
from ..utils.layouting.algorithms import BookletLayouter, GridLayouter
from ..core.imposition import impose_pages_general


@click.group(name="imposition")
def cli():
    """Imposition tools for generating and manipulating PDF documents."""
    pass


def _impose_impl(input_files: list[Path], output_file: Path, layouter, paper: str):
    pages = gather_pdf_pages(input_files)

    if not pages:
        raise ValueError("No PDF pages found in the provided input files.")

    print(f"Imposing {len(pages)} PDF pages into a layout...")

    writer = impose_pages_general(pages, layouter, paper=paper)

    with output_file.open("wb") as f:
        writer.write(f)

    print(f"Imposed PDF saved to {output_file}")


@cli.command(name="grid")
@click.argument("input_files", nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option(
    "-o",
    "--output-file",
    type=click.Path(path_type=Path),
    default=Path("output.pdf"),
    help="Output file path for the imposed PDF",
)
@click.option(
    "-p",
    "--paper",
    type=click.Choice(
        ["A3", "A3-landscape", "A4", "A4-landscape", "A5", "A5-landscape"],
        case_sensitive=False,
    ),
    default="A4",
    help="Paper size for the imposed document",
)
@click.option(
    "--padding",
    type=int,
    default=0,
    help="Padding around each PDF page in the grid layout",
)
@click.option(
    "--gap",
    type=int,
    default=0,
    help="Gap between PDF pages in the grid layout",
)
def impose_grid(
    input_files: list[Path], output_file: Path, paper: str, padding: int, gap: int
):
    """Impose multiple PDF files into a grid layout on a single PDF."""

    layouter = GridLayouter(padding=padding, gap=gap)

    _impose_impl(input_files, output_file, layouter, paper)


@cli.command(name="booklet")
@click.argument("input_files", nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option(
    "-o",
    "--output-file",
    type=click.Path(path_type=Path),
    default=Path("output.pdf"),
    help="Output file path for the concatenated PDF",
)
@click.option(
    "-p",
    "--paper",
    type=click.Choice(
        ["A3", "A3-landscape", "A4", "A4-landscape", "A5", "A5-landscape"],
        case_sensitive=False,
    ),
    default="A4",
    help="Paper size for the imposed document",
)
@click.option(
    "--padding",
    type=int,
    default=0,
    help="Padding around each PDF page in the grid layout",
)
@click.option(
    "--gap",
    type=int,
    default=0,
    help="Gap between PDF pages in the grid layout",
)
def impose_booklet(
    input_files: list[Path], output_file: Path, paper: str, padding: int, gap: int
):
    """Impose multiple PDF files into a booklet layout on a single PDF."""

    layouter = BookletLayouter(padding=padding, gap=gap)

    _impose_impl(input_files, output_file, layouter, paper)
