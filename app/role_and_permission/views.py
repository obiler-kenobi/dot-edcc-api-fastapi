from typing import List
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.role_and_permission.schemas import Role, RoleCreate, RoleGroup, RoleGroupCreate, Permission, PermissionCreate, UserAccess, UserAccessCreate, UserCustomAccess, UserCustomAccessCreate
from app.role_and_permission.services import RoleManager, PermissionManager, AccessManager

from app.deps import get_db

role_and_permission_router = APIRouter()

#GET ALL ROLES
@role_and_permission_router.get(
    "/roles",
    response_model=List[Role],
    status_code=status.HTTP_200_OK
)
def get_all_roles(db: Session = Depends(get_db)):
    return RoleManager.get_all_roles(db)

#CREATE ROLE
@role_and_permission_router.post(
    "/roles",
    response_model=Role,
    status_code=status.HTTP_201_CREATED
)
def  create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return RoleManager.create_role(db, role)

#GET ALL ROLE GROUP 
@role_and_permission_router.get(
    "/role-groups",
    response_model=List[RoleGroup],
    status_code=status.HTTP_200_OK
)
def get_all_role_groups(db: Session = Depends(get_db)):
    return RoleManager.get_all_role_groups(db)

#CREATE ROLE GROUP
@role_and_permission_router.post(
    "/role-groups",
    response_model=RoleGroup,
    status_code=status.HTTP_201_CREATED
)
def create_role_group(role_group: RoleGroupCreate, db: Session = Depends(get_db)):
    return RoleManager.create_role_group(db, role_group)

#GET ALL PERMISSIONS
@role_and_permission_router.get(
    "/permissions",
    response_model=List[Permission],
    status_code=status.HTTP_200_OK
)
def get_all_permissions(db: Session = Depends(get_db)):
    return PermissionManager.get_all_permissions(db)

#CREATE PERMISSION
@role_and_permission_router.post(
    "/permissions",
    response_model=Permission,
    status_code=status.HTTP_201_CREATED
)
def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    return PermissionManager.create_permission(db, permission)

#GET ALL USER ACCESS
@role_and_permission_router.get(
    "/user-access",
    response_model=List[UserAccess],
    status_code=status.HTTP_200_OK
)
def get_all_user_access(db: Session = Depends(get_db)):
    return AccessManager.get_all_user_access(db)

#CREATE USER ACCESS
@role_and_permission_router.post(
    "/user-access",
    response_model=UserAccess,
    status_code=status.HTTP_201_CREATED
)
def create_user_access(user_access: UserAccessCreate, db: Session = Depends(get_db)):
    return AccessManager.create_user_access(db, user_access)

#GET ALL CUSTOM ACCESS
@role_and_permission_router.get(
    "/user-custom-access",
    response_model=List[UserCustomAccess],
    status_code=status.HTTP_200_OK
)
def get_all_user_custom_access(db: Session = Depends(get_db)):
    return AccessManager.get_all_user_custom_access(db)

#CREATE CUSTOM ACCESS
@role_and_permission_router.post(
    "/user-custom-access",
    response_model=UserCustomAccess,
    status_code=status.HTTP_201_CREATED
)
def create_user_custom_access(user_custom_access: UserCustomAccessCreate, db: Session = Depends(get_db)):
    return AccessManager.create_user_custom_access(db, user_custom_access)