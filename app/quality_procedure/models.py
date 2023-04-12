from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.database import Base


#REQUEST
class QualityProcedureDocumentRequest(Base): 
    __tablename__ = "quality_procedure_document_request" #Temporary table name

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False) #May change to requested_by
    current_qp_id = Column(Integer, nullable=False)
    request_date = Column(TIMESTAMP, nullable=False)
    request_purpose = Column(String(150), nullable=False)
    request_type = Column(String(10), nullable=False)
    document_title = Column(String(150), nullable=False)
    document_number = Column(String(100), nullable=True) #might remove
    revision_number = Column(Integer, nullable=False)
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
    process_owner_id = Column(Integer, ForeignKey("user.id"))
    current_process_owner_id = Column(Integer, nullable=False) #will need to find a way to automate but currently this is manual
    previous_qp_id = Column(Integer, nullable=False)
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
    created_by = Column(String(15), nullable=False)
    drrrf_status = Column(String(15), nullable=False)

    user = relationship("User", back_populates="drrrf")
    qp_objective = relationship("QPObjective", back_populates="drrrf")
    qp_scope = relationship("QPScope", back_populates="drrrf")
    qp_definition_of_term = relationship("QPDefinitionOfTerm", back_populates="drrrf")
    qp_reference_document = relationship("QPReferenceDocument", back_populates="drrrf")
    qp_responsibility_and_authority = relationship("QPResponsbilityAndAuthority", back_populates="drrrf")
    qp_procedure = relationship("QPProcedure", back_populates="drrrf")
    qp_report = relationship("QPReport", back_populates="drrrf")
    qp_performance_indicator = relationship("QPPerformanceIndicator", back_populates="drrrf")
    qp_process = relationship("QPProcess", back_populates="drrrf")
    qp_process_in_charge = relationship("QPProcessInCharge", back_populates="drrrf")
    qp_process_record = relationship("QPProcessRecord", back_populates="drrrf")
    qp_attachments_and_form = relationship("QPAttachmentAndForm", back_populates="drrrf")
    qp_distribution_list = relationship("QPDistributionList", back_populates="drrrf")

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
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    objective = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_objective")

class QPProcessInCharge(Base):
    __tablename__ = "qp_process_in_charge"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    process_id = Column(Integer, ForeignKey("qp_process.id"))
    drrrf_id = Column(Integer, ForeignKey("drrrf.id")) 
    in_charge_id = Column(Integer, ForeignKey("qp_responsibility_and_authority.id"))
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_process_in_charge")
    qp_process = relationship("QPProcess", back_populates="qp_process_in_charge")
    qp_responsibility_and_authority = relationship("QPResponsbilityAndAuthority", back_populates="qp_process_in_charge")

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
    process_id = Column(Integer, ForeignKey("qp_process.id"))
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    record = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    qp_process = relationship("QPProcess", back_populates="qp_process_record")
    drrrf = relationship("DRRRF", back_populates="qp_process_record")

class QPReport(Base):
    __tablename__ = "qp_report"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    report = Column(String(100), nullable=False)
    frequency = Column(String(150), nullable=False)
    in_charge = Column(String(70), nullable=False) #change to id to relate with responsiblity and authority
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_report")

class QPPerformanceIndicator(Base):
    __tablename__ = "qp_performance_indicator"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    in_charge = Column(String(100), nullable=False)
    indicator = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    
    drrrf = relationship("DRRRF", back_populates="qp_performance_indicator")

class QPAttachmentAndForm(Base):
    __tablename__ = "qp_attachments_and_form"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    record = Column(String(100), nullable=False)
    control_number = Column(String(100), nullable=True)
    maintenance = Column(Integer, nullable=True)
    preservation = Column(Integer, nullable=True)
    remarks = Column(String(50), nullable=True)
    file_path = Column(String(100), nullable=True)
    date_created = Column(TIMESTAMP, nullable=False) 
    #include_in_lor boolean

    drrrf = relationship("DRRRF", back_populates="qp_attachments_and_form")


class QPDistributionList(Base):
    __tablename__ = "qp_distribution_list"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    interfacing_unit_id = Column(Integer, ForeignKey("user.id"))
    created_by = Column(String(100), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_distribution_list")
    user = relationship("User", back_populates="qp_distribution_list")
    