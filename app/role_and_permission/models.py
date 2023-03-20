from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role = Column(String(70), nullable=False)
    role_description = Column(String(200), nullable=False)
    role_group_id = Column(Integer, ForeignKey("role_group.id"))
    tag = Column(String(80), nullable=False)
    slug = Column(String(80), nullable=False)
    fixed = Column(Boolean, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    created_by = Column(String(40), nullable=False)

    role_group = relationship("RoleGroup", back_populates="role")

class RoleGroup(Base):
    __tablename__ = "role_group"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_title = Column(String(70), nullable=False)
    group_description = Column(String(200), nullable=False)
    slug = Column(String(80), nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)
    created_by = Column(String(40), nullable=False)

    role = relationship("Role", back_populates="role_group")

class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    permission = Column(String(70), nullable=False)
    permission_description = Column(String(100), nullable=False)
    tag = Column(String(80), nullable=False)
    slug = Column(String(80), nullable=False)
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)

class UserAccess(Base):
    __tablename__ = "user_access"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)
    tag = Column(String(150), unique=True, nullable=False)
    access_view = Column(Boolean, default=False)
    access_create = Column(Boolean, default=False)
    access_update = Column(Boolean, default=False)
    access_delete = Column(Boolean, default=False)
    access_disable = Column(Boolean, default=False)
    access_review = Column(Boolean, default=False)
    access_comment = Column(Boolean, default=False)
    access_approve = Column(Boolean, default=False)
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)

class UserCustomAccess(Base):
    __tablename__ = "user_custom_access"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)
    tag = Column(String(150), unique=True, nullable=False)
    access_view = Column(Boolean, default=False)
    access_create = Column(Boolean, default=False)
    access_update = Column(Boolean, default=False)
    access_delete = Column(Boolean, default=False)
    access_disable = Column(Boolean, default=False)
    access_review = Column(Boolean, default=False)
    access_comment = Column(Boolean, default=False)
    access_approve = Column(Boolean, default=False)
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)
