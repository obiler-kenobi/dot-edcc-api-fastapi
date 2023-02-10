from app.quality_procedure import models

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import QualityProcedureDocumentRequestCreate, QPRequestHistoryCreate

class QualityProcedureDocumentRequestManager(object): 
    @staticmethod
    def get_all_quality_procedure_document_requests(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QualityProcedureDocumentRequest).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_quality_procedure_document_request(db: Session, quality_procedure_document_request: QualityProcedureDocumentRequestCreate):
        new_quality_procedure_document_request = models.QualityProcedureDocumentRequest(**quality_procedure_document_request.dict())

        db.add(new_quality_procedure_document_request)
        db.commit()
        return new_quality_procedure_document_request
    
    @staticmethod
    def get_all_qp_request_history(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPRequestHistory).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_qp_request_history(db: Session, qp_request_history: QPRequestHistoryCreate):
        new_qp_request_history = models.QPRequestHistory(**qp_request_history.dict())

        db.add(new_qp_request_history)
        db.commit()
        return new_qp_request_history