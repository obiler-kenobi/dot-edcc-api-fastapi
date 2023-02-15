from app.quality_procedure import models

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import QualityProcedureDocumentRequestCreate, QPRequestHistoryCreate, DRRRFCreate, InterfacingUnitCreate, IUReviewSummaryCreate
from app.quality_procedure.schemas import QPTitlePageCreate, QPObjectiveCreate, QPScopeCreate, QPDefinitionOfTermCreate, QPReferenceDocumentCreate, QPResponsiblityAndAuthorityCreate, QPProcedureCreate, QPProcessCreate, QPProcessInChargeCreate, QPProcessNoteCreate, QPProcessRecordCreate, QPReportCreate, QPPerformanceIndicatorCreate, QPAttachmentAndFormCreate

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

class QualityProcedureManager(object):
    @staticmethod
    def get_all_title_page(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPTitlePage).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_title_page(db: Session, title_page: QPTitlePageCreate):
        new_title_page = models.QPTitlePage(**title_page.dict())

        db.add(new_title_page)
        db.commit()
        return new_title_page
    
    @staticmethod
    def get_all_objectives(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPObjective).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_objective(db: Session, objective: QPObjectiveCreate):
        new_objective = models.QPObjective(**objective.dict())

        db.add(new_objective)
        db.commit()
        return new_objective
    
    @staticmethod
    def get_all_scopes(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPScope).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_scope(db: Session, scope: QPScopeCreate):
        new_scope = models.QPScope(**scope.dict())

        db.add(new_scope)
        db.commit()
        return new_scope
    
    @staticmethod
    def get_all_definition_of_term(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPDefinitionOfTerm).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_definition_of_term(db: Session, definition_of_term: QPDefinitionOfTermCreate):
        new_definition_of_term = models.QPDefinitionOfTerm(**definition_of_term.dict())

        db.add(new_definition_of_term)
        db.commit()
        return new_definition_of_term
    
    @staticmethod
    def get_all_reference_document(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPReferenceDocument).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_reference_document(db: Session, reference_document: QPReferenceDocumentCreate):
        new_reference_document = models.QPReferenceDocument(**reference_document.dict())

        db.add(new_reference_document)
        db.commit()
        return new_reference_document
    
    @staticmethod
    def get_all_responsibility_and_authority(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPResponsbilityAndAuthority).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_responsibility_and_authority(db: Session, responsibility_and_authority: QPResponsiblityAndAuthorityCreate):
        new_responsibility_and_authority = models.QPResponsbilityAndAuthority(**responsibility_and_authority.dict())

        db.add(new_responsibility_and_authority)
        db.commit()
        return new_responsibility_and_authority
    
    @staticmethod
    def get_all_procedure(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcedure).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_procedure(db: Session, procedure: QPProcedureCreate):
        new_procedure = models.QPProcedure(**procedure.dict())

        db.add(new_procedure)
        db.commit()
        return new_procedure
    
    @staticmethod
    def get_all_process(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcess).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process(db: Session, process: QPProcessCreate):
        new_process = models.QPProcess(**process.dict())

        db.add(new_process)
        db.commit()
        return new_process

    @staticmethod
    def get_all_process_in_charge(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessInCharge).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_in_charge(db: Session, process_in_charge: QPProcessInChargeCreate):
        new_process_in_charge = models.QPProcessInCharge(**process_in_charge.dict())

        db.add(new_process_in_charge)
        db.commit()
        return new_process_in_charge
    
    @staticmethod
    def get_all_process_note(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessNote).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_note(db: Session, process_note: QPProcessNoteCreate):
        new_process_note = models.QPProcessNote(**process_note.dict())

        db.add(new_process_note)
        db.commit()
        return new_process_note

    @staticmethod
    def get_all_process_record(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessRecord).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_record(db: Session, process_record: QPProcessRecordCreate):
        new_process_record = models.QPProcessRecord(**process_record.dict())

        db.add(new_process_record)
        db.commit()
        return new_process_record
    
    @staticmethod
    def get_all_process_record(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessRecord).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_record(db: Session, process_record: QPProcessRecordCreate):
        new_process_record = models.QPProcessRecord(**process_record.dict())

        db.add(new_process_record)
        db.commit()
        return new_process_record
    
    @staticmethod
    def get_all_report(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPReport).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_report(db: Session, report: QPReportCreate):
        new_report = models.QPReport(**report.dict())

        db.add(new_report)
        db.commit()
        return new_report
    
    @staticmethod
    def get_all_performance_indicator(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPPerformanceIndicator).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_performance_indicator(db: Session, performance_indicator: QPPerformanceIndicatorCreate):
        new_performance_indicator = models.QPPerformanceIndicator(**performance_indicator.dict())

        db.add(new_performance_indicator)
        db.commit()
        return new_performance_indicator
    
    @staticmethod
    def get_all_attachment_and_form(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPAttachmentAndForm).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_attachment_and_form(db: Session, attachment_and_form: QPAttachmentAndFormCreate):
        new_attachment_and_form = models.QPAttachmentAndForm(**attachment_and_form.dict())

        db.add(new_attachment_and_form)
        db.commit()
        return new_attachment_and_form