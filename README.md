# print-tools

Scripts and other tools for working with PDFs for prepress, printing and publishing.



## Usage

```console
$ python -m print_tools --help

 Usage: python -m print_tools [OPTIONS] COMMAND [ARGS]...

 Print Tools CLI for generating and manipulating PDF documents.

╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --help      Show this message and exit.                                   │
╰───────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────╮
│ concat        Concatenate multiple PDF files into a single PDF.           │
│ imposition    Perform various imposition layouts on PDF files.            │
│ split         Split PDF pages into multiple smaller pages.                │
│ templating    Generate PDFs from a PDF template and source material.      │
╰───────────────────────────────────────────────────────────────────────────╯
```


Especially the `imposition` might be of interest:

```console
$ python -m print_tools imposition --help

 Usage: python -m print_tools imposition [OPTIONS] COMMAND [ARGS]...

 Perform various imposition layouts on PDF files.

╭─ Options ─────────────────────────────────────────────────────────────────╮
│ --help      Show this message and exit.                                   │
╰───────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────╮
│ booklet  Impose multiple PDF files into a booklet layout on a single PDF. │
│ grid     Impose multiple PDF files into a grid layout on a single PDF.    │
│ pack     Impose multiple PDF files into a packed layout on a single PDF.  │
╰───────────────────────────────────────────────────────────────────────────╯
```
