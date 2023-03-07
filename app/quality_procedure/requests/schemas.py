from typing import List
from datetime import datetime
from pydantic import BaseModel

class QualityProcedureRequestBase(BaseModel):  
    quality_procedure_id: int
    request_type: str 
    document_title: str
    document_number: str
    request_purpose: str
    revision_type: str
    revision_number: str
    date_created: datetime
    date_updated: datetime

class QualityProcedureRequestCreate(QualityProcedureRequestBase):
    requested_by: int
    status_id: int
    status_actions_id: int

class QualityProcedureRequest(QualityProcedureRequestBase):
    id: int

    class Config:
        orm_mode = True