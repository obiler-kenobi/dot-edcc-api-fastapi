from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime
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
    document_number = Column(String(100), nullable=True) #might remove
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

class DRRRF(Base):
    __tablename__ = "drrrf" #Document Review Request and Registration Form

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_owner_id = Column(Integer, nullable=False)
    #current_process_owner_id = Column(Integer, nullable=False)
    received_date = Column(TIMESTAMP, nullable=False)
    execution_date = Column(DateTime, nullable=True)
    document_number = Column(String(100), nullable=True)
    document_title = Column(String(100), nullable=False)
    document_type = Column(String(30), nullable=False)
    revision_number = Column(Integer, nullable=False)
    page_number = Column(Integer,nullable=False)
    purpose = Column(String(150), nullable=False)
    iso_remarks = Column(String(100), nullable=True)
    dcc_remarks = Column(String(100), nullable=True)

class InterfacingUnit(Base):
    __tablename__ = "intefacing_unit" #Interfacing Units to Review the Quality Procedure

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    nominated_date = Column(TIMESTAMP, nullable=False)

    
class IUReviewSummary(Base):
    __tablename__ = "iu_review_summary" #Summary of Interfacing Units' review

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interfacing_unit_id = Column(Integer, nullable=False)
    review_summary = Column(String(200), nullable=False)
    signed = Column(Boolean, nullable=False)
    reviewed_date = Column(TIMESTAMP, nullable=False)



