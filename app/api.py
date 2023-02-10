from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.models import ErrorModel
from app.office.views import office_router
from app.designation.views import designation_router
from app.user.views import user_router
from app.role_and_permission.views import role_and_permission_router
from app.quality_procedure.views import quality_procedure_router

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
