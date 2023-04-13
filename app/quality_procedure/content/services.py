from app.quality_procedure.content import models

from sqlalchemy.orm import Session

from app.quality_procedure.content.schemas import (
    QPScopeCreate,
    QPDefinitionOfTermCreate,
    QPReferenceDocumentCreate,
    QPResponsiblityAndAuthorityCreate,
    QPProcedureCreate,
    QPProcessCreate,
    QPProcessInChargeCreate,
    QPProcessRecordCreate,
    QPAttachmentAndFormCreate)

class QualityProcedureManager(object):
    @staticmethod
    def get_all_scopes(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPScope).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_scope(db: Session, scope: QPScopeCreate, drrrf_id: int):
        new_scope = models.QPScope(**scope.dict(),drrrf_id=drrrf_id)

        db.add(new_scope)
        db.commit()
        db.refresh(new_scope)
        return new_scope
    
    @staticmethod
    def get_all_definition_of_term(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPDefinitionOfTerm).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_definition_of_term(db: Session, definition_of_term: QPDefinitionOfTermCreate, drrrf_id: int):
        new_definition_of_term = models.QPDefinitionOfTerm(**definition_of_term.dict(),drrrf_id=drrrf_id)

        db.add(new_definition_of_term)
        db.commit()
        db.refresh(new_definition_of_term)
        return new_definition_of_term

    @staticmethod
    def get_all_reference_document(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPReferenceDocument).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_reference_document(db: Session, reference_document: QPReferenceDocumentCreate, drrrf_id: int):
        new_reference_document = models.QPReferenceDocument(**reference_document.dict(),drrrf_id=drrrf_id)

        db.add(new_reference_document)
        db.commit()
        db.refresh(new_reference_document)
        return new_reference_document
    
    @staticmethod
    def get_all_responsibility_and_authority(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPResponsbilityAndAuthority).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_all_drrrf_responsibility_and_authority(db: Session, drrrf_id: int):
        return db.query(models.QPResponsbilityAndAuthority).filter(models.QPResponsbilityAndAuthority.drrrf_id == drrrf_id).all()
    
    @staticmethod
    def create_responsibility_and_authority(db: Session, responsibility_and_authority: QPResponsiblityAndAuthorityCreate, drrrf_id: int):
        new_responsibility_and_authority = models.QPResponsbilityAndAuthority(**responsibility_and_authority.dict(), drrrf_id=drrrf_id)

        db.add(new_responsibility_and_authority)
        db.commit()
        db.refresh(new_responsibility_and_authority)
        return new_responsibility_and_authority
    
    @staticmethod
    def get_all_procedure(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcedure).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_drrrf_procedures(db: Session, drrrf_id: int):
        return db.query(models.QPProcedure).filter(models.QPProcedure.drrrf_id == drrrf_id).all()
    
    @staticmethod
    def create_procedure(db: Session, procedure: QPProcedureCreate, drrrf_id: int):
        new_procedure = models.QPProcedure(**procedure.dict(),drrrf_id=drrrf_id)

        db.add(new_procedure)
        db.commit()
        db.refresh(new_procedure)
        return new_procedure

    @staticmethod
    def get_all_process(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcess).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process(db: Session, process: QPProcessCreate, drrrf_id: int, procedure_id: int):
        new_process = models.QPProcess(**process.dict(),drrrf_id=drrrf_id,procedure_id=procedure_id)

        db.add(new_process)
        db.commit()
        db.refresh(new_process)
        return new_process
    
    @staticmethod
    def get_all_process_in_charge(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessInCharge).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_process_in_charge(db: Session, process_in_charge: QPProcessInChargeCreate, drrrf_id: int, process_id: int):
        new_process_in_charge = models.QPProcessInCharge(**process_in_charge.dict(), drrrf_id=drrrf_id,process_id=process_id)

        db.add(new_process_in_charge)
        db.commit()
        db.refresh(new_process_in_charge)
        return new_process_in_charge
    
    @staticmethod
    def get_all_process_record(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPProcessRecord).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_all_process_process_record(db: Session, process_id: int):
        return db.query(models.QPProcessRecord).filter(models.QPProcessRecord.process_id == process_id).all()
    
    @staticmethod
    def create_process_record(db: Session, process_record: QPProcessRecordCreate, drrrf_id: int, process_id: int):
        new_process_record = models.QPProcessRecord(**process_record.dict(), drrrf_id=drrrf_id,process_id=process_id)

        db.add(new_process_record)
        db.commit()
        db.refresh(new_process_record)
        return new_process_record
    
    @staticmethod
    def get_all_attachment_and_form(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.QPAttachmentAndForm).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_all_drrrf_attachment_and_form(db: Session, drrrf_id: int):
        return db.query(models.QPAttachmentAndForm).filter(models.QPAttachmentAndForm.drrrf_id == drrrf_id).all()
    
    @staticmethod
    def create_attachment_and_form(db: Session, attachment_and_form: QPAttachmentAndFormCreate, drrrf_id: int):
        new_attachment_and_form = models.QPAttachmentAndForm(**attachment_and_form.dict(), drrrf_id=drrrf_id)

        db.add(new_attachment_and_form)
        db.commit()
        db.refresh(new_attachment_and_form)
        return new_attachment_and_form