from datetime import datetime
from typing import Union
from pydantic import BaseModel

#MAIN OFFICE CLASSES
class DOTMainOfficeBase(BaseModel):
    main_office_name: str
    short_main_office_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTMainOfficeCreate(DOTMainOfficeBase):
    pass

class DOTMainOffice(DOTMainOfficeBase):
    id: int

    class Config:
        orm_mode = True

class DOTSectorBase(BaseModel):
    sector_name: str
    short_sector_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTSectorCreate(DOTSectorBase):
    dot_main_office_id = 1

class DOTSector(DOTSectorBase):
    id: int

    class Config:
        orm_mode = True

class DOTSubSectorBase(BaseModel):
    sub_sector_name: str
    short_sub_sector_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTSubSectorCreate(DOTSubSectorBase):
    dot_sector_id: int

class DOTSubSector(DOTSubSectorBase):
    id: int

    class Config:
        orm_mode = True

class DOTOfficeBase(BaseModel):
    office_name: str
    short_office_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTOfficeCreate(DOTOfficeBase):
    dot_main_office_id = 0
    dot_sector_id = 0
    dot_sub_sector_id = 0

class DOTOffice(DOTOfficeBase):
    id: int

    class Config:
        orm_mode = True

class DOTDivisionBase(BaseModel):
    division_name: str
    short_division_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTDivisionCreate(DOTDivisionBase):
    dot_office_id: int

class DOTDivision(DOTDivisionBase):
    id: int

    class Config:
        orm_mode = True

class DOTUnitBase(BaseModel):
    unit_name: str
    short_unit_name: str
    slug: str
    date_encoded: datetime
    encoded_by: str

class DOTUnitCreate(DOTUnitBase):
    dot_main_office_id: int
    dot_sector_id: int
    dot_sub_sector_id: int
    dot_office_id: int
    dot_division_id: int

class DOTUnit(DOTUnitBase):
    id: int

    class Config:
        orm_mode = True

#CLASS FOR LABEL PURPOSES
class DOTMainOfficeLabel(BaseModel):
    main_office_name: str
    short_main_office_name: str

    class Config:
        orm_mode = True

class DOTSectorLabel(BaseModel):
    sector_name: str
    short_sector_name: str

    class Config:
        orm_mode = True

class DOTSubSectorLabel(BaseModel):
    sub_sector_name: str
    short_sub_sector_name: str

    class Config:
        orm_mode = True

class DOTOfficeLabel(BaseModel):
    office_name: str
    short_office_name: str

    class Config:
        orm_mode = True

class DOTDivisionLabel(BaseModel):
    division_name: str
    short_division_name: str

    class Config:
        orm_mode = True

class DOTUnitLabel(BaseModel):
    unit_name: str
    short_unit_name: str

    class Config:
        orm_mode = True