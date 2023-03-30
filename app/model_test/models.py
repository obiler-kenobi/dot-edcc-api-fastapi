
from sqlalchemy import  Column, Integer
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base

class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sample = Column(JSONB, nullable=False)