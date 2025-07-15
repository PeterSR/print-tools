# Quick Start Guide

This guide will help you get started with Print Tools quickly.

## Basic Commands

### Concatenating PDFs

Combine multiple PDF files into one:

```bash
print-tools concat file1.pdf file2.pdf file3.pdf -o combined.pdf
```

You can also use directories containing PDF files:

```bash
print-tools concat path/to/pdf/folder/ -o combined.pdf
```

### Imposition Layouts

#### Grid Layout

Arrange pages in a simple grid:

```bash
print-tools imposition grid pages.pdf -o imposed.pdf --paper A4 --padding 10 --gap 5
```

#### Booklet Layout

Create a booklet with proper page ordering for saddle-stitching:

```bash
print-tools imposition booklet pages.pdf -o booklet.pdf --paper A4
```

#### Pack Layout

Optimize space usage by packing pages efficiently:

```bash
print-tools imposition pack pages.pdf -o packed.pdf --paper A3-landscape
```

### Splitting Pages

Split large pages into smaller sections:

```bash
print-tools split large-pages.pdf -o split.pdf --target-paper A5
```

### Templating

Generate multiple PDFs from a template and text content:

```bash
print-tools templating overlay template.pdf blocks.txt output-directory/
```

The `blocks.txt` file should contain text blocks separated by `---`:

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

## Common Use Cases

### Creating Business Cards

```bash
# Arrange business card designs on a sheet
print-tools imposition grid business-card.pdf -o sheet.pdf --paper A4 --gap 2
```

### Making a Booklet

```bash
# Create a properly imposed booklet
print-tools imposition booklet my-document.pdf -o booklet.pdf --paper A4
```

### Batch Label Generation

```bash
# Generate address labels from a template
print-tools templating overlay label-template.pdf addresses.txt labels/
```

## Tips

- Use `--help` with any command to see all available options
- Paper sizes support both portrait and landscape orientations (e.g., `A4-landscape`)
- For large jobs, consider testing with a few pages first
- Check output files before sending to production printing
