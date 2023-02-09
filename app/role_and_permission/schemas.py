from datetime import datetime
from pydantic import BaseModel

class RoleBase(BaseModel):
    role: str
    role_description: str
    tag: str
    slug: str
    fixed: bool
    encoded_date: datetime
    encoded_by: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class PermissionBase(BaseModel):
    permission: str
    permission_description: str
    tag: str
    slug: str
    encoded_date: datetime
    encoded_by: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True

class UserAccessBase(BaseModel):
    tag: str
    access_view: bool = False
    access_create: bool = False
    access_update: bool = False
    access_delete: bool = False
    access_disable: bool = False
    access_review: bool = False
    access_comment: bool = False
    access_approve: bool = False
    encoded_date: datetime
    encoded_by: str

class UserAccessCreate(UserAccessBase):
    role_id: int
    permission_id: int

class UserAccess(UserAccessBase):
    id: int

    class Config:
        orm_mode = True

class UserCustomAccessBase(BaseModel):
    tag: str
    access_view: bool = False
    access_create: bool = False
    access_update: bool = False
    access_delete: bool = False
    access_disable: bool = False
    access_review: bool = False
    access_comment: bool = False
    access_approve: bool = False
    encoded_date: datetime
    encoded_by: str

class UserCustomAccessCreate(UserCustomAccessBase):
    user_id: int
    permission_id: int

class UserCustomAccess(UserCustomAccessBase):
    id: int

    class Config:
        orm_mode = True



