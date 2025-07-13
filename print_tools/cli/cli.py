import rich_click as click
from .imposition import cli as imposition
from .templating import cli as templating
from .concat import cli as concat
from .split import cli as split


@click.group()
def cli():
    """Print Tools CLI for generating and manipulating PDF documents."""
    pass


cli.add_command(imposition)
cli.add_command(templating)
cli.add_command(concat)
cli.add_command(split)


if __name__ == "__main__":
    cli()
