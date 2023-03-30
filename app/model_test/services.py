from app.model_test import models

from app.model_test.schemas import SampleCreate

from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

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