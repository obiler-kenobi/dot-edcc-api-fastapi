from typing import List
from datetime import datetime
from pydantic import BaseModel

#ISO Facilitator
class ISOFacilitatorBase(BaseModel):
    active: bool = True
    date_encoded: datetime

class ISOFacilitatorCreate(ISOFacilitatorBase):
    user_id: int

class ISOFacilitator(ISOFacilitatorBase):
    id: int

    class Config:
        orm_mode = True

#Deputy ISO Facilitator
class DISOFacilitatorBase(BaseModel):
    office_handled: int
    active: bool = True
    date_encoded: datetime

class DISOFacilitatorCreate(DISOFacilitatorBase):
    user_id: int

class DISOFacilitator(DISOFacilitatorBase):
    id: int

    class Config:
        orm_mode = True

#Head of Office
class HeadOfOfficeBase(BaseModel):
    office_handled: int
    active: bool = True
    date_encoded: datetime

class HeadOfOfficeCreate(HeadOfOfficeBase):
    user_id: int

class HeadOfOffice(HeadOfOfficeBase):
    id: int

    class Config:
        orm_mode = True