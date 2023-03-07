from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.office.schemas import DOTMainOfficeLabel, DOTSectorLabel, DOTSubSectorLabel, DOTOfficeLabel,DOTDivisionLabel,DOTUnitLabel

class UserOfficeInformationBase(BaseModel):
    user_basic_information_id: int
    dot_main_office_id: int
    dot_sector_id: int
    dot_sub_sector_id: int
    dot_office_id: int
    dot_division_id: int
    date_created: datetime
    created_by: str

class UserOfficeInformationCreate(UserOfficeInformationBase):
    dot_unit_id: int

class UserOfficeInformation(UserOfficeInformationBase):
    id: int

    class Config:
        orm_mode = True

#CLASS FOR OFFICES NAME
class UserOffices(BaseModel):
    dot_main_office: DOTMainOfficeLabel
    dot_sector: DOTSectorLabel
    dot_sub_sector: DOTSubSectorLabel
    dot_office: DOTOfficeLabel
    dot_division: DOTDivisionLabel
    dot_unit: DOTUnitLabel

    class Config:
        orm_mode = True

class UserBasicInformationBase(BaseModel):
    first_name: str
    middle_initial: str
    last_name: str
    employee_id: int
    sex: str
    age: int
    contact_number: str
    alternate_contact_number: str
    alternate_email_address: str
    designation: int
    date_created: datetime
    created_by: str

class UserBasicInformationCreate(UserBasicInformationBase):
    user_id: int

class UserBasicInformation(UserBasicInformationCreate):
    id: int
    user_office_information: List[UserOffices] = []

    class Config:
        orm_mode = True

class UserInformation(BaseModel):
    first_name: str
    middle_initial: str
    last_name: str
    designation: int


class UserBase(BaseModel):
    username: str
    hashed_password: str = "DOTedcc@2022"
    primary_email_address: str
    active: bool = True
    date_created: datetime
    created_by: str

class UserCreate(UserBase):
    role_id: int

class User(UserBase):
    id: int
    user_basic_information: List[UserBasicInformation] = []

    class Config:
        orm_mode = True

class UserInformationSample(BaseModel):
    user_basic_information: List[UserBasicInformation] = []

    class Config:
        orm_mode = True

class ProcessOwner(BaseModel):
    id: int
    role_id: int
    user_basic_information: List[UserInformation] = []

    class Config:
        orm_mode = True



    