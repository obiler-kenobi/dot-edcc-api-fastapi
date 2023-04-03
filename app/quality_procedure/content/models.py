from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.database import Base

class QPScope(Base):
    __tablename__ = "qp_scope"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    scope = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_scope")

class QPDefinitionOfTerm(Base):
    __tablename__ = "qp_definition_of_term"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    term = Column(String(80), nullable=False)
    definition = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_definition_of_term")