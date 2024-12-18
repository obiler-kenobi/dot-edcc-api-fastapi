from typing import List, Dict
from datetime import datetime
from pydantic import BaseModel

from app.user.schemas import ProcessOwner
from app.quality_procedure.content.schemas import QPScope, QPDefinitionOfTerm, QPReferenceDocument, QPResponsiblityAndAuthority, QPProcedure, QPAttachmentAndForm, QPPerformanceIndicator

#QUALITY PROCEDURE REQUEST
class QPRequestHistoryBase(BaseModel):
    comment: str
    comment_date: datetime
    request_id: int
    
class QPRequestHistoryCreate(QPRequestHistoryBase):
    user_id: int
    
class QPRequestHistory(QPRequestHistoryBase):
    id: int

    class Config:
        orm_mode = True

class QualityProcedureDocumentRequestBase(BaseModel): 
    request_date: datetime
    request_purpose: str
    request_type: str 
    document_title: str
    document_number: str
    revision_number: str
    current_qp_id: int

class QualityProcedureDocumentRequestCreate(QualityProcedureDocumentRequestBase):
    user_id: int
    status_id: int
    action_id: int

class QualityProcedureDocumentRequest(QualityProcedureDocumentRequestBase):
    id: int
    status_id: int
    action_id: int
    qp_request_history: List[QPRequestHistory] = []

    class Config:
        orm_mode = True

class QualityProcedureDocumentRequestStatusUpdate(BaseModel):
    status_id: int
    action_id: int
    
    class Config:
        orm_mode = True

#INTERFACING UNITS
class InterfacingUnitBase(BaseModel):
    signed: bool = False
    signed_date: datetime = "0001-01-01T00:00:00.00Z"
    nominated_date: datetime
    
class InterfacingUnitCreate(InterfacingUnitBase):
    drrrf_id: int
    user_id: int

class InterfacingUnit(InterfacingUnitBase):
    id: int

    class Config: 
        orm_mode = True

#INTERFACING UNITS REVIEW SUMMARY
class IUReviewSummaryBase(BaseModel): #IU = Interfacing Unit
    review_summary: str
    reviewed_date: datetime

class IUReviewSummaryCreate(IUReviewSummaryBase):
    interfacing_unit_id: int

class IUReviewSummary(IUReviewSummaryBase):
    id: int

    class Config:
        orm_mode = True

#QUALITY PROCEDURE
##TITLE PAGE
class QPTitlePageBase(BaseModel):
    revision_type: str
    description_of_change: str
    page_affected: str
    date_created: datetime

class QPTitlePageCreate(QPTitlePageBase):
    pass

class QPTitlePage(QPTitlePageBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#OBJECTIVE
class QPObjectiveBase(BaseModel):
    objective: Dict[str, dict | str | list]
    date_created: datetime

class QPObjectiveCreate(QPObjectiveBase):
    pass

class QPObjective(QPObjectiveBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#PROCESS NOTES
class QPProcessNoteBase(BaseModel):
    note: str
    date_created: datetime

class QPProcessNoteCreate(QPProcessNoteBase):
    pass

class QPProcessNote(QPProcessNoteBase):
    id: int
    process_id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#REPORT
class QPReportBase(BaseModel):
    report: str
    frequency: str
    in_charge: str #might change in in_charge_id
    date_created: datetime

class QPReportCreate(QPReportBase):
    pass

class QPReport(QPReportBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

class StatusBase(BaseModel):
    status: str
    status_placement: int
    created_by: str
    date_created: datetime

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True
    
#DRRRF
class RegisteredDRRRFBase(BaseModel):
    received_date: datetime
    execution_date: datetime
    document_number: str
    document_title: str
    document_type: str = "Quality Procedure"
    previous_qp_id: int
    revision_number: int
    page_number: int
    purpose: str
    #iso_remarks: str omitted, will include in "update" of drrrf
    #dcc_remarks: str omitted, will include in "update" of drrrf
    slug: str
    #registration_mark: str
    registration_date: datetime
    #distribution_mark: str
    distribution_date: datetime
    date_created: datetime
    created_by: str
    drrrf_status: str

class DRRRFBase(BaseModel):
    received_date: datetime
    #execution_date: datetime = "0001-01-01T00:00:00.00Z" omitted, will include in "update" of drrrf
    document_number: str
    document_title: str
    document_type: str = "Quality Procedure"
    previous_qp_id: int
    revision_number: int
    page_number: int
    purpose: str
    #iso_remarks: str omitted, will include in "update" of drrrf
    #dcc_remarks: str omitted, will include in "update" of drrrf
    slug: str
    #registration_mark: str
    #registration_date: datetime = "0001-01-01T00:00:00.00Z" omitted, will include in "update" of drrrf
    #distribution_mark: str
    #distribution_date: datetime = "0001-01-01T00:00:00.00Z" omitted, will include in "update" of drrrf
    date_created: datetime
    created_by: str
    drrrf_status: str

class DRRRFCreate(DRRRFBase):
    process_owner_id: int
    current_process_owner_id: int

class DRRRF(DRRRFBase):
    id: int
    user: ProcessOwner = []
    qp_objective: List[QPObjective] = []
    qp_scope: List[QPScope] = []
    qp_definition_of_term: List[QPDefinitionOfTerm] = []
    qp_reference_document: List[QPReferenceDocument] = []
    qp_responsibility_and_authority: List[QPResponsiblityAndAuthority] = []
    qp_procedure: List[QPProcedure] = []
    qp_report: List[QPReport] = []
    qp_performance_indicator: List[QPPerformanceIndicator] = []
    qp_attachments_and_form: List[QPAttachmentAndForm] = []

    class Config:
        orm_mode = True

class DRRRF(DRRRFBase):
    id: int
    user: ProcessOwner = []
    qp_objective: List[QPObjective] = []
    qp_scope: List[QPScope] = []
    qp_definition_of_term: List[QPDefinitionOfTerm] = []
    qp_reference_document: List[QPReferenceDocument] = []
    qp_responsibility_and_authority: List[QPResponsiblityAndAuthority] = []
    qp_procedure: List[QPProcedure] = []
    qp_report: List[QPReport] = []
    qp_performance_indicator: List[QPPerformanceIndicator] = []
    qp_attachments_and_form: List[QPAttachmentAndForm] = []

    class Config:
        orm_mode = True

class RegisteredDRRRF(RegisteredDRRRFBase):
    id: int
    user: ProcessOwner = []
    qp_objective: List[QPObjective] = []
    qp_scope: List[QPScope] = []
    qp_definition_of_term: List[QPDefinitionOfTerm] = []
    qp_reference_document: List[QPReferenceDocument] = []
    qp_responsibility_and_authority: List[QPResponsiblityAndAuthority] = []
    qp_procedure: List[QPProcedure] = []
    qp_report: List[QPReport] = []
    qp_performance_indicator: List[QPPerformanceIndicator] = []
    qp_attachments_and_form: List[QPAttachmentAndForm] = []

    class Config:
        orm_mode = True

class DRRRFStatusUpdate(BaseModel):
    drrrf_status: str

    class Config:
        orm_mode = True

class DRRRFDistributeUpdate(BaseModel):
    drrrf_status: str
    execution_date: datetime
    distribution_date: datetime

    class Config:
        orm_mode = True

#DISTRIBUTION LIST
class DistributionListBase(BaseModel):
    created_by: str
    date_created: datetime

class DistributionListCreate(DistributionListBase):
    interfacing_unit_id: int
    drrrf_id: int

class DistributionList(DistributionListCreate):
    id: int

    class Config:
        orm_mode = True

