from sqlalchemy import TIMESTAMP, Text, Column, ForeignKey, Integer, String, DATE, Text
from sqlalchemy.orm import relationship

from app.database import Base

class QualityProcedureRequests(Base): 
    __tablename__ = "quality_procedure_requests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quality_procedure_id = Column(Integer, nullable=False) 
    request_type = Column(String(10), nullable=False)
    document_title = Column(String(150), nullable=False)
    document_number = Column(String(100), nullable=True)
    request_purpose = Column(Text, nullable=False)
    revision_type = Column(String(10), nullable=False)
    revision_number = Column(Integer, nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"))
    status_actions_id = Column(Integer, ForeignKey("status_actions.id"))
    requested_by = Column(Integer, ForeignKey("user.id"))
    date_created = Column(TIMESTAMP, nullable=False)
    date_updated = Column(TIMESTAMP, nullable=False)

    status = relationship("Status", back_populates="quality_procedure_requests")
    status_actions = relationship("StatusActions", back_populates="quality_procedure_requests")
    user = relationship("User", back_populates="quality_procedure_requests")
    quality_procedure_request_history = relationship("QualityProcedureRequestHistory", back_populates="quality_procedure_requests")

class QualityProcedureRequestHistory(Base):
    __tablename__ = "quality_procedure_request_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    request_id = Column(Integer, ForeignKey("quality_procedure_requests.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    status_actions_id = Column(Integer, ForeignKey("status_actions.id"))
    remarks = Column(Text, nullable=True)
    date_created = Column(DATE, nullable=False)
    time_created = Column(TIMESTAMP, nullable=False)

    quality_procedure_requests = relationship("QualityProcedureRequests", back_populates="quality_procedure_request_history")
    user = relationship("User", back_populates="quality_procedure_request_history")
    status = relationship("Status", back_populates="quality_procedure_request_history")
    status_actions = relationship("StatusActions", back_populates="quality_procedure_request_history")