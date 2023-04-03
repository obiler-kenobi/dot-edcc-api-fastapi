from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.models import ErrorModel
from app.office.views import office_router
from app.designation.views import designation_router
from app.user.views import user_router
from app.role_and_permission.views import role_and_permission_router
from app.quality_procedure.views import quality_procedure_router
from app.qms_team.views import qms_team_router
from app.quality_procedure.status.views import status_router
from app.quality_procedure.requests.views import quality_procedure_requests_router
from app.model_test.views import sample_router
from app.quality_procedure.content.views import quality_procedure_content_router

api_router = APIRouter(default_response_class=ORJSONResponse)

#SETTINGS/OFFICE
api_router.include_router(
    office_router,
    prefix="",
    tags=["offices"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

#SETTINGS/DESIGNATION
api_router.include_router(
    designation_router,
    prefix="",
    tags=["designation"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

#USERS
api_router.include_router(
    user_router,
    prefix="/users",
    tags=["users"],
    responses={401: {"model": ErrorModel}, 403: {"model":ErrorModel}}
)

#SETTINGS/ROLES AND PERMISSIONS
api_router.include_router(
    role_and_permission_router,
    prefix="",
    tags=["role-and-permission"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

#QUALITY PROCEDURES
api_router.include_router(
    quality_procedure_router,
    prefix="",
    tags=['quality-procedures'],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

#QMS TEAM
api_router.include_router(
    qms_team_router,
    prefix="",
    tags=["qms-team"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

#QUALITY PROCEDURE STATUS   
api_router.include_router(
    status_router,
    prefix="/quality-procedures",
    tags=["status"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

api_router.include_router(
    quality_procedure_requests_router,
    prefix="/quality-procedures",
    tags=["requests"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

api_router.include_router(
    sample_router,
    prefix="/sample-models",
    tags=["sample-models"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

api_router.include_router(
    quality_procedure_content_router,
    prefix="/quality-procedures",
    tags=["content"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)