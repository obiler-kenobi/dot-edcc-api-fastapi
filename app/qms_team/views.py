from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.qms_team.schemas import ISOFacilitator, ISOFacilitatorCreate
from app.qms_team.services import ISOFaciliatorManager
from app.deps import get_db

qms_team_router = APIRouter()

#GET ALL ISO FACILITATORS
@qms_team_router.get(
    "/iso-facilitators",
    response_model=List[ISOFacilitator],
    status_code=status.HTTP_200_OK
)
def get_all_iso_facilitators(db: Session = Depends(get_db)):
    return ISOFaciliatorManager.get_all_iso_facilitators(db)

#CREATE ISO FACILITATOR
@qms_team_router.post(
    "/iso-facilitators",
    response_model=ISOFacilitator,
    status_code=status.HTTP_201_CREATED
)
def create_iso_facilitator(iso_facilitator: ISOFacilitatorCreate, db: Session = Depends(get_db)):
    return ISOFaciliatorManager.create_iso_facilitator(db, iso_facilitator)