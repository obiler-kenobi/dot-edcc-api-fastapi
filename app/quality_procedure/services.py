from app.quality_procedure import models

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import QualityProcedureDocumentRequestCreate, QPRequestHistoryCreate, DRRRFCreate, InterfacingUnitCreate, IUReviewSummaryCreate

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
    
class DRRRFManager(object):
    @staticmethod
    def get_all_drrrfs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DRRRF).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_drrrf(db: Session, drrrf: DRRRFCreate):
        new_drrrf = models.DRRRF(**drrrf.dict())

        db.add(new_drrrf)
        db.commit()
        return new_drrrf
    
    @staticmethod
    def get_all_interfacing_units(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.InterfacingUnit).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_interfacing_unit(db: Session , interfacing_unit: InterfacingUnitCreate):
        new_interfacing_unit = models.InterfacingUnit(**interfacing_unit.dict())

        db.add(new_interfacing_unit)
        db.commit()
        return new_interfacing_unit

    @staticmethod
    def get_all_iu_review_summary(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.IUReviewSummary).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_iu_review_summary(db: Session, iu_review_summary: IUReviewSummaryCreate):
        new_iu_review_summary = models.IUReviewSummary(**iu_review_summary.dict())

        db.add(new_iu_review_summary)
        db.commit()
        return new_iu_review_summary
