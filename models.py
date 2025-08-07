from sqlalchemy import Column, Integer, String, Float, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class TramoVial(Base):
    __tablename__ = "tramos_viales"
    id = Column(Integer, primary_key=True, index=True)
    objectid = Column(Integer)
    categoria = Column(Integer)
    codigotramo = Column(String(20))
    postereferenciainicial = Column(Float)
    distancia_inicial = Column(Float)
    postereferenciafinal = Column(Float)
    distancia_final = Column(Float)
    nombreruta = Column(Text)
    sector = Column(Text)
    administrador = Column(String(50))
    fuente = Column(String(50))
    globalid = Column(UUID)
    nombretramo = Column(Text)
    created_user = Column(String(50))
    created_date = Column(Integer)
    last_edited_user = Column(String(50))
    last_edited_date = Column(Integer)
    territorial = Column(Integer)
    revisionestado = Column(String(50))
    shape_length = Column(Float)

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cargo = Column(String(100))
    telefono = Column(String(20))
    correo = Column(String(100))
    region = Column(String(50))
    activo = Column(Boolean, default=True)

class ReporteFuncionario(Base):
    __tablename__ = "reportes_funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    tramo_id = Column(Integer, ForeignKey("tramos_viales.id"))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    fecha_reporte = Column(TIMESTAMP)
    estado_tramo = Column(String(50))
    observaciones = Column(Text)
    foto_url = Column(Text)
    ubicacion_lat = Column(Float)
    ubicacion_lon = Column(Float)
