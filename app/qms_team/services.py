
from sqlalchemy.orm import Session

from app.qms_team import models
from app.qms_team.schemas import ISOFacilitatorCreate, DISOFacilitatorCreate, HeadOfOfficeCreate

class ISOFacilitatorManager(object):
    @staticmethod
    def get_all_iso_facilitators(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.ISOFacilitator).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_iso_facilitator(db: Session, iso_facilitator: ISOFacilitatorCreate):
        new_iso_facilitator = models.ISOFacilitator(**iso_facilitator.dict())

        db.add(new_iso_facilitator)
        db.commit()
        return new_iso_facilitator
    
class DISOFacilitatorManager(object):
    @staticmethod
    def get_all_diso_facilitators(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DISOFacilitator).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_diso_facilitator(db: Session, diso_facilitator: DISOFacilitatorCreate):
        new_diso_facilitator = models.DISOFacilitator(**diso_facilitator.dict())

        db.add(new_diso_facilitator)
        db.commit()
        return new_diso_facilitator
    
class HeadOfOfficeManager(object):
    @staticmethod
    def get_all_head_of_office(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.HeadOfOffice).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_head_of_office(db: Session, head_of_office: HeadOfOfficeCreate):
        new_head_of_office = models.HeadOfOffice(**head_of_office.dict())

        db.add(new_head_of_office)
        db.commit()
        return new_head_of_office