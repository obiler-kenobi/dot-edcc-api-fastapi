
from sqlalchemy.orm import Session

from app.qms_team import models
from app.qms_team.schemas import ISOFacilitatorCreate

class ISOFaciliatorManager(object):
    @staticmethod
    def get_all_iso_facilitators(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.ISOFacilitator).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_iso_facilitator(db: Session, iso_facilitator: ISOFacilitatorCreate):
        new_iso_facilitator = models.ISOFacilitator(**iso_facilitator.dict())

        db.add(new_iso_facilitator)
        db.commit()
        return new_iso_facilitator