from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.content.schemas import (
    QPScope, 
    QPScopeCreate,
    QPDefinitionOfTerm,
    QPDefinitionOfTermCreate)
from app.quality_procedure.content.services import QualityProcedureManager
from app.deps import get_db

quality_procedure_content_router = APIRouter()

#GET ALL SCOPE
@quality_procedure_content_router.get(
    "/scopes",
    response_model=List[QPScope],
    status_code=status.HTTP_200_OK
)
def get_all_scopes(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_scopes(db)

#CREATE SCOPE
@quality_procedure_content_router.post(
    "/{drrrf_id}/scopes",
    response_model=QPScope,
    status_code=status.HTTP_201_CREATED
)
def create_scope(drrrf_id: int, scope: QPScopeCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_scope(db, scope, drrrf_id)

#GET ALL DEFINITION OF TERM
@quality_procedure_content_router.get(
    "/definition-of-terms",
    response_model=List[QPDefinitionOfTerm],
    status_code=status.HTTP_200_OK
)
def get_all_definition_of_terms(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_definition_of_term(db)

#CREATE DEFINITION OF TERM
@quality_procedure_content_router.post(
    "/{drrrf_id}/definition-of-terms",
    response_model=QPDefinitionOfTerm,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(drrrf_id: int, definition_of_term: QPDefinitionOfTermCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_definition_of_term(db, definition_of_term, drrrf_id)