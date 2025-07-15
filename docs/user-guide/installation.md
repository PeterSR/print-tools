# Installation

## Requirements

- Python 3.13 or higher
- Operating System: Windows, macOS, or Linux

## Installing from PyPI

The recommended way to install Print Tools is using pip:

```bash
pip install print-tools
```

## Installing with UV (Recommended for Development)

If you're using [UV](https://docs.astral.sh/uv/) for Python package management:

```bash
uv add print-tools
```

## Installing from Source

To install the latest development version:

```bash
git clone https://github.com/username/print-tools.git
cd print-tools
pip install -e .
```

## Verification

Verify your installation by running:

```bash
print-tools --help
```

You should see the main help message with available commands.

## Dependencies

Print Tools has the following core dependencies:

- `pypdf`: PDF manipulation
- `reportlab`: PDF generation
- `rich-click`: Enhanced CLI interface
- `pydantic`: Data validation

These will be automatically installed when you install Print Tools.

## Troubleshooting

### Permission Errors

If you encounter permission errors during installation, try:

```bash
pip install --user print-tools
```

### Python Version Issues

Ensure you're using Python 3.13 or higher:

```bash
python --version
```

If you have multiple Python versions installed, you may need to use:

```bash
python3.13 -m pip install print-tools
```
