from datetime import datetime
from pydantic import BaseModel

class DesignationBase(BaseModel):
    designation_title: str
    designation_abbreviation: str
    date_encoded: datetime
    encoded_by: str

class DesignationCreate(DesignationBase):
    pass

class Designation(DesignationBase):
    id: int

    class Config:
        orm_mode = True