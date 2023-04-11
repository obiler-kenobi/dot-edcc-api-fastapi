from typing import Dict
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