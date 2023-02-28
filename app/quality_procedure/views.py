from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import (
    QualityProcedureDocumentRequest, 
    QualityProcedureDocumentRequestStatusUpdate,
    QualityProcedureDocumentRequestCreate, 
    QPRequestHistory, 
    QPRequestHistoryCreate) #QP REQUESTS
from app.quality_procedure.schemas import DRRRF, DRRRFCreate, DRRRFStatusUpdate, DRRRFDistributeUpdate, InterfacingUnit, InterfacingUnitCreate, IUReviewSummary, IUReviewSummaryCreate
from app.quality_procedure.services import QualityProcedureDocumentRequestManager, DRRRFManager
from app.quality_procedure.schemas import QPTitlePage, QPTitlePageCreate, QPObjective, QPObjectiveCreate, QPScope, QPScopeCreate, QPDefinitionOfTerm, QPDefinitionOfTermCreate, QPReferenceDocument, QPReferenceDocumentCreate, QPResponsiblityAndAuthority, QPResponsiblityAndAuthorityCreate, QPProcedure, QPProcedureCreate, QPProcess, QPProcessCreate, QPProcessInCharge, QPProcessInChargeCreate, QPProcessNote, QPProcessNoteCreate, QPProcessRecord, QPProcessRecordCreate, QPReport, QPReportCreate, QPPerformanceIndicator, QPPerformanceIndicatorCreate, QPAttachmentAndForm, QPAttachmentAndFormCreate, Status, StatusCreate
from app.quality_procedure.services import QualityProcedureManager, StatusManager
from app.quality_procedure.schemas import DistributionList, DistributionListCreate
from app.quality_procedure.services import DistributionListManager
from app.deps import get_db

quality_procedure_router = APIRouter()

#GET ALL QP REQUESTS
@quality_procedure_router.get(
    "/qp-document-requests",
    response_model=List[QualityProcedureDocumentRequest],
    status_code=status.HTTP_200_OK
)
def get_all_active_quality_procedure_document_requests(db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.get_all_active_quality_procedure_document_requests(db)

#CREATE QP REQUEST
@quality_procedure_router.post(
    "/qp-document-requests",
    response_model=QualityProcedureDocumentRequest,
    status_code=status.HTTP_201_CREATED
)
def create_quality_procedure_document_request(quality_procedure_document_request: QualityProcedureDocumentRequestCreate, db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.create_quality_procedure_document_request(db, quality_procedure_document_request)

#UPDATE QP REQUEST STATUS
@quality_procedure_router.patch(
    "/qp-document-requests/{request_id}",
    response_model=QualityProcedureDocumentRequest,
    status_code=status.HTTP_200_OK
)
def update_quality_procedure_document_request_status(request_id: int, quality_procedure_document_request: QualityProcedureDocumentRequestStatusUpdate, db: Session = Depends(get_db)):
    return QualityProcedureDocumentRequestManager.update_quality_procedure_document_request_status(db, request_id, quality_procedure_document_request)

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

#GET ALL ONGOING DRRRF
@quality_procedure_router.get(
    "/drrrfs/ongoing",
    response_model=List[DRRRF],
    status_code=status.HTTP_200_OK
)
def get_all_ongoing_drrrfs(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_ongoing_drrrfs(db)

#GET ALL REGISTERED DRRRF
@quality_procedure_router.get(
    "/drrrfs/registered",
    response_model=List[DRRRF],
    status_code=status.HTTP_200_OK
)
def get_all_registered_drrrfs(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_registered_drrrfs(db)

#GET ALL DISTRIBUTED DRRRF
@quality_procedure_router.get(
    "/drrrfs/distributed",
    response_model=List[DRRRF],
    status_code=status.HTTP_200_OK
)
def get_all_distributed_drrrfs(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_distributed_drrrfs(db)

#GET ALL DISTRIBUTED DRRRF
@quality_procedure_router.get(
    "/drrrfs/obsolete",
    response_model=List[DRRRF],
    status_code=status.HTTP_200_OK
)
def get_all_obsolete_drrrfs(db: Session = Depends(get_db)):
    return DRRRFManager.get_all_obsolete_drrrfs(db)

#GET DRRRF VIA SLUG
@quality_procedure_router.get(
    "/drrrfs/{slug}",
    response_model=DRRRF,
    status_code=status.HTTP_200_OK
)
def get_drrrf(slug: str, db: Session = Depends(get_db)):
    return DRRRFManager.get_drrrf(db, slug)

#CREATE DRRRF
@quality_procedure_router.post(
    "/drrrfs",
    response_model=DRRRF,
    status_code=status.HTTP_201_CREATED
)
def create_drrrf(drrrf: DRRRFCreate, db: Session = Depends(get_db)):
    return DRRRFManager.create_drrrf(db, drrrf)

#APPROVE QUALITY PROCEDURE
@quality_procedure_router.patch(
    "/drrrfs/{drrrf_id}/approve",
    response_model=DRRRF,
    status_code=status.HTTP_200_OK
)
def approve_quality_procedure(drrrf_id: int, drrrf_status: DRRRFStatusUpdate, db: Session = Depends(get_db)):
    return DRRRFManager.approve_quality_procedure(db, drrrf_id, drrrf_status)

#APPROVE QUALITY PROCEDURE
@quality_procedure_router.patch(
    "/drrrfs/{drrrf_id}/distribute",
    response_model=DRRRF,
    status_code=status.HTTP_200_OK
)
def distribute_quality_procedure(drrrf_id: int, drrrf_status: DRRRFDistributeUpdate, db: Session = Depends(get_db)):
    return DRRRFManager.distribute_quality_procedure(db, drrrf_id, drrrf_status)

#OBSOLETE QUALITY PROCEDURE
@quality_procedure_router.patch(
    "/drrrfs/{drrrf_id}/obsolete",
    response_model=DRRRF,
    status_code=status.HTTP_200_OK
)
def obsolete_quality_procedure(drrrf_id: int, drrrf_status: DRRRFStatusUpdate, db: Session = Depends(get_db)):
    return DRRRFManager.obsolete_quality_procedure(db, drrrf_id, drrrf_status)


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
    response_model=List[QPTitlePage],
    status_code=status.HTTP_200_OK
)
def get_all_title_page(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_title_page(db)

#CREATE TITLE PAGE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/title-pages",
    response_model=QPTitlePage,
    status_code=status.HTTP_201_CREATED
)
def create_title_page(drrrf_id: int, title_page: QPTitlePageCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_title_page(db, title_page, drrrf_id)

#GET ALL OBJECTIVE
@quality_procedure_router.get(
    "/quality-procedures/objectives",
    response_model=List[QPObjective],
    status_code=status.HTTP_200_OK
)
def get_all_objectives(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_objectives(db)

#CREATE OBJECTIVE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/objectives",
    response_model=QPObjective,
    status_code=status.HTTP_201_CREATED
)
def create_objective(drrrf_id: int, objective: QPObjectiveCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_objective(db, objective, drrrf_id)

#GET ALL SCOPE
@quality_procedure_router.get(
    "/quality-procedures/scopes",
    response_model=List[QPScope],
    status_code=status.HTTP_200_OK
)
def get_all_scopes(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_scopes(db)

#CREATE SCOPE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/scopes",
    response_model=QPScope,
    status_code=status.HTTP_201_CREATED
)
def create_scope(drrrf_id: int, scope: QPScopeCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_scope(db, scope, drrrf_id)

#GET ALL DEFINITION OF TERM
@quality_procedure_router.get(
    "/quality-procedures/definition-of-terms",
    response_model=List[QPDefinitionOfTerm],
    status_code=status.HTTP_200_OK
)
def get_all_definition_of_terms(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_definition_of_term(db)

#CREATE DEFINITION OF TERM
@quality_procedure_router.post(
    "/quality-procedures/definition-of-terms",
    response_model=QPDefinitionOfTerm,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(definition_of_term: QPDefinitionOfTermCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_definition_of_term(db, definition_of_term)

#CREATE DEFINITION OF TERM
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/definition-of-terms",
    response_model=QPDefinitionOfTerm,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(drrrf_id: int, definition_of_term: QPDefinitionOfTermCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_definition_of_term(db, definition_of_term, drrrf_id)

#GET ALL REFERENCE DOCUMENT
@quality_procedure_router.get(
    "/quality-procedures/reference-documents",
    response_model=List[QPReferenceDocument],
    status_code=status.HTTP_200_OK
)
def get_all_reference_document(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_reference_document(db)

#CREATE REFERENCE DOCUMENT
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/reference-documents",
    response_model=QPReferenceDocument,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(drrrf_id: int, reference_document: QPReferenceDocumentCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_reference_document(db, reference_document, drrrf_id)

#GET ALL RESPONSIBLITY AND AUTHORITY
@quality_procedure_router.get(
    "/quality-procedures/responsiblities-and-authorities",
    response_model=List[QPResponsiblityAndAuthority],
    status_code=status.HTTP_200_OK
)
def get_all_responsibility_and_authority(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_responsibility_and_authority(db)

#GET ALL RESPONSIBLITY AND AUTHORITY
@quality_procedure_router.get(
    "/quality-procedures/{drrrf_id}/responsiblities-and-authorities",
    response_model=List[QPResponsiblityAndAuthority],
    status_code=status.HTTP_200_OK
)
def get_all_drrrf_responsibility_and_authority(drrrf_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_drrrf_responsibility_and_authority(db, drrrf_id)

#CREATE RESPONSIBILITIES AND AUTHORITIES
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/responsibilities-and-authorities",
    response_model=QPResponsiblityAndAuthority,
    status_code=status.HTTP_201_CREATED
)
def create_responsibility_and_authority(drrrf_id: int, responsibility_and_authority: QPResponsiblityAndAuthorityCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_responsibility_and_authority(db, responsibility_and_authority, drrrf_id)

#GET ALL PROCEDURE
@quality_procedure_router.get(
    "/quality-procedures/procedures",
    response_model=List[QPProcedure],
    status_code=status.HTTP_200_OK
)
def get_all_procedure(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_procedure(db)

#CREATE PROCEDURE
@quality_procedure_router.get(
    "/quality-procedures/{drrrf_id}/procedures",
    response_model=List[QPProcedure],
    status_code=status.HTTP_200_OK
)
def get_drrrf_procedures(drrrf_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_drrrf_procedures(db, drrrf_id)

#CREATE PROCEDURE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/procedures",
    response_model=QPProcedure,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(drrrf_id: int, procedure: QPProcedureCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_procedure(db, procedure, drrrf_id)

#GET ALL PROCESS
@quality_procedure_router.get(
    "/quality-procedures/processes",
    response_model=List[QPProcess],
    status_code=status.HTTP_200_OK
)
def get_all_process(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process(db)

#CREATE PROCESS
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/procedures/{procedure_id}/processes",
    response_model=QPProcess,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(drrrf_id: int, procedure_id: int, process: QPProcessCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process(db, process, drrrf_id, procedure_id)

#GET ALL PROCESS NOTE
@quality_procedure_router.get(
    "/quality-procedures/process-notes",
    response_model=List[QPProcessNote],
    status_code=status.HTTP_200_OK
)
def get_all_process_note(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process_note(db)

#CREATE PROCESS NOTE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/processes/{process_id}/process-notes",
    response_model=QPProcessNote,
    status_code=status.HTTP_201_CREATED
)
def create_process_note(drrrf_id: int, process_id: int, process_note: QPProcessNoteCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_note(db, process_note, drrrf_id, process_id)

#GET ALL PROCESS IN-CHARGE
@quality_procedure_router.get(
    "/quality-procedures/process-in-charge",
    response_model=List[QPProcessInCharge],
    status_code=status.HTTP_200_OK
)
def get_all_process_in_charge(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process_in_charge(db)

#CREATE PROCESS IN-CHARGE
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/processes/{process_id}/process-in-charge",
    response_model=QPProcessInCharge,
    status_code=status.HTTP_201_CREATED
)
def create_process_in_charge(drrrf_id: int, process_id: int, process_in_charge: QPProcessInChargeCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_in_charge(db, process_in_charge, drrrf_id, process_id)

#GET ALL PROCESS RECORD
@quality_procedure_router.get(
    "/quality-procedures/process-records",
    response_model=List[QPProcessRecord],
    status_code=status.HTTP_200_OK
)
def get_all_process_record(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process_record(db)

#GET ALL PROCESS PROCESS RECORD
@quality_procedure_router.get(
    "/quality-procedures/{process_id}/process-records",
    response_model=List[QPProcessRecord],
    status_code=status.HTTP_200_OK
)
def get_all_process_process_record(process_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process_process_record(db, process_id)

#CREATE PROCESS RECORD
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/processes/{process_id}/process-records",
    response_model=QPProcessRecord,
    status_code=status.HTTP_201_CREATED
)
def create_process_record(drrrf_id: int, process_id: int, process_record: QPProcessRecordCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_record(db, process_record, drrrf_id, process_id)

#GET ALL PROCESS REPORT
@quality_procedure_router.get(
    "/quality-procedures/process-reports",
    response_model=List[QPReport],
    status_code=status.HTTP_200_OK
)
def get_all_report(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_report(db)

#CREATE PROCESS REPORT
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/process-reports",
    response_model=QPReport,
    status_code=status.HTTP_201_CREATED
)
def create_report(drrrf_id: int, report: QPReportCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_report(db, report, drrrf_id)

#GET ALL PERFORMANCE INDICATORS
@quality_procedure_router.get(
    "/quality-procedures/performance-indicators",
    response_model=List[QPPerformanceIndicator],
    status_code=status.HTTP_200_OK
)
def get_all_performance_indicator(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_performance_indicator(db)

#CREATE PROCESS REPORT
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/performance-indicators",
    response_model=QPPerformanceIndicator,
    status_code=status.HTTP_201_CREATED
)
def create_performance_indicator(drrrf_id: int, performance_indicator: QPPerformanceIndicatorCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_performance_indicator(db, performance_indicator, drrrf_id)

#GET ALL ATTACHMENT AND FORM
@quality_procedure_router.get(
    "/quality-procedures/attachments-and-forms",
    response_model=List[QPAttachmentAndForm],
    status_code=status.HTTP_200_OK
)
def get_all_attachment_and_form(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_attachment_and_form(db)

#GET ALL DRRRF ATTACHMENT AND FORM
@quality_procedure_router.get(
    "/quality-procedures/{drrrf_id}/attachments-and-forms",
    response_model=List[QPAttachmentAndForm],
    status_code=status.HTTP_200_OK
)
def get_all_drrrf_attachment_and_form(drrrf_id: int, db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_drrrf_attachment_and_form(db, drrrf_id)

#CREATE ATTACHMENT AND FORM
@quality_procedure_router.post(
    "/quality-procedures/{drrrf_id}/attachments-and-forms",
    response_model=QPAttachmentAndForm,
    status_code=status.HTTP_201_CREATED
)
def create_attachment_and_form(drrrf_id: int, attachment_and_form: QPAttachmentAndFormCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_attachment_and_form(db, attachment_and_form, drrrf_id)

#GET ALL STATUS
@quality_procedure_router.get(
    "/status",
    response_model=List[Status],
    status_code=status.HTTP_200_OK
)
def get_all_status(db: Session = Depends(get_db)):
    return StatusManager.get_all_status(db)

#CREATE STATUS
@quality_procedure_router.post(
    "/status",
    response_model=Status,
    status_code=status.HTTP_201_CREATED
)
def create_status(status: StatusCreate, db: Session = Depends(get_db)):
    return StatusManager.create_status(db, status)

#GET ALL DISTRIBUTION LIST
@quality_procedure_router.get(
    "/distributions-list",
    response_model=List[DistributionList],
    status_code=status.HTTP_200_OK
)
def get_all_distribution_list(db: Session = Depends(get_db)):
    return DistributionListManager.get_all_distribution_list(db)

#GET ALL DRRRF DISTRIBUTION LIST
@quality_procedure_router.get(
    "/drrrfs/{drrrf_id}/distributions-list",
    response_model=List[DistributionList],
    status_code=status.HTTP_200_OK
)
def get_all_drrrf_distribution_list(drrrf_id: int, db: Session = Depends(get_db)):
    return DistributionListManager.get_all_drrrf_distribution_list(db, drrrf_id)

#CREATE DISTRIBUTION LIST
@quality_procedure_router.post(
    "/distributions-list",
    response_model=DistributionList,
    status_code=status.HTTP_201_CREATED
)
def create_distribution_list(distribution_list: DistributionListCreate, db: Session = Depends(get_db)):
    return DistributionListManager.create_distribution_list(db, distribution_list)