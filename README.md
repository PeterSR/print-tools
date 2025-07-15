# Print Tools

[![CI](https://github.com/username/print-tools/workflows/CI/badge.svg)](https://github.com/username/print-tools/actions)
[![codecov](https://codecov.io/gh/username/print-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/username/print-tools)
[![PyPI version](https://badge.fury.io/py/print-tools.svg)](https://badge.fury.io/py/print-tools)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Professional PDF manipulation tools for prepress, printing and publishing workflows.

## ✨ Features

- **📄 Concatenation**: Merge multiple PDF files into a single document
- **📐 Imposition**: Professional page layouts for efficient printing
- **✂️ Splitting**: Divide large pages into smaller sections
- **🏷️ Templating**: Generate PDFs from templates with dynamic content
- **🖥️ CLI Interface**: Easy-to-use command-line tools
- **🐍 Python API**: Programmatic access to all functionality

## 🚀 Quick Start

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

## 📖 Documentation

For detailed documentation, visit: **[print-tools.readthedocs.io](https://print-tools.readthedocs.io)**

- [Installation Guide](https://print-tools.readthedocs.io/en/latest/user-guide/installation/)
- [Quick Start Tutorial](https://print-tools.readthedocs.io/en/latest/user-guide/quickstart/)
- [CLI Reference](https://print-tools.readthedocs.io/en/latest/user-guide/cli-reference/)
- [API Documentation](https://print-tools.readthedocs.io/en/latest/api/)

## 🎯 Use Cases

- **Print Shops**: Efficient page imposition for commercial printing
- **Publishers**: Automated layout generation for books and magazines
- **Marketing**: Batch processing of promotional materials
- **Educational**: Creating handouts and course materials
- **Personal Projects**: Organizing documents for home printing

## 🛠️ Available Commands

### Concatenation
```bash
print-tools concat input1.pdf input2.pdf -o output.pdf
```

### Imposition Layouts

**Grid Layout** - Simple rectangular arrangements:
```bash
print-tools imposition grid pages.pdf -o imposed.pdf --paper A4 --padding 10 --gap 5
```

**Booklet Layout** - Professional saddle-stitched booklets:
```bash
print-tools imposition booklet pages.pdf -o booklet.pdf --paper A4
```

**Pack Layout** - Space-optimized arrangements:
```bash
print-tools imposition pack pages.pdf -o packed.pdf --paper A3-landscape
```

### Splitting
```bash
print-tools split large-doc.pdf -o split-pages.pdf --target-paper A5
```

### Templating
```bash
print-tools templating overlay template.pdf blocks.txt output-directory/
```

## 🔧 Development

### Setup

```bash
git clone https://github.com/username/print-tools.git
cd print-tools
uv sync --all-extras
uv run pre-commit install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=print_tools --cov-report=html

# Run only unit tests
uv run pytest tests/unit/

# Run integration tests
uv run pytest tests/integration/ -m integration
```

### Code Quality

```bash
# Lint and format
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy print_tools
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [PyPDF](https://pypdf.readthedocs.io/) for PDF manipulation
- CLI powered by [Rich-Click](https://github.com/ewels/rich-click)
- PDF generation using [ReportLab](https://www.reportlab.com/)

---

**Made with ❤️ for the printing and publishing community**
