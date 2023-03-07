from app.quality_procedure.requests import models

from sqlalchemy.orm import Session

from app.quality_procedure.requests.schemas import QualityProcedureRequestCreate

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
    
    
        new_qp_request_history = models.QPRequestHistory(**qp_request_history.dict())

        db.add(new_qp_request_history)
        db.commit()
        return new_qp_request_history