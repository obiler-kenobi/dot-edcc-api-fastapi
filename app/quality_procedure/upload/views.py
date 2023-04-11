from fastapi import APIRouter, status

from app.quality_procedure.upload.services import UploadManager

from fastapi import UploadFile, Form

upload_router = APIRouter()

#UPLOAD FILE
@upload_router.post(
    "",
    status_code=status.HTTP_200_OK
    )
def upload_file(uploaded: UploadFile, filename: str = Form()):
    return UploadManager.upload_file(uploaded, filename)