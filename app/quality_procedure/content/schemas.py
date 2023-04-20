from typing import Dict, List
from datetime import datetime
from pydantic import BaseModel

#SCOPE
class QPScopeBase(BaseModel):
    scope: Dict[str, dict | str | list]
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
    definition: Dict[str, dict | str | list]
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
    responsibility: Dict[str, dict | str | list]
    date_created: datetime

class QPResponsiblityAndAuthorityCreate(QPResponsiblityAndAuthorityBase):
    pass

class QPResponsiblityAndAuthority(QPResponsiblityAndAuthorityBase):
    id: int
    drrrf_id: int

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

#PROCESS
class QPProcessBase(BaseModel):
    process_title: str
    process_description: Dict[str, dict | str | list]
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
    qp_process: list[QPProcess] = []

    class Config:
        orm_mode = True

#ATTACHMENT AND FORM
class QPAttachmentAndFormBase(BaseModel):
    record: str
    date_created: datetime

class LORUpdate(BaseModel):
    control_number: str
    maintenance: int
    preservation: int
    remarks: str
    file_path: str

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
    
class QPAttachmentAndFormCreateUpdate(BaseModel):
    include_in_lor: bool

class QPAttachmentAndFormCreate(QPAttachmentAndFormBase):
    pass

class QPAttachmentAndForm(QPAttachmentAndFormBase):
    id: int
    drrrf_id: int

    class Config:
        orm_mode = True