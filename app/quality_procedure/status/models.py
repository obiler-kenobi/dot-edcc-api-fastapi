
from sqlalchemy import TIMESTAMP, TIME, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from app.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(150), nullable=False)
    status_description = Column(String(150), nullable=False)
    status_placement = Column(Integer, nullable=True)
    created_by = Column(String(100), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    date_updated = Column(TIMESTAMP, nullable=True)

    quality_procedure_requests = relationship("QualityProcedureRequests", back_populates="status")
    quality_procedure_request_history = relationship("QualityProcedureRequestHistory", back_populates="status")

class StatusActions(Base):
    __tablename__ = "status_actions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    action = Column(String(100), nullable=False)
    action_description = Column(String(150), nullable=False)
    action_color = Column(String(50), nullable=False)
    created_by = Column(String(100), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    date_updated = Column(TIMESTAMP, nullable=True)

    quality_procedure_requests = relationship("QualityProcedureRequests", back_populates="status_actions")
    quality_procedure_request_history = relationship("QualityProcedureRequestHistory", back_populates="status_actions")