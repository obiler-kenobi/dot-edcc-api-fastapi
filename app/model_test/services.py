import time
timestr = time.strftime("%Y%m%d-%H%M%S")

import os
from pathlib import Path
import shutil

from app.model_test import models
from app.model_test.schemas import SampleCreate

from sqlalchemy.orm import Session

from fastapi import UploadFile, File

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = Path(BASE_DIR).parent
REFERENCE_UPLOAD_DIR = os.path.join(PROJECT_DIR, "uploads/reference_documents")

class SampleManager(object): 
    @staticmethod
    def get_all_samples(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Sample).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_sample(db: Session, id: int):
        return db.query(models.Sample).filter(models.Sample.id == id).first()
    
    @staticmethod
    def create_sample(db: Session, sample: SampleCreate):
        new_sample = models.Sample(**sample.dict())

        db.add(new_sample)
        db.commit()
        return new_sample

    @staticmethod
    def upload_file(uploaded: UploadFile = File(...)):
        
        FILE_EXTENSION = os.path.splitext(uploaded.filename)
        NEW_FILE_NAME = "sample_" + timestr + FILE_EXTENSION[1]
        UPLOADED_FILE = os.path.join(REFERENCE_UPLOAD_DIR, NEW_FILE_NAME)

        with open(UPLOADED_FILE, "wb") as buffer:
            shutil.copyfileobj(uploaded.file, buffer)
        
        return UPLOADED_FILE
        