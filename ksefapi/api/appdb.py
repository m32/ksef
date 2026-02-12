from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    Index,
    ForeignKey,
    UniqueConstraint,
    Boolean,
    BigInteger,
    Integer,
    Float,
    String,
    Text,
    Uuid,
    Date,
    DateTime,
)
class Decimal(Float):
        def __init__(self, a, b, *args, **kwargs):
             super().__init__(a, *args, **kwargs)

from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///ksef.sqlite3'
SQLALCHEMY_ARGS={"check_same_thread": False}    # only needed for SQLite

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=SQLALCHEMY_ARGS,
#    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
