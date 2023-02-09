from app.role_and_permission import models
from app.role_and_permission.schemas import RoleCreate, PermissionCreate, UserAccessCreate, UserCustomAccessCreate

from sqlalchemy.orm import Session

class RoleManager(object):
    @staticmethod
    def get_all_roles(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Role).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_role(db: Session, role: RoleCreate):
        new_role = models.Role(**role.dict())

        db.add(new_role)
        db.commit()
        return new_role
    
class PermissionManager(object):
    @staticmethod
    def get_all_permissions(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Permission).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_permission(db: Session, permission: PermissionCreate):
        new_permission = models.Permission(**permission.dict())

        db.add(new_permission)
        db.commit()
        return new_permission
    
class AccessManager(object):
    @staticmethod
    def get_all_user_access(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserAccess).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_user_access(db: Session, user_access: UserAccessCreate):
        new_user_access = models.UserAccess(**user_access.dict())

        db.add(new_user_access)
        db.commit()
        return new_user_access
    
    @staticmethod
    def get_all_user_custom_access(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserCustomAccess).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_user_custom_access(db: Session, user_custom_access: UserCustomAccessCreate):
        new_user_custom_access = models.UserCustomAccess(**user_custom_access.dict())

        db.add(new_user_custom_access)
        db.commit()
        return new_user_custom_access