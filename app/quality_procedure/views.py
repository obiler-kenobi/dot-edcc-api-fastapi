from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.schemas import (QualityProcedureDocumentRequest, QualityProcedureDocumentRequestCreate, QPRequestHistory, QPRequestHistoryCreate) #QP REQUESTS
from app.quality_procedure.schemas import DRRRF, DRRRFCreate, InterfacingUnit, InterfacingUnitCreate, IUReviewSummary, IUReviewSummaryCreate
from app.quality_procedure.services import QualityProcedureDocumentRequestManager, DRRRFManager
from app.quality_procedure.schemas import QPTitlePage, QPTitlePageCreate, QPObjective, QPObjectiveCreate, QPScope, QPScopeCreate, QPDefinitionOfTerm, QPDefinitionOfTermCreate, QPReferenceDocument, QPReferenceDocumentCreate, QPResponsiblityAndAuthority, QPResponsiblityAndAuthorityCreate, QPProcedure, QPProcedureCreate, QPProcess, QPProcessCreate, QPProcessInCharge, QPProcessInChargeCreate, QPProcessNote, QPProcessNoteCreate, QPProcessRecord, QPProcessRecordCreate, QPReport, QPReportCreate, QPPerformanceIndicator, QPPerformanceIndicatorCreate, QPAttachmentAndForm, QPAttachmentAndFormCreate
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
    response_model=List[QPTitlePage],
    status_code=status.HTTP_200_OK
)
def get_all_title_page(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_title_page(db)

#CREATE IU REVIEW SUMMARY
@quality_procedure_router.post(
    "/quality-procedures/title-pages",
    response_model=QPTitlePage,
    status_code=status.HTTP_201_CREATED
)
def create_title_page(title_page: QPTitlePageCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_title_page(db, title_page)

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
    "/quality-procedures/objectives",
    response_model=QPObjective,
    status_code=status.HTTP_201_CREATED
)
def create_objective(objective: QPObjectiveCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_objective(db, objective)

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
    "/quality-procedures/scopes",
    response_model=QPScope,
    status_code=status.HTTP_201_CREATED
)
def create_scope(scope: QPScopeCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_scope(db, scope)

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
    "/quality-procedures/reference-documents",
    response_model=QPReferenceDocument,
    status_code=status.HTTP_201_CREATED
)
def create_definition_of_term(reference_document: QPReferenceDocumentCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_reference_document(db, reference_document)

#GET ALL RESPONSIBLITY AND AUTHORITY
@quality_procedure_router.get(
    "/quality-procedures/responsiblities-and-authorities",
    response_model=List[QPResponsiblityAndAuthority],
    status_code=status.HTTP_200_OK
)
def get_all_responsibility_and_authority(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_responsibility_and_authority(db)

#CREATE REFERENCE DOCUMENT
@quality_procedure_router.post(
    "/quality-procedures/responsiblities-and-authorities",
    response_model=QPResponsiblityAndAuthority,
    status_code=status.HTTP_201_CREATED
)
def create_responsibility_and_authority(responsibility_and_authority: QPResponsiblityAndAuthorityCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_responsibility_and_authority(db, responsibility_and_authority)

#GET ALL PROCEDURE
@quality_procedure_router.get(
    "/quality-procedures/procedures",
    response_model=List[QPProcedure],
    status_code=status.HTTP_200_OK
)
def get_all_procedure(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_procedure(db)

#CREATE PROCEDURE
@quality_procedure_router.post(
    "/quality-procedures/procedures",
    response_model=QPProcedure,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(procedure: QPProcedureCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_procedure(db, procedure)

#GET ALL PROCESS
@quality_procedure_router.get(
    "/quality-procedures/process",
    response_model=List[QPProcess],
    status_code=status.HTTP_200_OK
)
def get_all_process(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process(db)

#CREATE PROCESS
@quality_procedure_router.post(
    "/quality-procedures/process",
    response_model=QPProcess,
    status_code=status.HTTP_201_CREATED
)
def create_procedure(process: QPProcessCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process(db, process)

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
    "/quality-procedures/process-notes",
    response_model=QPProcessNote,
    status_code=status.HTTP_201_CREATED
)
def create_process_note(process_note: QPProcessNoteCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_note(db, process_note)

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
    "/quality-procedures/process-in-charge",
    response_model=QPProcessInCharge,
    status_code=status.HTTP_201_CREATED
)
def create_process_in_charge(process_in_charge: QPProcessInChargeCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_in_charge(db, process_in_charge)

#GET ALL PROCESS RECORD
@quality_procedure_router.get(
    "/quality-procedures/process-records",
    response_model=List[QPProcessRecord],
    status_code=status.HTTP_200_OK
)
def get_all_process_record(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_process_record(db)

#CREATE PROCESS RECORD
@quality_procedure_router.post(
    "/quality-procedures/process-records",
    response_model=QPProcessRecord,
    status_code=status.HTTP_201_CREATED
)
def create_process_record(process_record: QPProcessRecordCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_process_record(db, process_record)

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
    "/quality-procedures/process-reports",
    response_model=QPReport,
    status_code=status.HTTP_201_CREATED
)
def create_report(report: QPReportCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_report(db, report)

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
    "/quality-procedures/performance-indicators",
    response_model=QPPerformanceIndicator,
    status_code=status.HTTP_201_CREATED
)
def create_performance_indicator(performance_indicator: QPPerformanceIndicatorCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_performance_indicator(db, performance_indicator)

#GET ALL ATTACHMENT AND FORM
@quality_procedure_router.get(
    "/quality-procedures/attachments-and-forms",
    response_model=List[QPAttachmentAndForm],
    status_code=status.HTTP_200_OK
)
def get_all_attachment_and_form(db: Session = Depends(get_db)):
    return QualityProcedureManager.get_all_attachment_and_form(db)

#CREATE ATTACHMENT AND FORM
@quality_procedure_router.post(
    "/quality-procedures/attachments-and-forms",
    response_model=QPAttachmentAndForm,
    status_code=status.HTTP_201_CREATED
)
def create_attachment_and_form(attachment_and_form: QPAttachmentAndFormCreate, db: Session = Depends(get_db)):
    return QualityProcedureManager.create_attachment_and_form(db, attachment_and_form)