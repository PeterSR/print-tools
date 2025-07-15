# Architecture

This document describes the architecture and design principles of Print Tools.

## Project Structure

```
print_tools/
├── __init__.py          # Package metadata and exports
├── __main__.py          # Entry point for python -m print_tools
├── cli/                 # Command-line interface
│   ├── cli.py          # Main CLI entry point
│   ├── concat.py       # Concatenation commands
│   ├── imposition.py   # Imposition commands
│   ├── split.py        # Splitting commands
│   └── templating.py   # Templating commands
├── core/               # Core business logic
│   ├── concat.py       # PDF concatenation
│   ├── imposition.py   # Page imposition
│   ├── split.py        # Page splitting
│   └── templating.py   # Template processing
└── utils/              # Utility modules
    ├── embed.py        # Page embedding utilities
    ├── paper.py        # Paper size definitions
    ├── parsing.py      # Text parsing utilities
    ├── utils.py        # General utilities
    └── layouting/      # Layout algorithms
        ├── algorithms.py   # Layout implementations
        ├── models.py      # Data models
        ├── helpers.py     # Helper functions
        └── errors.py      # Custom exceptions
```

## Design Principles

### Separation of Concerns

- **CLI Layer**: Handles user input, argument parsing, and output formatting
- **Core Layer**: Contains business logic and PDF manipulation
- **Utils Layer**: Provides reusable utilities and algorithms

### Modularity

Each command is implemented as a separate module with:
- CLI interface in `cli/`
- Core logic in `core/`
- Shared utilities in `utils/`

### Type Safety

- All public APIs have type hints
- Pydantic models for data validation
- MyPy for static type checking

### Error Handling

- Custom exception classes for different error types
- Graceful error messages for CLI users
- Proper error propagation through the stack

## Key Components

### Layout System

The layout system is built around these core concepts:

- **Container**: Available space for placing content
- **Box**: Content that needs to be placed
- **Layouter**: Algorithm that arranges boxes in containers
- **AppliedBox**: A box that has been positioned in a container

### PDF Processing Pipeline

1. **Input Validation**: Check file existence and format
2. **Page Gathering**: Collect pages from input files
3. **Layout Calculation**: Determine page positions
4. **PDF Generation**: Create output with positioned pages

### CLI Architecture

- Rich-Click for enhanced CLI experience
- Hierarchical command structure
- Consistent argument patterns across commands
- Comprehensive help text

## Extension Points

### Adding New Layout Algorithms

1. Inherit from `BaseLayouter`
2. Implement `perform_layout()` method
3. Add CLI command in appropriate module
4. Add tests for new algorithm

### Adding New Commands

1. Create core logic in `core/`
2. Add CLI interface in `cli/`
3. Register command in main CLI
4. Add documentation and tests

### Supporting New Paper Sizes

1. Add size definition to `utils/paper.py`
2. Update CLI choices in relevant commands
3. Add tests for new size
