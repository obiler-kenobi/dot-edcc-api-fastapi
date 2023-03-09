from typing import List
from datetime import datetime
from pydantic import BaseModel

from app.user.schemas import ProcessOwner


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
    objective: str
    date_created: datetime

class QPObjectiveCreate(QPObjectiveBase):
    pass

class QPObjective(QPObjectiveBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#SCOPE
class QPScopeBase(BaseModel):
    scope: str
    date_created: datetime

class QPScopeCreate(QPScopeBase):
    pass

class QPScope(QPScopeBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#DEFINITION OF TERMS
class QPDefinitionOfTermBase(BaseModel):
    term: str
    definition: str
    date_created: datetime

class QPDefinitionOfTermCreate(QPDefinitionOfTermBase):
    pass

class QPDefinitionOfTerm(QPDefinitionOfTermBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#REFERENCE DOCUMENTS
class QPReferenceDocumentBase(BaseModel):
    reference_document: str
    file_path: str
    date_created: datetime

class QPReferenceDocumentCreate(QPReferenceDocumentBase):
    pass

class QPReferenceDocument(QPReferenceDocumentBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#RESPONSIBILITY AND AUTHORITY
class QPResponsiblityAndAuthorityBase(BaseModel):
    authority: str
    responsibility: str
    date_created: datetime

class QPResponsiblityAndAuthorityCreate(QPResponsiblityAndAuthorityBase):
    pass

class QPResponsiblityAndAuthority(QPResponsiblityAndAuthorityBase):
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

#PROCESS RECORD
class QPProcessRecordBase(BaseModel):
    record: str
    date_created: datetime

class QPProcessRecordCreate(QPProcessRecordBase):
    pass

class QPProcessRecord(QPProcessRecordBase):
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

#PERFORMANCE INDICATOR
class QPPerformanceIndicatorBase(BaseModel):
    in_charge: str
    indicator: str
    date_created: datetime

class QPPerformanceIndicatorCreate(QPPerformanceIndicatorBase):
    pass

class QPPerformanceIndicator(QPPerformanceIndicatorBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True

#ATTACHMENT AND FORM
class QPAttachmentAndFormBase(BaseModel):
    record: str
    #control_number: str omitted, will be available on LOR
    #maintenance: int omitted, will be available on LOR
    #preservation: int omitted, will be available on LOR
    #remarks: str omitted, will be available on LOR
    #file_path: str omitted, will be available on LOR
    #include_in_lor: bool omitted, will be available on 9.0
    date_created: datetime

class QPAttachmentAndFormCreate(QPAttachmentAndFormBase):
    pass

class QPAttachmentAndForm(QPAttachmentAndFormBase):
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
    

#PROCESS IN CHARGE
class QPProcessInChargeBase(BaseModel):
    date_created: datetime

class QPProcessInChargeCreate(QPProcessInChargeBase):
    in_charge_id: int

class QPProcessInCharge(QPProcessInChargeBase):
    id: int 
    process_id: int
    drrrf_id: int
    qp_responsibility_and_authority: QPResponsiblityAndAuthority = []

    class Config:
        orm_mode = True

#PROCESS
class QPProcessBase(BaseModel):
    process_title: str
    process_description: str
    date_created: datetime

class QPProcessCreate(QPProcessBase):
    pass

class QPProcess(QPProcessBase):
    id: int
    drrrf_id: int
    procedure_id: int
    qp_process_in_charge: List[QPProcessInCharge] = []
    qp_process_record: List[QPProcessRecord] = []

    class Config:
        orm_mode = True

#PROCEDURE
class QPProcedureBase(BaseModel):
    procedure: str
    date_created: datetime

class QPProcedureCreate(QPProcedureBase):
    pass

class QPProcedure(QPProcedureBase):
    id: int
    drrrf_id: int
    qp_process: List[QPProcess] = []

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

