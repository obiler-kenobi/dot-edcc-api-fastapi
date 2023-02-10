from typing import List
from datetime import datetime
from pydantic import BaseModel

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

