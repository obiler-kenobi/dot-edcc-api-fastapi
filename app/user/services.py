from app.user import models
from app.auth.services import get_password_hash

from sqlalchemy.orm import Session

from app.user.schemas import UserBasicInformationCreate, UserOfficeInformationCreate, UsersCreate

class UserManager(object):
    @staticmethod
    def get_all_users_basic_information(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserBasicInformation).offset(skip).limit(limit).all()

    @staticmethod
    def create_user_basic_information(db: Session, user_basic_information: UserBasicInformationCreate):
        new_user_basic_information = models.UserBasicInformation(**user_basic_information.dict())

        db.add(new_user_basic_information)
        db.commit()
        return new_user_basic_information

    @staticmethod
    def get_all_users_office_information(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserOfficeInformation).offset(skip).limit(limit).all()

    @staticmethod
    def create_user_office_information(db: Session, user_office_information: UserOfficeInformationCreate):
        new_user_office_information = models.UserOfficeInformation(**user_office_information.dict())

        db.add(new_user_office_information)
        db.commit()
        return new_user_office_information

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Users).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user_account: UsersCreate):
        new_user = models.Users(**user_account.dict())

        new_user.hashed_password = get_password_hash(new_user.hashed_password)

        db.add(new_user)
        db.commit()
        return new_user