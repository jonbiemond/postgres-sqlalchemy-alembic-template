# Postgres, SQLAlchemy and Alembic Template
Template for creating a project using Postgres, SQLAlchemy and Alembic.

## Usage

1. Fork project and title your new project.
`gh repo fork jonbiemond/postgres-sqlalchemy-alembic-template --clone --fork-name <new project> --remote-name <new project>`
2. Install dependencies: `poetry install`
3. Refactor project directory to project name and set in `pyproject.toml`.
4. Create `.env` file and set `DBNAME`. Optionally set credentials, otherwise `postgres` defaults are used.
5. Run `init_db.py` to initialize database.
6. Declare models.
