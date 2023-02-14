from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


#REQUEST
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

#DRRRF
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

    #registration_mark = Column(Text, nullable=True)
    #registration_date = Column(DateTime, nullable=True)
    #distribution_mark = Column(Text, nullable=True)
    #distribution_date = Column(Text, nullable=True)
    #date_created = Column(TIMESTAMP, nullable=False)

class InterfacingUnit(Base):
    __tablename__ = "intefacing_unit" #Interfacing Units to Review the Quality Procedure

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    #signed = Column(Boolean, nullable=False) 
    #signed_date = Column(DateTime, nullable=False)
    nominated_date = Column(TIMESTAMP, nullable=False)
   
class IUReviewSummary(Base):
    __tablename__ = "iu_review_summary" #Summary of Interfacing Units' review

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interfacing_unit_id = Column(Integer, nullable=False)
    review_summary = Column(String(200), nullable=False)
    signed = Column(Boolean, nullable=False)
    reviewed_date = Column(TIMESTAMP, nullable=False)

class CurrentProcessOwner(Base):
    __tablename__ = "current_process_owner"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False)
    date_acted = Column(DateTime, nullable=False) #DATE ACTED AS CURRENT PROCESS OWNER

class QPSignatories(Base):
    __tablename__ = "qp_signatories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_owner_id = Column(Integer, nullable=False)
    iso_facilitator_id = Column(Integer, nullable=False)
    diso_facilitator_id = Column(Integer, nullable=False)
    head_of_office_id = Column(Integer, nullable=False)
    dcc_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)

class DRRRFSignatures(Base):
    __tablename__ = "drrrf_signatures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    process_owner_signed = Column(Boolean, nullable=False)
    process_owner_date_signed = Column(DateTime, nullable=True)
    head_of_office_initial_signed = Column(Boolean, nullable=False)
    head_of_office_initial_date_signed = Column(DateTime, nullable=True)
    iso_initial_review_signed = Column(Boolean, nullable=False)
    iso_initial_review_date_signed = Column(DateTime, nullable=False)
    head_of_office_approval_signed = Column(Boolean, nullable=False)
    head_of_office_approval_date_signed = Column(DateTime, nullable=False)
    diso_approval_signed = Column(Boolean, nullable=False)
    diso_approval_date_signed = Column(DateTime, nullable=False)
    dcc_signed = Column(Boolean, nullable=False)
    dcc_date_signed = Column(DateTime, nullable=False)
    iso_approval_signed = Column(Boolean, nullable=False)
    iso_approval_date_signed = Column(DateTime, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False) 

class QPSignatures(Base):
    __tablename__ = "qp_signatures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    process_owner_signed = Column(Boolean, nullable=False)
    process_owner_date_signed = Column(DateTime, nullable=True)
    head_of_office_approval_signed = Column(Boolean, nullable=False)
    head_of_office_approval_date_signed = Column(DateTime, nullable=False)
    diso_approval_signed = Column(Boolean, nullable=False)
    diso_approval_date_signed = Column(DateTime, nullable=False)
    iso_approval_signed = Column(Boolean, nullable=False)
    iso_approval_date_signed = Column(DateTime, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False) 

class LORSignatures(Base):
    __tablename__ = "lor_signatures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    process_owner_signed = Column(Boolean, nullable=False)
    process_owner_date_signed = Column(DateTime, nullable=True)
    head_of_office_approval_signed = Column(Boolean, nullable=False)
    head_of_office_approval_date_signed = Column(DateTime, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False) 

class QPStatus(Base):
    __tablename__ = "qp_status"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)
    action_id = Column(Integer, nullable=False)
    status_date = Column(TIMESTAMP, nullable=False)


