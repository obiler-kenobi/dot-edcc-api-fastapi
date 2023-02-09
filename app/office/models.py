from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class DOTMainOffice(Base):
    __tablename__ = "dot_main_office"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    main_office_name = Column(String(100), nullable=False)
    short_main_office_name = Column(String(30), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_sector = relationship("DOTSector", back_populates="dot_main_office")
    dot_office = relationship("DOTOffice", back_populates="dot_main_office")
    dot_unit = relationship("DOTUnit", back_populates='dot_main_office')
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_main_office")

class DOTSector(Base):
    __tablename__ = "dot_sector"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dot_main_office_id = Column(Integer, ForeignKey("dot_main_office.id"))
    sector_name = Column(String(100), nullable=False)
    short_sector_name = Column(String(30), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_main_office = relationship("DOTMainOffice", back_populates="dot_sector")
    dot_sub_sector = relationship("DOTSubSector", back_populates="dot_sector")
    dot_office = relationship("DOTOffice", back_populates="dot_sector")
    dot_unit = relationship("DOTUnit", back_populates='dot_sector')
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_sector")

class DOTSubSector(Base):
    __tablename__ = "dot_sub_sector"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dot_sector_id = Column(Integer, ForeignKey("dot_sector.id"))
    sub_sector_name = Column(String(100), nullable=False)
    short_sub_sector_name = Column(String(30), nullable=False)
    slug = Column(String(100), nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_sector = relationship("DOTSector", back_populates="dot_sub_sector") 
    dot_office = relationship("DOTOffice", back_populates="dot_sub_sector")
    dot_unit = relationship("DOTUnit", back_populates='dot_sub_sector')
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_sub_sector")

class DOTOffice(Base):
    __tablename__ = "dot_office"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dot_main_office_id = Column(Integer, ForeignKey("dot_main_office.id"))
    dot_sector_id = Column(Integer, ForeignKey("dot_sector.id"))
    dot_sub_sector_id = Column(Integer, ForeignKey("dot_sub_sector.id"))
    office_name = Column(String(100), nullable=False)
    short_office_name = Column(String(30), nullable=False)
    slug = Column(String(100), nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_main_office = relationship("DOTMainOffice", back_populates="dot_office")
    dot_sector = relationship("DOTSector", back_populates="dot_office")
    dot_sub_sector = relationship("DOTSubSector", back_populates="dot_office")
    dot_division = relationship("DOTDivision", back_populates="dot_office")
    dot_unit = relationship("DOTUnit", back_populates='dot_office')
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_office")

class DOTDivision(Base):
    __tablename__ = "dot_division"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dot_office_id = Column(Integer, ForeignKey("dot_office.id"))
    division_name = Column(String(100), nullable=False)
    short_division_name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_office = relationship("DOTOffice", back_populates="dot_division")
    dot_unit = relationship("DOTUnit", back_populates='dot_division')
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_division")

class DOTUnit(Base):
    __tablename__ = "dot_unit"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dot_main_office_id = Column(Integer, ForeignKey("dot_main_office.id"))
    dot_sector_id = Column(Integer, ForeignKey("dot_sector.id"))
    dot_sub_sector_id = Column(Integer, ForeignKey("dot_sub_sector.id"))
    dot_division_id = Column(Integer, ForeignKey("dot_division.id"))
    dot_office_id = Column(Integer, ForeignKey("dot_office.id"))
    unit_name = Column(String(100), nullable=False)
    short_unit_name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)

    dot_main_office = relationship("DOTMainOffice", back_populates="dot_unit")
    dot_sector = relationship("DOTSector", back_populates="dot_unit")
    dot_sub_sector = relationship("DOTSubSector", back_populates="dot_unit")
    dot_division = relationship("DOTDivision", back_populates="dot_unit")
    dot_office = relationship("DOTOffice", back_populates="dot_unit")
    user_office_information = relationship("UserOfficeInformation", back_populates="dot_unit")