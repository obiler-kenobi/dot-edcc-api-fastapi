from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import (QualityProcedureDocumentRequest, QualityProcedureDocumentRequestCreate, QPRequestHistory, QPRequestHistoryCreate) #QP REQUESTS
from app.quality_procedure.schemas import DRRRF, DRRRFCreate, InterfacingUnit, InterfacingUnitCreate, IUReviewSummary, IUReviewSummaryCreate
from app.quality_procedure.services import QualityProcedureDocumentRequestManager, DRRRFManager
from app.quality_procedure.schemas import TitlePage, TitlePageCreate
from app.quality_procedure.services import QualityProcedureManager
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

#GET ALL DRRRF
@quality_procedure_router.get(
    "/drrrfs",
    response_model=List[DRRRF],
    status_code=status.HTTP_200_OK
)
def get_all_drrrfs(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_drrrfs(db)

#CREATE DRRRF
@quality_procedure_router.post(
    "/drrrfs",
    response_model=DRRRF,
    status_code=status.HTTP_201_CREATED
)
def create_drrrf(drrrf: DRRRFCreate, db: Session = Depends(get_db)):
    return DRRRFManager.create_drrrf(db, drrrf)

#GET ALL INTERFACING UNIT
@quality_procedure_router.get(
    "/interfacing-units",
    response_model=List[InterfacingUnit],
    status_code=status.HTTP_200_OK
)
def get_all_interfacing_units(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_interfacing_units(db)

#CREATE INTERFACING UNIT
@quality_procedure_router.post(
    "/interfacing-units",
    response_model=InterfacingUnit,
    status_code=status.HTTP_201_CREATED
)
def create_interfacing_unit(interfacing_unit: InterfacingUnitCreate, db: Session = Depends(get_db)):
    return DRRRFManager.create_interfacing_unit(db, interfacing_unit)

#GET ALL IU REVIEW SUMMARY
@quality_procedure_router.get(
    "/iu-review-summary",
    response_model=List[IUReviewSummary],
    status_code=status.HTTP_200_OK
)
def get_all_iu_review_summary(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_iu_review_summary(db)

#CREATE IU REVIEW SUMMARY
@quality_procedure_router.post(
    "/iu-review-summary",
    response_model=IUReviewSummary,
    status_code=status.HTTP_201_CREATED
)
def create_iu_review_summary(iu_review_summary: IUReviewSummaryCreate, db: Session = Depends(get_db)):
    return DRRRFManager.create_iu_review_summary(db, iu_review_summary)

#QUALITY PROCEDURE
#GET ALL TITLE PAGE
@quality_procedure_router.get(
    "/quality-procedures/title-pages",
    response_model=List[TitlePage],
    status_code=status.HTTP_200_OK
)
def get_all_title_page(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_title_page(db)

#CREATE IU REVIEW SUMMARY
@quality_procedure_router.post(
    "/quality-procedures/title-pages",
    response_model=TitlePage,
    status_code=status.HTTP_201_CREATED
)
def create_title_page(title_page: TitlePageCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_title_page(db, title_page)