# Development Setup

This guide will help you set up a development environment for Print Tools.

## Prerequisites

- Python 3.13 or higher
- Git
- UV (recommended) or pip

## Setting Up the Environment

### 1. Clone the Repository

```bash
git clone https://github.com/username/print-tools.git
cd print-tools
```

### 2. Install UV (Recommended)

UV is a fast Python package manager. Install it:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Install Dependencies

```bash
# Install all dependencies including dev tools
uv sync --all-extras

# Or just development dependencies
uv sync --extra dev
```

### 4. Install Pre-commit Hooks

```bash
uv run pre-commit install
```

## Alternative: Using pip

If you prefer using pip:

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Development Workflow

### Running the Application

```bash
# Using UV
uv run python -m print_tools --help

# Or activate environment and run directly
source .venv/bin/activate
python -m print_tools --help
```

### Code Quality Checks

```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy print_tools

# All quality checks
make quality
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=print_tools --cov-report=html

# Run specific test categories
uv run pytest tests/unit/          # Unit tests only
uv run pytest tests/integration/   # Integration tests only
```

### Documentation

```bash
# Build documentation
uv run mkdocs build

# Serve documentation locally
uv run mkdocs serve
```

Visit http://localhost:8000 to view the documentation.

## IDE Setup

### VS Code

Recommended extensions:
- Python
- Pylance
- Ruff
- MyPy Type Checker

### PyCharm

Configure:
- Python interpreter to use the virtual environment
- Enable type checking
- Set up Ruff as the linter and formatter

## Common Development Tasks

### Adding a New Feature

1. Create a feature branch
2. Write tests first (TDD)
3. Implement the feature
4. Update documentation
5. Run quality checks
6. Submit a pull request

### Debugging

Use Python's built-in debugger:

```python
import pdb; pdb.set_trace()
```

Or use your IDE's debugging capabilities.

### Performance Testing

For performance-critical changes:

```bash
# Time execution
time uv run python -m print_tools concat *.pdf -o output.pdf

# Profile with cProfile
uv run python -m cProfile -s tottime -m print_tools concat *.pdf -o output.pdf
```

## Makefile Commands

We provide a Makefile for common tasks:

```bash
make help           # Show all available commands
make install        # Install development dependencies
make test           # Run tests
make test-cov       # Run tests with coverage
make lint           # Run linting
make format         # Format code
make docs           # Build documentation
make clean          # Clean build artifacts
```

## Troubleshooting

### UV Issues

If UV isn't working:
1. Ensure it's in your PATH
2. Try reinstalling: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Use pip as fallback

### Import Errors

If you get import errors:
1. Ensure you've installed in development mode: `uv sync` or `pip install -e .`
2. Check your PYTHONPATH
3. Verify virtual environment is activated

### Test Failures

If tests are failing:
1. Ensure all dependencies are installed
2. Check if you need test data files
3. Run tests in verbose mode: `pytest -v`

## Getting Help

- Check existing issues on GitHub
- Ask questions in discussions
- Review the contributing guide
- Contact maintainers
