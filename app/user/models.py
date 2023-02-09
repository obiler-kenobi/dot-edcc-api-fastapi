from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class UserBasicInformation(Base):
    __tablename__ = "user_basic_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String(100), nullable=False)
    middle_initial = Column(String(5), nullable=True)
    last_name = Column(String(100), nullable=False)
    employee_id = Column(Integer, nullable=True)
    sex = Column(String(6), nullable=False)
    age = Column(Integer, nullable=False)
    contact_number = Column(String(17), nullable=True)
    alternate_contact_number = Column(String(17), nullable=True)
    alternate_email_address = Column(String(70), nullable=True)
    designation = Column(Integer, nullable=False)
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)

    users = relationship("Users", back_populates="user_basic_information")
    user_office_information = relationship("UserOfficeInformation", back_populates="user_basic_information")

class UserOfficeInformation(Base):
    __tablename__ = "user_office_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_basic_information_id = Column(Integer,ForeignKey("user_basic_information.id"))
    dot_main_office_id = Column(Integer, ForeignKey("dot_main_office.id"))
    dot_sector_id = Column(Integer, ForeignKey("dot_sector.id"))
    dot_sub_sector_id = Column(Integer, ForeignKey("dot_sub_sector.id"))
    dot_office_id = Column(Integer, ForeignKey("dot_office.id"))
    dot_division_id = Column(Integer, ForeignKey("dot_division.id"))
    dot_unit_id = Column(Integer, ForeignKey("dot_unit.id"))
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)

    user_basic_information = relationship("UserBasicInformation", back_populates="user_office_information")
    dot_main_office = relationship("DOTMainOffice", back_populates="user_office_information")
    dot_sector = relationship("DOTSector", back_populates="user_office_information")
    dot_sub_sector = relationship("DOTSubSector", back_populates="user_office_information")
    dot_office = relationship("DOTOffice", back_populates="user_office_information")
    dot_division = relationship("DOTDivision", back_populates="user_office_information")
    dot_unit = relationship("DOTUnit", back_populates="user_office_information")

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(40), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    primary_email_address = Column(String(40), nullable=False)
    role = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    encoded_date = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(40), nullable=False)

    user_basic_information = relationship("UserBasicInformation", back_populates="users")


