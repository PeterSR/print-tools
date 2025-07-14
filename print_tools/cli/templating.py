from pathlib import Path

import rich_click as click

from ..core.templating import create_labeled_pdfs


@click.group(name="templating")
def cli():
    """Generate PDFs from a PDF template and source material."""
    pass


@cli.command(name="overlay")
@click.argument("template", type=click.Path(exists=True, path_type=Path))
@click.argument("blocks", type=click.Path(exists=True, path_type=Path))
@click.argument("output_dir", type=click.Path(path_type=Path))
@click.option(
    "--font",
    default="Helvetica",
    help="Font name or path to TTF/OTF file",
)
@click.option(
    "--size",
    default=18,
    help="Font size in points",
)
@click.option(
    "--spacing",
    default=4,
    help="Extra space between lines in points",
)
@click.option(
    "--colour",
    default="#000000",
    help="Text color: reportlab color name or #RRGGBB hex code",
)
def overlay_text(
    template: Path,
    blocks: Path,
    output_dir: Path,
    font: str,
    size: int,
    spacing: int,
    colour: str,
):
    """
    Overlay blocks of text on a PDF template.

    TEMPLATE: Path to the PDF template file
    BLOCKS: Path to text file with blocks separated by --- lines
    OUTPUT_DIR: Directory to save the generated PDFs
    """
    create_labeled_pdfs(
        template_path=template,
        blocks_path=blocks,
        output_dir=output_dir,
        font_name=font,
        font_size=size,
        line_spacing=spacing,
        text_colour=colour,
    )
