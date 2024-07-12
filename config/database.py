from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection details (replace with your actual configuration)
SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"

engine = None
SessionLocal = None

Base = declarative_base()

def initialize_setup(database_URL= None):
    """
    Use this to Initialize the Database Setup, input a database_URL to change the Default URL for Database Connection.
    Common use during Test Unit (Pytest) where We need to pass a URL for the in memory database.
    """
    global engine, SessionLocal, SQLALCHEMY_DATABASE_URL
    if (database_URL != None):
        SQLALCHEMY_DATABASE_URL = database_URL

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()