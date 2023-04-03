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