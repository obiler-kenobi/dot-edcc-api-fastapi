from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_jwt_auth import AuthJWT

from app.auth.config import Settings

from app.database import engine
from app.api import api_router

from app.office import models as offices_models
from app.designation import models as designation_models
from app.user import models as user_models
from app.role_and_permission import models as role_and_permission_models
from app.quality_procedure import models as quality_procedure_models
from app.quality_procedure.status import models as quality_procedure_status_models
from app.qms_team import models as qms_team_models
from app.model_test import models as model_test_models


app = FastAPI()

offices_models.Base.metadata.create_all(bind=engine)
designation_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)
role_and_permission_models.Base.metadata.create_all(bind=engine)
quality_procedure_models.Base.metadata.create_all(bind=engine)
quality_procedure_status_models.Base.metadata.create_all(bind=engine)
qms_team_models.Base.metadata.create_all(bind=engine)
model_test_models.Base.metadata.create_all(bind=engine)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)

app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@AuthJWT.load_config
def get_config():
    return Settings()