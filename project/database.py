"""Database connection details"""
from os import getenv

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

POSTGRES_USER = getenv("PGUSER", "postgres")
POSTGRES_HOST = getenv("PGHOST", "localhost")
POSTGRES_PORT = getenv("PGPORT", 5432)
POSTGRES_PASSWORD = getenv("PGPASSWORD", "postgres")
DB_NAME = getenv("DBNAME", "_test")
DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}"


# SQLAlchemy Session
engine = create_engine(DB_URL)
Session = sessionmaker(engine)


def db_connection(dbname=None):
    """Get a psycopg2 connection to the database."""
    conn = psycopg2.connect(
        user=POSTGRES_USER,
        host=POSTGRES_HOST,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT,
        dbname=dbname,
    )
    conn.autocommit = True
    return conn
