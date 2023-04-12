from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.database import Base

class QPScope(Base):
    __tablename__ = "qp_scope"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    scope = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_scope")

class QPDefinitionOfTerm(Base):
    __tablename__ = "qp_definition_of_term"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    term = Column(String(80), nullable=False)
    definition = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_definition_of_term")

class QPReferenceDocument(Base):
    __tablename__ = "qp_reference_document"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    reference_document = Column(Text, nullable=False)
    file_path = Column(String(250), nullable=True)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_reference_document")

class QPResponsbilityAndAuthority(Base):
    __tablename__ = "qp_responsibility_and_authority"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    authority = Column(String, nullable=False)
    responsibility = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_responsibility_and_authority")
    qp_process_in_charge = relationship("QPProcessInCharge", back_populates="qp_responsibility_and_authority")

class QPProcedure(Base):
    __tablename__ = "qp_procedure"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    procedure = Column(Text, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_procedure")
    qp_process = relationship("QPProcess", back_populates="qp_procedure")

class QPProcess(Base):
    __tablename__ = "qp_process" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    procedure_id = Column(Integer, ForeignKey("qp_procedure.id"))
    drrrf_id = Column(Integer, ForeignKey("drrrf.id"))
    process_title = Column(String(100), nullable=False)
    process_description = Column(JSONB, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False)

    drrrf = relationship("DRRRF", back_populates="qp_process")
    qp_procedure = relationship("QPProcedure", back_populates="qp_process")
    qp_process_in_charge = relationship("QPProcessInCharge", back_populates="qp_process")
    qp_process_record = relationship("QPProcessRecord", back_populates="qp_process")