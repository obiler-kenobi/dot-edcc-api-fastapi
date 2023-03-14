from typing import List
from datetime import date,datetime
from pydantic import BaseModel

from app.user.schemas import ProcessOwner, PersonResponsible
from app.quality_procedure.status.schemas import StatusDescription, StatusAction

class QualityProcedureRequestBase(BaseModel):  
    quality_procedure_id: int
    request_type: str 
    document_title: str
    document_number: str
    request_purpose: str
    revision_type: str
    revision_number: int
    date_created: datetime
    date_updated: datetime

class QualityProcedureRequestCreate(QualityProcedureRequestBase):
    requested_by: int
    status_id: int
    status_actions_id: int

class QualityProcedureRequest(QualityProcedureRequestBase):
    id: int
    user: ProcessOwner = []
    status: StatusDescription = []
    status_actions: StatusAction = []

    class Config:
        orm_mode = True

class QualityProcedureStatusUpdate(BaseModel):
    status_id: int
    status_actions_id: int

    class Config:
        orm_mode = True

class QualityProcedureRequestHistoryBase(BaseModel):
    remarks: str
    date_created: date
    time_created: datetime

class QualityProcedureRequestHistoryCreate(QualityProcedureRequestHistoryBase):
    user_id: int
    status_id: int
    status_actions_id: int

class QualityProcedureRequestHistory(QualityProcedureRequestHistoryBase):
    id: int
    request_id: int
    status: StatusDescription = []
    status_actions: StatusAction = []
    user: PersonResponsible = []

    class Config:
        orm_mode = True
    