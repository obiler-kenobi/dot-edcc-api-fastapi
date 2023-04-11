import time
timestr = time.strftime("%Y%m%d_%H%M%S")

import os
from pathlib import Path
import shutil

from app.model_test import models
from app.model_test.schemas import SampleCreate

from sqlalchemy.orm import Session

from fastapi import UploadFile, File, Form

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = Path(BASE_DIR).parent.parent
REFERENCE_DOCUMENT = "uploads/reference_documents"
REFERENCE_UPLOAD_DIR = os.path.join(PROJECT_DIR, REFERENCE_DOCUMENT)

class UploadManager(object): 
    @staticmethod
    def upload_file(uploaded: UploadFile = File(...), filename: str = Form()):
        FILE_EXTENSION = os.path.splitext(uploaded.filename)
        NEW_FILE_NAME = filename + "_" + timestr + FILE_EXTENSION[1]
        UPLOADED_FILE = os.path.join(REFERENCE_UPLOAD_DIR, NEW_FILE_NAME)
        PATH = "/" + os.path.join(REFERENCE_DOCUMENT, NEW_FILE_NAME)
        

        with open(UPLOADED_FILE, "wb") as buffer:
            shutil.copyfileobj(uploaded.file, buffer)
        
        return {"path": PATH}
        