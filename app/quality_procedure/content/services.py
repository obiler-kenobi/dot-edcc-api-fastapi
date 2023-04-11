from app.quality_procedure.content import models

from sqlalchemy.orm import Session

from app.quality_procedure.content.schemas import QPScopeCreate, QPDefinitionOfTermCreate, QPReferenceDocumentCreate, QPResponsiblityAndAuthorityCreate

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