from app.quality_procedure.status import models

from sqlalchemy.orm import Session

from app.quality_procedure.status.schemas import StatusBase, StatusActionsBase

class StatusManager(object):
    @staticmethod
    def get_all_status(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Status).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_status(db: Session, status: StatusBase):
        new_status = models.Status(**status.dict())

        db.add(new_status)
        db.commit()
        return new_status
    
class StatusActionsManager(object):
    @staticmethod
    def get_all_status_actions(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.StatusActions).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_status_actions(db: Session, status_action: StatusActionsBase):
        new_status_action = models.StatusActions(**status_action.dict())

        db.add(new_status_action)
        db.commit()
        return new_status_action