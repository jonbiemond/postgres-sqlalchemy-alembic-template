"""Create database and initalize schema.

WARNING: If db exists, all data will be dropped.
"""
from alembic import config
from sqlalchemy import Engine

from database import DB_NAME, db_connection, Session


def create_db(dbname):
    """Create an empty database with the given name if it does not exist."""
    with db_connection().cursor() as cur:
        cur.execute(f"SELECT datname FROM pg_database WHERE datname = '{dbname}';")
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {dbname};")
        else:
            with db_connection(dbname).cursor() as db_cur:
                db_cur.execute(
                    """
                    DROP SCHEMA public CASCADE;
                    CREATE SCHEMA public;"""
                )
                

def create_schema(engine: Engine):
    alembic_cfg = config.Config("alembic.ini")
    with engine.begin() as connection:
        alembic_cfg.attributes['connection'] = connection
        # alembic_cfg.attributes['script_location'] = r'.\alembic'
        config.command.upgrade(alembic_cfg, "head")
    

def populate_db(session: Session):
    pass


if __name__ == '__main__':
    
    # Create Database
    create_db(DB_NAME)
    with db_connection().cursor() as cur:
        cur.execute(f"SELECT datname FROM pg_database WHERE datname = '{DB_NAME}';")
        assert cur.fetchone() is not None
    
    # Create Schema
    session = Session()
    create_schema(session.bind)
    with db_connection(DB_NAME).cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name = 'alembic_version';")
        assert cur.fetchone() is not None
        
    # Populate Database
    with Session() as session:
        populate_db(session)
    with db_connection(DB_NAME).cursor() as cur:
        # assert test data exists
        pass
        