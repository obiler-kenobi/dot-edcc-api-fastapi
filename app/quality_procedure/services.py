from app.quality_procedure import models

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import QualityProcedureDocumentRequestStatusUpdate, QualityProcedureDocumentRequestCreate, QPRequestHistoryCreate, DRRRFCreate, DRRRFStatusUpdate, DRRRFDistributeUpdate, InterfacingUnitCreate, IUReviewSummaryCreate
from app.quality_procedure.schemas import QPTitlePageCreate, QPObjectiveCreate, QPProcessNoteCreate, QPReportCreate
from app.quality_procedure.schemas import StatusCreate
from app.quality_procedure.schemas import DistributionListCreate

from operator import itemgetter

class QualityProcedureDocumentRequestManager(object): 
    @staticmethod
    def get_all_active_quality_procedure_document_requests(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QualityProcedureDocumentRequest).filter(models.QualityProcedureDocumentRequest.status_id <= 6).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_quality_procedure_document_request(db: Session, quality_procedure_document_request: QualityProcedureDocumentRequestCreate):
        new_quality_procedure_document_request = models.QualityProcedureDocumentRequest(**quality_procedure_document_request.dict())

        db.add(new_quality_procedure_document_request)
        db.commit()
        return new_quality_procedure_document_request
    
    @staticmethod
    def update_quality_procedure_document_request_status(db: Session, request_id: int, quality_procedure_document_request: QualityProcedureDocumentRequestStatusUpdate):
        stored_item_data = db.query(models.QualityProcedureDocumentRequest).filter(models.QualityProcedureDocumentRequest.id == request_id).first()
        update_data = quality_procedure_document_request.dict(exclude_unset=True)
        db.query(models.QualityProcedureDocumentRequest).filter(models.QualityProcedureDocumentRequest.id == request_id).update(update_data, synchronize_session=False)
        
        db.commit()
        db.refresh(stored_item_data)
        return stored_item_data
    
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
    
    def get_all_ongoing_drrrfs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DRRRF).filter(models.DRRRF.drrrf_status == 'ongoing').offset(skip).limit(limit).all()
    
    def get_all_registered_drrrfs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DRRRF).filter(models.DRRRF.drrrf_status == 'registered').offset(skip).limit(limit).all()
    
    def get_all_distributed_drrrfs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DRRRF).filter(models.DRRRF.drrrf_status == 'distributed').offset(skip).limit(limit).all()
    
    def get_all_obsolete_drrrfs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.DRRRF).filter(models.DRRRF.drrrf_status == 'obsolete').offset(skip).limit(limit).all()

    @staticmethod
    def get_drrrf(db: Session, slug: str):
        procedure = db.query(models.DRRRF).filter(models.DRRRF.slug == slug).first()
        PROCEDURE_LENGTH = len(procedure.qp_procedure)

        procedure.qp_procedure = sorted(procedure.qp_procedure, key=lambda x: x.id)

        for x in range(PROCEDURE_LENGTH):
            procedure.qp_procedure[x].qp_process = sorted(procedure.qp_procedure[x].qp_process, key=lambda x: x.id)
    
        return procedure
    
    @staticmethod
    def approve_quality_procedure(db: Session, drrrf_id: int, drrrf_status: DRRRFStatusUpdate):
        stored_item_data = db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).first()
        update_data = drrrf_status.dict(exclude_unset=True)
        db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).update(update_data, synchronize_session=False)
        
        db.commit()
        db.refresh(stored_item_data)
        return stored_item_data
    
    @staticmethod
    def obsolete_quality_procedure(db: Session, drrrf_id: int, drrrf_status: DRRRFStatusUpdate):
        stored_item_data = db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).first()
        update_data = drrrf_status.dict(exclude_unset=True)
        db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).update(update_data, synchronize_session=False)
        
        db.commit()
        db.refresh(stored_item_data)
        return stored_item_data
    
    @staticmethod
    def distribute_quality_procedure(db: Session, drrrf_id: int, drrrf_distribute: DRRRFDistributeUpdate):
        stored_item_data = db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).first()
        update_data = drrrf_distribute.dict(exclude_unset=True)
        db.query(models.DRRRF).filter(models.DRRRF.id == drrrf_id).update(update_data, synchronize_session=False)
        
        db.commit()
        db.refresh(stored_item_data)
        return stored_item_data
    
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

class QualityProcedureManager(object):
    @staticmethod
    def get_all_title_page(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPTitlePage).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_title_page(db: Session, title_page: QPTitlePageCreate, drrrf_id: int):
        new_title_page = models.QPTitlePage(**title_page.dict(),drrrf_id=drrrf_id)

        db.add(new_title_page)
        db.commit()
        db.refresh(new_title_page)
        return new_title_page
    
    @staticmethod
    def get_all_objectives(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPObjective).offset(skip).limit(limit).all()

    @staticmethod
    def create_objective(db: Session, objective: QPObjectiveCreate, drrrf_id: int):
        new_objective = models.QPObjective(**objective.dict(),drrrf_id=drrrf_id)

        db.add(new_objective)
        db.commit()
        db.refresh(new_objective)
        return new_objective

    @staticmethod
    def get_all_process_note(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessNote).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_note(db: Session, process_note: QPProcessNoteCreate, drrrf_id: int, process_id: int):
        new_process_note = models.QPProcessNote(**process_note.dict(),drrrf_id=drrrf_id,process_id=process_id)

        db.add(new_process_note)
        db.commit()
        db.refresh(new_process_note)
        return new_process_note

    @staticmethod
    def get_all_report(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPReport).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_report(db: Session, report: QPReportCreate, drrrf_id: int):
        new_report = models.QPReport(**report.dict(), drrrf_id=drrrf_id)

        db.add(new_report)
        db.commit()
        db.refresh(new_report)
        return new_report


    
class StatusManager(object):
    @staticmethod
    def get_all_status(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Status).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_status(db: Session, status: StatusCreate):
        new_status = models.Status(**status.dict())

        db.add(new_status)
        db.commit()
        return new_status
    
class DistributionListManager(object):
    @staticmethod
    def get_all_distribution_list(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPDistributionList).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_all_drrrf_distribution_list(db: Session, drrrf_id: int):
        return db.query(models.QPDistributionList).filter(models.QPDistributionList.drrrf_id == drrrf_id).all()
    
    @staticmethod
    def create_distribution_list(db: Session, distribution_list: DistributionListCreate):
        new_distribution_list = models.QPDistributionList(**distribution_list.dict())

        db.add(new_distribution_list)
        db.commit()
        return new_distribution_list