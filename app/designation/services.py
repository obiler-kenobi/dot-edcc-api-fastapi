from app.designation import models

from sqlalchemy.orm import Session

from app.designation.schemas import DesignationCreate

class DesignationManager(object):
    @staticmethod
    def get_all_designations(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Designation).offset(skip).limit(limit).all()

    @staticmethod
    def create_designation(db: Session, designation: DesignationCreate):
        new_designation = models.Designation(**designation.dict())

        db.add(new_designation)
        db.commit()
        return new_designation