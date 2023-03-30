from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.model_test.schemas import Sample, SampleCreate
from app.model_test.services import SampleManager

from app.deps import get_db

sample_router = APIRouter()

#GET ALL STATUS
@sample_router.get(
    "/samples",
    response_model=List[Sample],
    status_code=status.HTTP_200_OK
)
def get_all_sample(db: Session = Depends(get_db)):
    return SampleManager.get_all_samples(db)

#GET ALL STATUS
@sample_router.get(
    "/samples/{id}",
    response_model=Sample,
    status_code=status.HTTP_200_OK
)
def get_sample(id: int, db: Session = Depends(get_db)):
    return SampleManager.get_sample(db, id)

#CREATE STATUS
@sample_router.post(
    "/samples",
    response_model=Sample,
    status_code=status.HTTP_201_CREATED
)
def create_sample(sample: SampleCreate, db: Session = Depends(get_db)):
    return SampleManager.create_sample(db, sample)