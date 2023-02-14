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

class DRRRFCreate(DRRRFBase):
    process_owner_id: int
    #current_process_owner_id: int

class DRRRF(DRRRFBase):
    id: int

    class Config:
        orm_mode = True

#Interfacing Units
class InterfacingUnitBase(BaseModel):
    nominated_date: datetime
    user_id: int

class InterfacingUnitCreate(InterfacingUnitBase):
    drrrf_id: int

class InterfacingUnit(InterfacingUnitBase):
    id: int

    class Config: 
        orm_mode = True

#Interfacing Units Review Summary
class IUReviewSummaryBase(BaseModel): #IU = Interfacing Unit
    review_summary: str
    signed: bool = False
    reviewed_date: datetime

class IUReviewSummaryCreate(IUReviewSummaryBase):
    interfacing_unit_id: int

class IUReviewSummary(IUReviewSummaryBase):
    id: int

    class Config:
        orm_mode = True

#Quality Procedure
#Title Page
class TitlePageBase(BaseModel):
    revision_type: str
    description_of_change: str
    page_affected: str
    date_created: datetime

class TitlePageCreate(TitlePageBase):
    drrrf_id: int

class TitlePage(TitlePageBase):
    id: int

    class Config:
        orm_mode = True

class ObjectiveBase(BaseModel):
    objective: str
    date_created: datetime

class ObjectiveCreate(ObjectiveBase):
    drrrf_id: int

class Objective(ObjectiveBase):
    id: int

    class Config:
        orm_mode = True