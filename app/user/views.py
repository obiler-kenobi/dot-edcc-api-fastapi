from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.user.schemas import UserBasicInformation, UserBasicInformationCreate, UserOfficeInformation, UserOfficeInformationCreate, User, UserCreate, ProcessOwner
from app.user.services import UserManager
from app.deps import get_db

user_router = APIRouter()

#GET ALL USER BASIC INFORMATION
@user_router.get(
    "/basic-information",
    response_model=List[UserBasicInformation],
    status_code=status.HTTP_200_OK
)
def get_all_users_basic_information(db: Session = Depends(get_db)):
    return UserManager.get_all_users_basic_information(db)

#CREATE USER BASIC INFORMATION
@user_router.post(
    "/basic-information",
    response_model=UserBasicInformation,
    status_code=status.HTTP_201_CREATED
)
def create_user_basic_information(user_basic_information: UserBasicInformationCreate, db: Session = Depends(get_db)):
    return UserManager.create_user_basic_information(db, user_basic_information)

#GET ALL USER OFFICE INFORMATION
@user_router.get(
    "/office-information",
    response_model=List[UserOfficeInformation],
    status_code=status.HTTP_200_OK
)
def get_all_users_office_information(db: Session = Depends(get_db)):
    return UserManager.get_all_users_office_information(db)

#CREATE USER OFFICE INFORMATION
@user_router.post(
    "/office-information",
    response_model=UserOfficeInformation,
    status_code=status.HTTP_201_CREATED
)
def create_user_office_information(user_office_information: UserOfficeInformationCreate, db: Session = Depends(get_db)):
    return UserManager.create_user_office_information(db, user_office_information)

#GET ALL USER ACCOUNT
@user_router.get(
    "",
    response_model=List[User],
    status_code=status.HTTP_200_OK
)
def get_all_users_account(db: Session = Depends(get_db)):
    return UserManager.get_all_users(db)

#CREATE NEW USER ACCOUNT
@user_router.post(
    "",
    response_model=User,
    status_code=status.HTTP_201_CREATED
)
def create_user_account(user_account: UserCreate, db: Session = Depends(get_db)):
    return UserManager.create_user(db, user_account)
