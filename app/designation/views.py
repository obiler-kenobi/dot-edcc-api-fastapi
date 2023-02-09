from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.designation.schemas import Designation, DesignationCreate
from app.designation.services import DesignationManager
from app.deps import get_db

designation_router = APIRouter()

#GET ALL DESIGNATIONS
@designation_router.get(
    "/designations",
    response_model=List[Designation],
    status_code=status.HTTP_200_OK
)
def get_all_designations(db: Session = Depends(get_db)):
    return DesignationManager.get_all_designations(db)

#CREATE NEW DESIGNATION
@designation_router.post(
    "/designations",
    response_model=Designation,
    status_code=status.HTTP_201_CREATED
)
def create_designation(designation: DesignationCreate, db: Session = Depends(get_db)):
    return DesignationManager.create_designation(db, designation)


