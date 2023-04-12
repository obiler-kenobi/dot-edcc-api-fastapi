from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.content.schemas import (
    QPScope, 
    QPScopeCreate,
    QPDefinitionOfTerm,
    QPDefinitionOfTermCreate,
    QPReferenceDocument,
    QPReferenceDocumentCreate,
    QPResponsiblityAndAuthority,
    QPResponsiblityAndAuthorityCreate,
    QPProcedure,
    QPProcedureCreate,
    QPProcess,
    QPProcessCreate)
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

#GET ALL REFERENCE DOCUMENT
@quality_procedure_content_router.get(
    "/reference-documents",
    response_model=List[QPReferenceDocument],
    status_code=status.HTTP_200_OK
)
def get_all_reference_document(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_reference_document(db)

#CREATE REFERENCE DOCUMENT
@quality_procedure_content_router.post(
    "/{drrrf_id}/reference-documents",
    response_model=QPReferenceDocument,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(drrrf_id: int, reference_document: QPReferenceDocumentCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_reference_document(db, reference_document, drrrf_id)

#GET ALL RESPONSIBLITY AND AUTHORITY
@quality_procedure_content_router.get(
    "/responsiblities-and-authorities",
    response_model=List[QPResponsiblityAndAuthority],
    status_code=status.HTTP_200_OK
)
def get_all_responsibility_and_authority(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_responsibility_and_authority(db)

#GET ALL RESPONSIBLITY AND AUTHORITY
@quality_procedure_content_router.get(
    "/{drrrf_id}/responsiblities-and-authorities",
    response_model=List[QPResponsiblityAndAuthority],
    status_code=status.HTTP_200_OK
)
def get_all_drrrf_responsibility_and_authority(drrrf_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_drrrf_responsibility_and_authority(db, drrrf_id)

#CREATE RESPONSIBILITIES AND AUTHORITIES
@quality_procedure_content_router.post(
    "/{drrrf_id}/responsibilities-and-authorities",
    response_model=QPResponsiblityAndAuthority,
    status_code=status.HTTP_201_CREATED
)
def create_responsibility_and_authority(drrrf_id: int, responsibility_and_authority: QPResponsiblityAndAuthorityCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_responsibility_and_authority(db, responsibility_and_authority, drrrf_id)

#GET ALL PROCEDURE
@quality_procedure_content_router.get(
    "/procedures",
    response_model=List[QPProcedure],
    status_code=status.HTTP_200_OK
)
def get_all_procedure(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_procedure(db)

#CREATE PROCEDURE
@quality_procedure_content_router.get(
    "/{drrrf_id}/procedures",
    response_model=List[QPProcedure],
    status_code=status.HTTP_200_OK
)
def get_drrrf_procedures(drrrf_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_drrrf_procedures(db, drrrf_id)

#CREATE PROCEDURE
@quality_procedure_content_router.post(
    "/{drrrf_id}/procedures",
    response_model=QPProcedure,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(drrrf_id: int, procedure: QPProcedureCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_procedure(db, procedure, drrrf_id)

#GET ALL PROCESS
@quality_procedure_content_router.get(
    "/processes",
    response_model=List[QPProcess],
    status_code=status.HTTP_200_OK
)
def get_all_process(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process(db)

#CREATE PROCESS
@quality_procedure_content_router.post(
    "/{drrrf_id}/procedures/{procedure_id}/processes",
    response_model=QPProcess,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(drrrf_id: int, procedure_id: int, process: QPProcessCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process(db, process, drrrf_id, procedure_id)