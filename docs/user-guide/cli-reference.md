# CLI Reference

Complete reference for all Print Tools command-line interface commands.

## Global Options

All commands support these global options:

- `--help`: Show help message and exit

## Commands Overview

- `concat`: Concatenate multiple PDF files
- `imposition`: Perform page layout operations
- `split`: Split PDF pages by size
- `templating`: Generate PDFs from templates

## concat

Concatenate multiple PDF files into a single PDF document.

```bash
print-tools concat [OPTIONS] INPUT_FILES...
```

### Arguments

- `INPUT_FILES`: One or more PDF files or directories containing PDFs

### Options

- `-o, --output-file PATH`: Output file path (default: `output.pdf`)

### Examples

```bash
# Concatenate specific files
print-tools concat file1.pdf file2.pdf file3.pdf -o combined.pdf

# Concatenate all PDFs in a directory
print-tools concat /path/to/pdfs/ -o all-files.pdf

# Mix files and directories
print-tools concat intro.pdf /path/to/chapters/ conclusion.pdf -o book.pdf
```

## imposition

Perform various imposition layouts on PDF files for efficient printing.

```bash
print-tools imposition [OPTIONS] COMMAND [ARGS]...
```

### Subcommands

#### grid

Arrange pages in a simple rectangular grid.

```bash
print-tools imposition grid [OPTIONS] INPUT_FILES...
```

**Options:**
- `-o, --output-file PATH`: Output file path (default: `output.pdf`)
- `-p, --paper CHOICE`: Paper size - A3, A3-landscape, A4, A4-landscape, A5, A5-landscape (default: A4)
- `--padding INTEGER`: Padding around the grid in points (default: 0)
- `--gap INTEGER`: Gap between pages in points (default: 0)

**Example:**
```bash
print-tools imposition grid business-cards.pdf -o sheet.pdf --paper A4 --gap 5
```

#### booklet

Create a booklet layout with proper page ordering for saddle-stitching.

```bash
print-tools imposition booklet [OPTIONS] INPUT_FILES...
```

**Options:**
- `-o, --output-file PATH`: Output file path (default: `output.pdf`)
- `-p, --paper CHOICE`: Paper size (default: A4)
- `--padding INTEGER`: Padding in points (default: 0)
- `--gap INTEGER`: Gap between pages in points (default: 0)

**Example:**
```bash
print-tools imposition booklet my-document.pdf -o booklet.pdf --paper A4
```

#### pack

Optimize space usage by packing pages efficiently.

```bash
print-tools imposition pack [OPTIONS] INPUT_FILES...
```

**Options:**
- `-o, --output-file PATH`: Output file path (default: `output.pdf`)
- `-p, --paper CHOICE`: Paper size (default: A4)
- `--padding INTEGER`: Padding in points (default: 0)
- `--gap INTEGER`: Gap between pages in points (default: 0)

**Example:**
```bash
print-tools imposition pack mixed-sizes.pdf -o optimized.pdf --paper A3-landscape
```

## split

Split PDF pages into multiple smaller pages based on target paper size.

```bash
print-tools split [OPTIONS] INPUT_FILES...
```

### Options

- `-o, --output-file PATH`: Output file path (default: `output.pdf`)
- `-p, --target-paper CHOICE`: Target paper size for splitting (default: A4)

### Examples

```bash
# Split A3 pages into A4 pages
print-tools split large-document.pdf -o split.pdf --target-paper A4

# Split to A5 landscape
print-tools split poster.pdf -o sections.pdf --target-paper A5-landscape
```

## templating

Generate PDFs from templates with dynamic content.

```bash
print-tools templating [OPTIONS] COMMAND [ARGS]...
```

### Subcommands

#### overlay

Overlay text blocks onto a PDF template.

```bash
print-tools templating overlay [OPTIONS] TEMPLATE BLOCKS OUTPUT_DIR
```

**Arguments:**
- `TEMPLATE`: Path to the PDF template file
- `BLOCKS`: Path to text file with content blocks
- `OUTPUT_DIR`: Directory to save generated PDFs

**Options:**
- `--font TEXT`: Font name or path to TTF/OTF file (default: Helvetica)
- `--size INTEGER`: Font size in points (default: 18)
- `--spacing INTEGER`: Extra space between lines in points (default: 4)
- `--colour TEXT`: Text color - name or #RRGGBB hex (default: #000000)

**Text Block Format:**

The blocks file should contain text blocks separated by `---` lines:

```
First Label
Line 1
Line 2
---
Second Label
Another line
---
Third Label
Final content
```

**Example:**
```bash
print-tools templating overlay badge-template.pdf names.txt badges/ \
    --font Arial --size 24 --colour "#0000FF"
```

## Paper Sizes

Supported paper sizes and their dimensions:

| Size | Portrait (pts) | Landscape (pts) |
|------|----------------|-----------------|
| A3 | 842 × 1191 | 1191 × 842 |
| A4 | 595 × 842 | 842 × 595 |
| A5 | 420 × 595 | 595 × 420 |

## Tips and Best Practices

### File Handling
- Use absolute paths when possible
- Test with small files first for large jobs
- Ensure sufficient disk space for output files

### Performance
- Large files may take time to process
- Consider splitting very large jobs into smaller batches
- Use SSD storage for better performance

### Quality Control
- Always review output files before production printing
- Test impose layouts with a few pages first
- Verify measurements match your printing requirements

### Troubleshooting
- Use `--help` with any command for detailed information
- Check file permissions if encountering access errors
- Ensure input files are valid PDFs
