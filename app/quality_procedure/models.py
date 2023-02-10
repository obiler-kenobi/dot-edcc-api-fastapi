from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class QualityProcedureDocumentRequest(Base): 
    __tablename__ = "quality_procedure_document_request" #Temporary table name

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    request_date = Column(TIMESTAMP, nullable=False)
    request_purpose = Column(String(150), nullable=False)
    request_type = Column(String(10), nullable=False)
    document_title = Column(String(150), nullable=False)
    document_number = Column(String(100), nullable=True)
    status_id = Column(Integer, nullable=False)
    action_id = Column(Integer, nullable=False)

    qp_request_history = relationship("QPRequestHistory", back_populates="quality_procedure_document_request")

class QPRequestHistory(Base):
    __tablename__ = "qp_request_history" #QP = Quality Procedure

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    request_id = Column(Integer, ForeignKey("quality_procedure_document_request.id"))
    user_id = Column(Integer, nullable=False)
    comment = Column(String(150), nullable=False)
    comment_date = Column(TIMESTAMP, nullable=False) #Temporary Column Name

    quality_procedure_document_request = relationship("QualityProcedureDocumentRequest", back_populates="qp_request_history")




