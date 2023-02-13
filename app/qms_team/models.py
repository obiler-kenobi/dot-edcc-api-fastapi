from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class ISOFacilitator(Base):
    __tablename__ = "iso_facilitator"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)

class DISOFacilitator(Base):
    __tablename__ = "diso_facilitator" #Deputy ISO Facilitator

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    office_handled = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)

class HeadOfOffice(Base):
    __tablename__ = "head_of_office" #Directors and Regional Directors

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    office_handled = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)