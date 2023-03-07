from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.quality_procedure.status.schemas import StatusBase, StatusActionsBase, Status, StatusActions
from app.quality_procedure.status.services import StatusManager, StatusActionsManager

from app.deps import get_db

status_router = APIRouter()

#GET ALL STATUS
@status_router.get(
    "/status",
    response_model=List[Status],
    status_code=status.HTTP_200_OK
)
def get_all_status(db: Session = Depends(get_db)):
    return StatusManager.get_all_status(db)

#CREATE STATUS
@status_router.post(
    "/status",
    response_model=Status,
    status_code=status.HTTP_201_CREATED
)
def create_status(status: StatusBase, db: Session = Depends(get_db)):
    return StatusManager.create_status(db, status)

#GET ALL STATUS ACTIONS
@status_router.get(
    "/status-actions",
    response_model=List[StatusActions],
    status_code=status.HTTP_200_OK
)
def get_all_status_actions(db: Session = Depends(get_db)):
    return StatusActionsManager.get_all_status_actions(db)

@status_router.post(
    "/status-actions",
    response_model=StatusActions,
    status_code=status.HTTP_201_CREATED
)
def create_status_actions(status_action: StatusActionsBase, db: Session = Depends(get_db)):
    return StatusActionsManager.create_status_actions(db, status_action)