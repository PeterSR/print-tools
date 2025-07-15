# Contributing to Print Tools

We love your input! We want to make contributing to Print Tools as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/print-tools.git
   cd print-tools
   ```

2. **Install UV** (recommended)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**
   ```bash
   uv sync --all-extras
   ```

4. **Install pre-commit hooks**
   ```bash
   uv run pre-commit install
   ```

## Code Style

We use several tools to maintain code quality:

- **Ruff**: For linting and formatting
- **MyPy**: For type checking
- **Black**: For code formatting (via Ruff)
- **Pre-commit**: For running checks automatically

Run all checks locally:
```bash
uv run ruff check .
uv run ruff format .
uv run mypy print_tools
```

## Testing

We use pytest for testing. Run tests with:

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=print_tools

# Run only unit tests
uv run pytest tests/unit/

# Run only integration tests
uv run pytest tests/integration/ -m integration
```

### Writing Tests

- Unit tests go in `tests/unit/`
- Integration tests go in `tests/integration/`
- Use descriptive test names and docstrings
- Follow the AAA pattern: Arrange, Act, Assert
- Use fixtures from `conftest.py` for common test data

## Documentation

We use MkDocs with Material theme for documentation.

Build and serve documentation locally:
```bash
uv run mkdocs serve
```

## Submitting Changes

1. **Create an issue** describing the problem or feature
2. **Fork the repository** and create a feature branch
3. **Make your changes** with tests and documentation
4. **Run the test suite** and ensure all checks pass
5. **Submit a pull request** with a clear description

## Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we pledge to make participation in our project and community a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue with the "question" label if you need help or have questions about contributing.
