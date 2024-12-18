from typing import List
from datetime import datetime
from pydantic import BaseModel

class StatusBase(BaseModel):
    status: str
    status_description: str
    status_placement: int
    created_by: str
    date_created: datetime
    date_updated: datetime

class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True

class StatusDescription(BaseModel):
    id: int
    status_description: str

    class Config:
        orm_mode = True

class StatusActionsBase(BaseModel):
    action: str
    action_description: str
    created_by: str
    date_created: datetime
    date_updated: datetime

class StatusActions(StatusActionsBase):
    id: int

    class Config:
        orm_mode = True

class StatusAction(BaseModel):
    id: int
    action: str
    action_color: str

    class Config:
        orm_mode = True
