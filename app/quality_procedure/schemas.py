from typing import List
from datetime import datetime
from pydantic import BaseModel

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

class QualityProcedureDocumentRequestCreate(QualityProcedureDocumentRequestBase):
    user_id: int
    status_id: int
    action_id: int

class QualityProcedureDocumentRequest(QualityProcedureDocumentRequestBase):
    id: int
    qp_request_history: List[QPRequestHistory] = []

    class Config:
        orm_mode = True

#DRRRF
class DRRRFBase(BaseModel):
    received_date: datetime
    execution_date: datetime = "0001-01-01T00:00:00.00Z"
    document_number: str
    document_title: str
    document_type: str = "Quality Procedure"
    revision_number: int
    page_number: int
    purpose: str
    iso_remarks: str
    dcc_remarks: str
    slug: str
    registration_mark: str
    registration_date: datetime = "0001-01-01T00:00:00.00Z"
    distribution_mark: str
    distribution_date: datetime = "0001-01-01T00:00:00.00Z"
    date_created: datetime

class DRRRFCreate(DRRRFBase):
    process_owner_id: int
    current_process_owner_id: int

class DRRRF(DRRRFBase):
    id: int

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
    drrrf_id: int

class QPTitlePage(QPTitlePageBase):
    id: int

    class Config:
        orm_mode = True

#OBJECTIVE
class QPObjectiveBase(BaseModel):
    objective: str
    date_created: datetime

class QPObjectiveCreate(QPObjectiveBase):
    drrrf_id: int

class QPObjective(QPObjectiveBase):
    id: int

    class Config:
        orm_mode = True

#SCOPE
class QPScopeBase(BaseModel):
    scope: str
    date_created: datetime

class QPScopeCreate(QPScopeBase):
    drrrf_id: int

class QPScope(QPScopeBase):
    id: int

    class Config:
        orm_mode = True

#DEFINITION OF TERMS
class QPDefinitionOfTermBase(BaseModel):
    term: str
    definition: str
    date_created: datetime

class QPDefinitionOfTermCreate(QPDefinitionOfTermBase):
    drrrf_id: int

class QPDefinitionOfTerm(QPDefinitionOfTermBase):
    id: int

    class Config:
        orm_mode = True

#REFERENCE DOCUMENTS
class QPReferenceDocumentBase(BaseModel):
    reference_document: str
    file_path: str
    date_created: datetime

class QPReferenceDocumentCreate(QPReferenceDocumentBase):
    drrrf_id: int

class QPReferenceDocument(QPReferenceDocumentBase):
    id: int

    class Config:
        orm_mode = True

#RESPONSIBILITY AND AUTHORITY
class QPResponsiblityAndAuthorityBase(BaseModel):
    authority: str
    responsibility: str
    date_created: datetime

class QPResponsiblityAndAuthorityCreate(QPResponsiblityAndAuthorityBase):
    drrrf_id: int

class QPResponsiblityAndAuthority(QPResponsiblityAndAuthorityBase):
    id: int

    class Config:
        orm_mode = True

#PROCEDURE
class QPProcedureBase(BaseModel):
    procedure: str
    date_created: datetime

class QPProcedureCreate(QPProcedureBase):
    drrrf_id: int

class QPProcedure(QPProcedureBase):
    id: int

    class Config:
        orm_mode = True

#PROCESS
class QPProcessBase(BaseModel):
    process_title: str
    process_description: str
    date_created: datetime

class QPProcessCreate(QPProcessBase):
    drrrf_id: int
    procedure_id: int

class QPProcess(QPProcessBase):
    id: int

    class Config:
        orm_mode = True

#PROCESS IN CHARGE
class QPProcessInChargeBase(BaseModel):
    date_created: datetime

class QPProcessInChargeCreate(QPProcessInChargeBase):
    in_charge_id: int
    process_id: int
    drrrf_id: int

class QPProcessInCharge(QPProcessInChargeBase):
    id: int

    class Config:
        orm_mode = True

#PROCESS NOTES
class QPProcessNoteBase(BaseModel):
    note: str
    date_created: datetime

class QPProcessNoteCreate(QPProcessNoteBase):
    process_id: int
    drrrf_id: int

class QPProcessNote(QPProcessNoteBase):
    id: int

    class Config:
        orm_mode = True

#PROCESS RECORD
class QPProcessRecordBase(BaseModel):
    record: str
    date_created: datetime

class QPProcessRecordCreate(QPProcessRecordBase):
    process_id: int
    drrrf_id: int

class QPProcessRecord(QPProcessRecordBase):
    id: int

    class Config:
        orm_mode = True

#REPORT
class QPReportBase(BaseModel):
    report: str
    frequency: str
    in_charge: str
    date_created: datetime

class QPReportCreate(QPReportBase):
    drrrf_id: int

class QPReport(QPReportBase):
    id: int

    class Config:
        orm_mode = True

#PERFORMANCE INDICATOR
class QPPerformanceIndicatorBase(BaseModel):
    in_charge: str
    indicator: str
    date_created: datetime

class QPPerformanceIndicatorCreate(QPPerformanceIndicatorBase):
    drrrf_id: int

class QPPerformanceIndicator(QPPerformanceIndicatorBase):
    id: int

    class Config:
        orm_mode = True

#ATTACHMENT AND FORM
class QPAttachmentAndFormBase(BaseModel):
    record: str
    control_number: str
    maintenance: int
    preservation: int
    remarks: str
    file_path: str
    date_created: datetime

class QPAttachmentAndFormCreate(QPAttachmentAndFormBase):
    drrrf_id: int

class QPAttachmentAndForm(QPAttachmentAndFormBase):
    id: int

    class Config:
        orm_mode = True