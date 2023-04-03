from app.quality_procedure.content import models

from sqlalchemy.orm import Session

from app.quality_procedure.content.schemas import QPScopeCreate, QPDefinitionOfTermCreate

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
