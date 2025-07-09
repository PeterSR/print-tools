import rich_click as click
from pathlib import Path

from ..core.concat import concat_pdfs


@click.command(name="concat")
@click.argument("input_files", nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option(
    "-o",
    "--output-file",
    type=click.Path(path_type=Path),
    default=Path("output.pdf"),
    help="Output file path for the concatenated PDF",
)
def cli(input_files: list[Path], output_file: Path):
    """Concatenate multiple PDF files into a single PDF."""
    concat_pdfs(input_files, output_file)
