.PHONY: help install test lint format type-check clean docs build release
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@egrep '^(.+)\s*:.*?##\s*(.+)' $(MAKEFILE_LIST) | column -t -c 2 -s ':#'

install: ## Install dependencies for development
	uv sync --all-extras
	uv run pre-commit install

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=print_tools --cov-report=html --cov-report=term-missing

test-unit: ## Run only unit tests
	uv run pytest tests/unit/

test-integration: ## Run only integration tests
	uv run pytest tests/integration/ -m integration

lint: ## Run linting
	uv run ruff check .

lint-fix: ## Run linting with auto-fix
	uv run ruff check . --fix

format: ## Format code
	uv run ruff format .

format-check: ## Check code formatting
	uv run ruff format --check .

type-check: ## Run type checking
	uv run mypy print_tools

security: ## Run security checks
	uv run pip install safety bandit
	uv run safety check
	uv run bandit -r print_tools/

quality: lint format-check type-check ## Run all quality checks

docs: ## Build documentation
	uv run mkdocs build

docs-serve: ## Serve documentation locally
	uv run mkdocs serve

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build package
	uv build

release: build ## Release package to PyPI
	uv run pip install twine
	uv run twine upload dist/*

dev-setup: install ## Set up development environment
	@echo "Development environment set up successfully!"
	@echo "Run 'make help' to see available commands."
