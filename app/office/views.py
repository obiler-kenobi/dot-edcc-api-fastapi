from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.office.schemas import DOTMainOffice, DOTMainOfficeCreate, DOTSector, DOTSectorCreate, DOTSubSector, DOTSubSectorCreate, DOTOffice, DOTOfficeCreate, DOTDivision, DOTDivisionCreate, DOTUnit, DOTUnitCreate
from app.office.services import DOTMainOfficeManager, DOTSectorManager, DOTSubSectorManager, DOTOfficeManager, DOTDivisionManager, DOTUnitManager
from app.deps import get_db

office_router = APIRouter()

#Get All Main Offices
@office_router.get(
    "/main-offices",
    response_model=List[DOTMainOffice],
    status_code=status.HTTP_200_OK
)
def get_all_main_offices(db: Session = Depends(get_db)):
    return DOTMainOfficeManager.get_all_main_offices(db)

#Main Office Create
@office_router.post(
    "/main-offices",
    response_model=DOTMainOffice,
    status_code=status.HTTP_201_CREATED
)
def create_main_office(main_office: DOTMainOfficeCreate, db: Session = Depends(get_db)):
    return DOTMainOfficeManager.create_main_office(db, main_office)

#Get All Sectors
@office_router.get(
    "/sectors",
    response_model=List[DOTSector],
    status_code=status.HTTP_200_OK
)
def get_all_sectors(db: Session = Depends(get_db)):
    return DOTSectorManager.get_all_sectors(db)

#Sector Create
@office_router.post(
    "/sectors",
    response_model=DOTSector,
    status_code=status.HTTP_201_CREATED
)
def create_sector(sector: DOTSectorCreate, db: Session = Depends(get_db)):
    return DOTSectorManager.create_sector(db, sector)

#Get All Sub-sectors
@office_router.get(
    "/sub-sectors",
    response_model=list[DOTSubSector],
    status_code=status.HTTP_200_OK
)
def get_all_sub_sectors(db: Session = Depends(get_db)):
    return DOTSubSectorManager.get_all_sub_sectors(db)

#Sub-sectors Create
@office_router.post(
    "/sub-sectors",
    response_model=DOTSubSector,
    status_code=status.HTTP_201_CREATED
)
def create_sub_sector(sub_sector: DOTSubSectorCreate, db: Session = Depends(get_db)):
    return DOTSubSectorManager.create_sub_sector(db, sub_sector)

#GET ALL OFFICE
@office_router.get(
    "/offices",
    response_model=List[DOTOffice],
    status_code=status.HTTP_200_OK
)
def get_all_offices(db: Session = Depends(get_db)):
    return DOTOfficeManager.get_all_offices(db)

#CREATE NEW OFFICE
@office_router.post(
    "/offices",
    response_model=DOTOffice,
    status_code=status.HTTP_201_CREATED
)
def create_office(office: DOTOfficeCreate, db: Session = Depends(get_db)):
    return DOTOfficeManager.create_office(db, office)

#GET ALL DIVISIONS
@office_router.get(
    "/divisions",
    response_model=List[DOTDivision],
    status_code=status.HTTP_200_OK
)
def get_all_divisions(db: Session = Depends(get_db)):
    return DOTDivisionManager.get_all_division(db)

#CREATE NEW DIVISION
@office_router.post(
    "/divisions",
    response_model=DOTDivision,
    status_code=status.HTTP_201_CREATED
)
def create_division(division: DOTDivisionCreate, db: Session = Depends(get_db)):
    return DOTDivisionManager.create_division(db, division)

#GET ALL UNIT
@office_router.get(
    "/units",
    response_model=List[DOTUnit],
    status_code=status.HTTP_200_OK
)
def get_all_units(db: Session = Depends(get_db)):
    return DOTUnitManager.get_all_units(db)

#CREATE NEW UNIT
@office_router.post(
    "/units",
    response_model=DOTUnit,
    status_code=status.HTTP_201_CREATED
)
def create_unit(unit: DOTUnitCreate, db: Session = Depends(get_db)):
    return DOTUnitManager.create_unit(db, unit)