# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive test suite with unit and integration tests
- GitHub Actions CI/CD pipeline
- Pre-commit hooks for code quality
- Complete documentation with MkDocs
- Type hints throughout the codebase
- Professional project structure

### Changed
- Updated pyproject.toml with comprehensive metadata
- Improved error handling and validation
- Enhanced CLI interface with better help messages

### Fixed
- Various code quality improvements
- Linting and formatting issues

## [0.1.0] - 2025-01-14

### Added
- Initial release of print-tools
- PDF concatenation functionality
- Imposition layouts (grid, booklet, pack)
- PDF splitting by target size
- Template-based PDF generation
- Command-line interface with rich-click
- Support for A3, A4, A5 paper sizes in portrait and landscape
- Basic layouting algorithms for page arrangement

### Features
- **Concat**: Merge multiple PDF files into one
- **Imposition**: Professional page layout for printing
  - Grid layout for simple arrangements
  - Booklet layout for saddle-stitched publications
  - Pack layout for space optimization
- **Split**: Divide pages by target paper size
- **Templating**: Overlay text blocks on PDF templates

[Unreleased]: https://github.com/username/print-tools/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/username/print-tools/releases/tag/v0.1.0
