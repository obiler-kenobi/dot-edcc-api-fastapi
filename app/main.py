from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.database import engine
from app.api import api_router

from app.office import models as offices_models
from app.designation import models as designation_models
from app.user import models as user_models
from app.role_and_permission import models as role_and_permission_models
from app.quality_procedure import models as quality_procedure_models

app = FastAPI()

offices_models.Base.metadata.create_all(bind=engine)
designation_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)
role_and_permission_models.Base.metadata.create_all(bind=engine)
quality_procedure_models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)