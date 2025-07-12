from pathlib import Path
import rich_click as click

from ..utils import gather_pdf_pages

from ..core.imposition import impose_pages_grid


@click.group(name="imposition")
def cli():
    """Imposition tools for generating and manipulating PDF documents."""
    pass


@cli.command(name="grid")
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
    type=click.Choice(["A3", "A4", "A5", "LETTER"]),
    default="A4",
    help="Paper size for the imposed document",
)
def impose_grid(input_files: list[Path], output_file: Path, paper: str):
    """Impose multiple PDF files into a grid layout on a single PDF."""

    pages = gather_pdf_pages(input_files)

    if not pages:
        raise ValueError("No PDF pages found in the provided input files.")

    print(f"Imposing {len(pages)} PDF pages into a grid layout...")

    writer = impose_pages_grid(pages, paper=paper)

    with output_file.open("wb") as f:
        writer.write(f)

    print(f"Imposed PDF saved to {output_file}")
