from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from app.database import Base


#REQUEST
class QualityProcedureDocumentRequest(Base): 
    __tablename__ = "quality_procedure_document_request" #Temporary table name

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False) #May change to requested_by
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
    comment = Column(String(150), nullable=False) #might change to remarks
    comment_date = Column(TIMESTAMP, nullable=False) #Temporary Column Name

    quality_procedure_document_request = relationship("QualityProcedureDocumentRequest", back_populates="qp_request_history")

#DRRRF
class DRRRF(Base):
    __tablename__ = "drrrf" #Document Review Request and Registration Form

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_owner_id = Column(Integer, nullable=False)
    current_process_owner_id = Column(Integer, nullable=False) #will need to find a way to automate but currently this is manual
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
    slug = Column(String(100), nullable=False)
    registration_mark = Column(Text, nullable=True)
    registration_date = Column(DateTime, nullable=True)
    distribution_mark = Column(Text, nullable=True)
    distribution_date = Column(DateTime, nullable=True)
    date_created = Column(TIMESTAMP, nullable=False)

    #should add created_by

class InterfacingUnit(Base):
    __tablename__ = "intefacing_unit" #Interfacing Units to Review the Quality Procedure

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    signed = Column(Boolean, nullable=False) 
    signed_date = Column(DateTime, nullable=False)
    nominated_date = Column(TIMESTAMP, nullable=False)
   
class IUReviewSummary(Base):
    __tablename__ = "iu_review_summary" #Summary of Interfacing Units' review

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interfacing_unit_id = Column(Integer, nullable=False)
    review_summary = Column(String(200), nullable=False)
    reviewed_date = Column(TIMESTAMP, nullable=False)

class CurrentProcessOwner(Base): #Might change to process owner 
    __tablename__ = "current_process_owner"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False)
    date_created  = Column(DateTime, nullable=False) #DATE ACTED AS CURRENT PROCESS OWNER

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

#QUALITY PROCEDURES
class QPTitlePage(Base):
    __tablename__ = "qp_title_page"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    revision_type = Column(String(15), nullable=False)
    description_of_change = Column(String(200), nullable=False)
    page_affected = Column(String(10), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPObjective(Base):
    __tablename__ = "qp_objective"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    objective = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPScope(Base):
    __tablename__ = "qp_scope"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    scope = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPDefinitionOfTerm(Base):
    __tablename__ = "qp_definition_of_term"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    term = Column(String(80), nullable=False)
    definition = Column(Text, nullable=False)
    #slug
    date_created = Column(TIMESTAMP, nullable=False)

class QPReferenceDocument(Base):
    __tablename__ = "qp_reference_document"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    reference_document = Column(Text, nullable=False)
    file_path = Column(String(150), nullable=True)
    date_created = Column(TIMESTAMP, nullable=False)

class QPResponsbilityAndAuthority(Base):
    __tablename__ = "qp_responsibility_and_authority"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    authority = Column(String, nullable=False)
    responsibility = Column(Text, nullable=False)
    #slug
    date_created = Column(TIMESTAMP, nullable=False)

class QPProcedure(Base):
    __tablename__ = "qp_procedure"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    procedure = Column(Text, nullable=False)
    #slug
    date_created = Column(TIMESTAMP, nullable=False)

class QPProcess(Base):
    __tablename__ = "qp_process" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    procedure_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    process_title = Column(String(100), nullable=False)
    process_description = Column(Text, nullable=False) #WYSIWYG
    #slug
    date_created = Column(TIMESTAMP, nullable=False)

class QPProcessInCharge(Base):
    __tablename__ = "qp_process_in_charge"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False) 
    in_charge_id = Column(Integer, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPProcessNote(Base):
    __tablename__ = "qp_process_note"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    note = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPProcessRecord(Base):
    __tablename__ = "qp_process_record"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_id = Column(Integer, nullable=False)
    drrrf_id = Column(Integer, nullable=False)
    record = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPReport(Base):
    __tablename__ = "qp_report"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    report = Column(String(100), nullable=False)
    frequency = Column(String(150), nullable=False)
    in_charge = Column(String(70), nullable=False) #change to id to relate with responsiblity and authority
    date_created = Column(TIMESTAMP, nullable=False)

class QPPerformanceIndicator(Base):
    __tablename__ = "qp_performance_indicator"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    in_charge = Column(String(100), nullable=False)
    indicator = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

class QPAttachmentAndForm(Base):
    __tablename__ = "qp_attachments_and_form"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, nullable=False)
    record = Column(String(100), nullable=False)
    control_number = Column(String(100), nullable=True)
    maintenance = Column(Integer, nullable=True)
    preservation = Column(Integer, nullable=True)
    remarks = Column(String(50), nullable=True)
    file_path = Column(String(100), nullable=True)
    date_created = Column(TIMESTAMP, nullable=False)