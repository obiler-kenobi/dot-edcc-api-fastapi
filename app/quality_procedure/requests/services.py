from typing import List

from app.quality_procedure.requests import models

from sqlalchemy.orm import Session

from app.quality_procedure.requests.schemas import QualityProcedureRequestCreate, QualityProcedureRequestHistory, QualityProcedureStatusUpdate

class QualityProcedureRequestManager(object): 
    @staticmethod
    def get_all_quality_procedure_requests(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QualityProcedureRequests).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_quality_procedure_request(db: Session, quality_procedure_request: QualityProcedureRequestCreate):
        new_quality_procedure_request = models.QualityProcedureRequests(**quality_procedure_request.dict())

        db.add(new_quality_procedure_request)
        db.commit()
        return new_quality_procedure_request
    
    @staticmethod
    def update_quality_procedure_request_status(db: Session, request_id: int, quality_procedure_request_update: QualityProcedureStatusUpdate):
        stored_item_data = db.query(models.QualityProcedureRequests).filter(models.QualityProcedureRequests.id == request_id).first()
        update_data = quality_procedure_request_update.dict(exclude_unset=True)
        db.query(models.QualityProcedureRequests).filter(models.QualityProcedureRequests.id == request_id).update(update_data, synchronize_session=False)
        
        db.commit()
        db.refresh(stored_item_data)
        return stored_item_data

class QualityProcedureRequestHistoryManager(object):
    @staticmethod
    def get_all_quality_procedure_request_history(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QualityProcedureRequestHistory).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_quality_procedure_request_history(db: Session, request_id: int):
        return db.query(models.QualityProcedureRequestHistory).filter(models.QualityProcedureRequestHistory.request_id == request_id).order_by(models.QualityProcedureRequestHistory.time_created.desc()).all()
    
    @staticmethod
    def create_quality_procedure_request_history(db: Session, quality_procedure_request_history: QualityProcedureRequestHistory, request_id: int):
        new_quality_procedure_request_history = models.QualityProcedureRequestHistory(**quality_procedure_request_history.dict(),request_id=request_id)

        db.add(new_quality_procedure_request_history)
        db.commit()
        db.refresh(new_quality_procedure_request_history)
        return new_quality_procedure_request_history
