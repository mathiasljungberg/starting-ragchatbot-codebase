.PHONY: help install install-dev format lint type-check test test-cov quality pre-commit clean

help:
	@echo "Available commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make format        - Format code with ruff"
	@echo "  make lint          - Lint code with ruff"
	@echo "  make type-check    - Run type checking with mypy"
	@echo "  make test          - Run tests with pytest"
	@echo "  make test-cov      - Run tests with coverage report"
	@echo "  make quality       - Run all quality checks (format, lint, type-check, test)"
	@echo "  make pre-commit    - Install pre-commit hooks"
	@echo "  make clean         - Remove cache and temporary files"

install:
	uv sync

install-dev:
	uv sync --extra dev

format:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff check .

type-check:
	uv run mypy backend/

test:
	uv run pytest

test-cov:
	uv run pytest --cov=backend --cov-report=html --cov-report=term

quality: format lint type-check test
	@echo "All quality checks passed!"

pre-commit:
	uv run pre-commit install
	@echo "Pre-commit hooks installed!"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "Cleanup complete!"
