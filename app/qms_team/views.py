from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.qms_team.schemas import ISOFacilitator, ISOFacilitatorCreate, DISOFacilitator, DISOFacilitatorCreate, HeadOfOffice, HeadOfOfficeCreate
from app.qms_team.services import ISOFacilitatorManager, DISOFacilitatorManager, HeadOfOfficeManager
from app.deps import get_db

qms_team_router = APIRouter()

#GET ALL ISO FACILITATORS
@qms_team_router.get(
    "/iso-facilitators",
    response_model=List[ISOFacilitator],
    status_code=status.HTTP_200_OK
)
def get_all_iso_facilitators(db: Session = Depends(get_db)):
    return ISOFacilitatorManager.get_all_iso_facilitators(db)

#CREATE ISO FACILITATOR
@qms_team_router.post(
    "/iso-facilitators",
    response_model=ISOFacilitator,
    status_code=status.HTTP_201_CREATED
)
def create_iso_facilitator(iso_facilitator: ISOFacilitatorCreate, db: Session = Depends(get_db)):
    return ISOFacilitatorManager.create_iso_facilitator(db, iso_facilitator)

#GET ALL DISO FACILITATORS
@qms_team_router.get(
    "/diso-facilitators",
    response_model=List[DISOFacilitator],
    status_code=status.HTTP_200_OK
)
def get_all_diso_facilitators(db: Session = Depends(get_db)):
    return DISOFacilitatorManager.get_all_diso_facilitators(db)

#CREATE DISO FACILITATOR
@qms_team_router.post(
    "/diso-facilitators",
    response_model=DISOFacilitator,
    status_code=status.HTTP_201_CREATED
)
def create_diso_facilitator(diso_facilitator: DISOFacilitatorCreate, db: Session = Depends(get_db)):
    return DISOFacilitatorManager.create_diso_facilitator(db, diso_facilitator)

#GET ALL HEAD OF OFFICE
@qms_team_router.get(
    "/head-of-office",
    response_model=List[HeadOfOffice],
    status_code=status.HTTP_200_OK
)
def get_all_head_of_office(db: Session = Depends(get_db)):
    return HeadOfOfficeManager.get_all_head_of_office(db)

#CREATE DISO FACILITATOR
@qms_team_router.post(
    "/head-of-office",
    response_model=HeadOfOffice,
    status_code=status.HTTP_201_CREATED
)
def create_head_of_office(head_of_office: HeadOfOfficeCreate, db: Session = Depends(get_db)):
    return HeadOfOfficeManager.create_head_of_office(db, head_of_office )