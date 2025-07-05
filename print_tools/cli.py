import rich_click as click
from print_tools.imposition.cli import cli as imposition
from print_tools.templating.cli import cli as templating


@click.group()
def cli():
    """Print Tools CLI for generating and manipulating PDF documents."""
    pass


cli.add_command(imposition)
cli.add_command(templating)


if __name__ == "__main__":
    cli()
