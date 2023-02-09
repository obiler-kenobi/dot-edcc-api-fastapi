from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.models import ErrorModel
from app.office.views import office_router
from app.designation.views import designation_router
from app.user.views import user_router
from app.role_and_permission.views import role_and_permission_router

api_router = APIRouter(default_response_class=ORJSONResponse)

api_router.include_router(
    office_router,
    prefix="",
    tags=["offices"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

api_router.include_router(
    designation_router,
    prefix="",
    tags=["designation"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)

api_router.include_router(
    user_router,
    prefix="/users",
    tags=["users"],
    responses={401: {"model": ErrorModel}, 403: {"model":ErrorModel}}
)

api_router.include_router(
    role_and_permission_router,
    prefix="",
    tags=["role-and-permission"],
    responses={401: {"model": ErrorModel}, 403: {"model": ErrorModel}}
)