# Print Tools

Professional PDF manipulation tools for prepress, printing and publishing workflows.

[![CI](https://github.com/username/print-tools/workflows/CI/badge.svg)](https://github.com/username/print-tools/actions)
[![codecov](https://codecov.io/gh/username/print-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/username/print-tools)
[![PyPI version](https://badge.fury.io/py/print-tools.svg)](https://badge.fury.io/py/print-tools)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Features

Print Tools provides a comprehensive set of utilities for working with PDF documents in professional printing and publishing environments:

- **Concatenation**: Merge multiple PDF files into a single document
- **Imposition**: Arrange pages for efficient printing with multiple layout options:
  - Grid layout for simple arrangements
  - Booklet layout for saddle-stitched publications
  - Pack layout for optimal space utilization
- **Splitting**: Divide large pages into smaller sections
- **Templating**: Overlay text content onto PDF templates

## Quick Start

### Installation

```bash
pip install print-tools
```

### Basic Usage

```bash
# Concatenate PDFs
print-tools concat file1.pdf file2.pdf file3.pdf -o combined.pdf

# Create a booklet layout
print-tools imposition booklet pages.pdf -o booklet.pdf --paper A4

# Split pages
print-tools split large-pages.pdf -o split-pages.pdf --target-paper A5

# Generate PDFs from template
print-tools templating overlay template.pdf text-blocks.txt output-dir/
```

## Key Benefits

- **Professional Quality**: Designed for prepress and commercial printing workflows
- **Flexible Layouts**: Multiple imposition algorithms for different use cases
- **Command Line Interface**: Easy integration into automated workflows
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Python API**: Programmatic access to all functionality

## Use Cases

- **Print Shops**: Efficient page imposition for various print jobs
- **Publishers**: Automated layout generation for books and magazines
- **Marketing**: Batch processing of promotional materials
- **Educational**: Creating handouts and course materials
- **Personal Projects**: Organizing documents for home printing

## Documentation

Visit our [documentation](https://username.github.io/print-tools) for detailed usage guides, API reference, and examples.

## Contributing

We welcome contributions! Please see our [contributing guide](developer-guide/contributing.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/username/print-tools/blob/main/LICENSE) file for details.
