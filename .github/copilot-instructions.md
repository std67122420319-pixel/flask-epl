# Flask-EPL Copilot Instructions

## Project Overview
Flask-EPL is an early-stage Flask web application with SQLAlchemy ORM integration. The project uses `uv` for dependency management (see `pyproject.toml` and `uv.lock`) and Python 3.14+.

## Project Structure
- **main.py**: Entry point with placeholder `main()` function
- **epl/**: Application package (currently empty) - where Flask app, blueprints, models, and routes will be implemented
- **pyproject.toml**: Package metadata and dependencies (Flask 3.1.2+, Flask-SQLAlchemy 3.1.1+)

## Key Technologies & Versions
- **Flask**: 3.1.2+ (web framework)
- **Flask-SQLAlchemy**: 3.1.1+ (ORM integration)
- **Python**: 3.14
- **Package Manager**: uv (not pip)

## Development Commands
- **Install dependencies**: `uv sync` (uses `uv.lock` for reproducible installs)
- **Run application**: `python main.py` (entry point is main.py)
- **Add packages**: `uv add <package_name>` (updates pyproject.toml and uv.lock)

## Development Patterns
When implementing Flask features:
1. **Application Factory Pattern**: Expect Flask app creation in `epl/` (likely in `__init__.py` or dedicated factory module)
2. **Blueprints**: Use Flask blueprints for route organization in `epl/` submodules
3. **Models**: Define SQLAlchemy models in dedicated modules within `epl/`
4. **Database**: Flask-SQLAlchemy will use relative imports from the epl package

## Important Notes
- The `epl/` directory is empty - all application code needs to be scaffolded
- No existing tests, templates, or static files yet
- `.venv` is in `.gitignore` - respect virtual environment isolation
- `uv.lock` must be committed to ensure reproducible environments
