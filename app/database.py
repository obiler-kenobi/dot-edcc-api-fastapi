from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1111@localhost/edccapp"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)