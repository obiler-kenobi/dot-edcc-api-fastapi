from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Designation(Base):
    __tablename__ = "designation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    designation_title = Column(String(50), nullable=False)
    designation_abbreviation = Column(String(20), nullable=False)
    date_encoded = Column(TIMESTAMP, nullable=False)
    encoded_by = Column(String(50), nullable=False)
