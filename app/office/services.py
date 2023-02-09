from app.office import models

from sqlalchemy.orm import Session

from app.office.schemas import DOTMainOfficeCreate,DOTSectorCreate,DOTSubSectorCreate,DOTOfficeCreate,DOTDivisionCreate,DOTUnitCreate

class DOTMainOfficeManager(object):
    @staticmethod
    def get_all_main_offices(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTMainOffice).offset(skip).limit(limit).all()

    @staticmethod
    def create_main_office(db: Session, main_office: DOTMainOfficeCreate):
        new_main_office = models.DOTMainOffice(**main_office.dict())

        db.add(new_main_office)
        db.commit()
        return new_main_office

class DOTSectorManager(object):
    @staticmethod
    def get_all_sectors(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTSector).offset(skip).limit(limit).all()

    @staticmethod
    def create_sector(db: Session, sector: DOTSectorCreate):
        new_sector = models.DOTSector(**sector.dict())

        db.add(new_sector)
        db.commit()
        return new_sector

class DOTSubSectorManager(object):
    @staticmethod
    def get_all_sub_sectors(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTSubSector).offset(skip).limit(limit).all()

    @staticmethod
    def create_sub_sector(db: Session, sub_sector: DOTSubSectorCreate):
        new_sub_sector = models.DOTSubSector(**sub_sector.dict())

        db.add(new_sub_sector)
        db.commit()
        return new_sub_sector

class DOTOfficeManager(object):
    @staticmethod
    def get_all_offices(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTOffice).offset(skip).limit(limit).all()

    @staticmethod
    def create_office(db: Session, office: DOTOfficeCreate):
        new_office = models.DOTOffice(**office.dict())

        db.add(new_office)
        db.commit()
        return new_office

class DOTDivisionManager(object):
    @staticmethod
    def get_all_division(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTDivision).offset(skip).limit(limit).all()

    @staticmethod
    def create_division(db: Session, division: DOTDivisionCreate):
        new_division = models.DOTDivision(**division.dict())

        db.add(new_division)
        db.commit()
        return new_division

class DOTUnitManager(object):
    @staticmethod
    def get_all_units(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DOTUnit).offset(skip).limit(limit).all()

    @staticmethod
    def create_unit(db: Session, unit: DOTUnitCreate):
        new_unit = models.DOTUnit(**unit.dict())

        db.add(new_unit)
        db.commit()
        return new_unit