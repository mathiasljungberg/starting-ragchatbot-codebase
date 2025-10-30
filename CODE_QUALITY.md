# Code Quality Tools

This project uses modern Python code quality tools to ensure consistent, maintainable, and error-free code.

## Tools Included

### 1. Ruff (Linting & Formatting)
Ruff is an extremely fast Python linter and formatter that replaces multiple tools (flake8, isort, black, etc.).

**What it checks:**
- Code style (PEP 8)
- Potential bugs and errors
- Import sorting
- Code simplifications
- Unused variables and imports
- And much more

### 2. MyPy (Type Checking)
Static type checker for Python that helps catch type-related bugs before runtime.

### 3. Pytest (Testing)
Modern testing framework with:
- Test discovery
- Fixtures
- Async support
- Coverage reporting

### 4. Pre-commit (Git Hooks)
Automatically runs quality checks before each commit to catch issues early.

## Quick Start

### Install Development Dependencies
```bash
make install-dev
# or
uv sync --extra dev
```

### Install Pre-commit Hooks
```bash
make pre-commit
# or
uv run pre-commit install
```

## Available Commands

Use the Makefile for convenience:

```bash
# Format code automatically
make format

# Check for linting errors
make lint

# Run type checking
make type-check

# Run tests
make test

# Run tests with coverage report
make test-cov

# Run all quality checks at once
make quality

# Clean cache files
make clean

# Show all available commands
make help
```

## Manual Commands

If you prefer to run tools directly:

```bash
# Format code
uv run ruff format .

# Auto-fix linting issues
uv run ruff check --fix .

# Check for linting errors (no fix)
uv run ruff check .

# Type checking
uv run mypy backend/

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=backend --cov-report=html --cov-report=term

# Pre-commit on all files
uv run pre-commit run --all-files
```

## Configuration

All tool configurations are in `pyproject.toml`:

- **Ruff**: Lines 29-53
  - Line length: 100 characters
  - Target: Python 3.13
  - Selected rules: pycodestyle, pyflakes, isort, bugbear, comprehensions, pyupgrade, etc.

- **MyPy**: Lines 55-60
  - Python version: 3.13
  - Currently lenient (ignore_missing_imports=true)
  - Can be made stricter by setting disallow_untyped_defs=true

- **Pytest**: Lines 62-84
  - Test directory: tests/
  - Auto coverage reporting
  - Async support enabled

## Pre-commit Hooks

Pre-commit hooks automatically run before each commit:

1. **Basic checks**: trailing whitespace, file endings, YAML/JSON validation
2. **Ruff**: Auto-format and lint
3. **MyPy**: Type checking

To skip hooks temporarily (not recommended):
```bash
git commit --no-verify
```

## Testing

### Running Tests
```bash
make test              # Run all tests
make test-cov          # Run with coverage report (HTML + terminal)
```

### Writing Tests
Place tests in the `tests/` directory:

```python
# tests/test_example.py
def test_something():
    assert 1 + 1 == 2
```

For FastAPI tests, use the provided test_client fixture:
```python
def test_api_endpoint(test_client):
    response = test_client.get("/api/courses")
    assert response.status_code == 200
```

### Coverage Reports
After running `make test-cov`, open `htmlcov/index.html` in your browser to see detailed coverage.

## IDE Integration

### VS Code
Install these extensions:
- **Ruff** (charliermarsh.ruff)
- **Pylance** (ms-python.vscode-pylance)

Add to `.vscode/settings.json`:
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "python.linting.enabled": true,
  "python.analysis.typeCheckingMode": "basic"
}
```

### PyCharm
PyCharm has built-in support for most tools. Configure:
- **Settings → Tools → Ruff**: Enable as formatter and linter
- **Settings → Editor → Inspections**: Enable MyPy integration

## CI/CD Integration

Add to your CI pipeline (GitHub Actions example):

```yaml
name: Code Quality
on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --extra dev
      - run: uv run ruff check .
      - run: uv run mypy backend/
      - run: uv run pytest --cov
```

## Best Practices

1. **Run quality checks before committing**: Use `make quality`
2. **Keep coverage high**: Aim for >80% test coverage
3. **Fix linting errors**: Don't ignore warnings without good reason
4. **Add type hints**: Gradually add type hints to improve type checking
5. **Write tests first**: Follow TDD when possible

## Troubleshooting

### Pre-commit hooks not running
```bash
make pre-commit  # Reinstall hooks
```

### Ruff errors in IDE
Reload your IDE window after installing ruff

### MyPy false positives
Add `# type: ignore` comments sparingly, or configure in pyproject.toml

### Tests not discovered
Ensure test files start with `test_` and functions start with `test_`

## Further Reading

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
