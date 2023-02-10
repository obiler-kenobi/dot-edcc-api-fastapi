from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import QualityProcedureDocumentRequest, QualityProcedureDocumentRequestCreate, QPRequestHistory, QPRequestHistoryCreate
from app.quality_procedure.services import QualityProcedureDocumentRequestManager
from app.deps import get_db

quality_procedure_router = APIRouter()

#GET ALL QP REQUESTS
@quality_procedure_router.get(
    "/qp-document-requests",
    response_model=List[QualityProcedureDocumentRequest],
    status_code=status.HTTP_200_OK
)
def get_all_quality_procedure_document_requests(db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.get_all_quality_procedure_document_requests(db)

#CREATE QP REQUEST
@quality_procedure_router.post(
    "/qp-document-requests",
    response_model=QualityProcedureDocumentRequest,
    status_code=status.HTTP_201_CREATED
)
def create_quality_procedure_document_request(quality_procedure_document_request: QualityProcedureDocumentRequestCreate, db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.create_quality_procedure_document_request(db, quality_procedure_document_request)

#GET ALL QP REQUEST HISTORY
@quality_procedure_router.get(
    "/qp-request-history",
    response_model=List[QPRequestHistory],
    status_code=status.HTTP_200_OK
)
def get_all_qp_request_history(db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.get_all_qp_request_history(db)

#CREATE QP REQUEST HISTORY
@quality_procedure_router.post(
    "/qp-request-history",
    response_model=QPRequestHistory,
    status_code=status.HTTP_201_CREATED
)
def create_qp_request_history(qp_request_history: QPRequestHistoryCreate, db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.create_qp_request_history(db, qp_request_history)