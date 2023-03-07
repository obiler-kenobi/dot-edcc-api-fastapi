from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.requests.schemas import QualityProcedureRequest, QualityProcedureRequestCreate
from app.quality_procedure.requests.services import QualityProcedureRequestManager

from app.deps import get_db

quality_procedure_requests_router = APIRouter()

#GET ALL QP REQUESTS
@quality_procedure_requests_router.get(
    "/requests",
    response_model=List[QualityProcedureRequest],
    status_code=status.HTTP_200_OK
)
def get_all_active_quality_procedure_document_requests(db: Session = Depends(get_db)):
    return QualityProcedureRequestManager.get_all_quality_procedure_requests(db)

#CREATE QP REQUEST
@quality_procedure_requests_router.post(
    "/requests",
    response_model=QualityProcedureRequest,
    status_code=status.HTTP_201_CREATED
)
def create_quality_procedure_document_request(quality_procedure_request: QualityProcedureRequestCreate, db: Session = Depends(get_db)):
    return QualityProcedureRequestManager.create_quality_procedure_request(db, quality_procedure_request)
