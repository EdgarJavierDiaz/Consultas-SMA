from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class TramoVialBase(BaseModel):
    objectid: Optional[int]
    categoria: Optional[int]
    codigotramo: Optional[str]
    postereferenciainicial: Optional[float]
    distancia_inicial: Optional[float]
    postereferenciafinal: Optional[float]
    distancia_final: Optional[float]
    nombreruta: Optional[str]
    sector: Optional[str]
    administrador: Optional[str]
    fuente: Optional[str]
    globalid: Optional[UUID]
    nombretramo: Optional[str]
    created_user: Optional[str]
    created_date: Optional[int]
    last_edited_user: Optional[str]
    last_edited_date: Optional[int]
    territorial: Optional[int]
    revisionestado: Optional[str]
    shape_length: Optional[float]

class TramoVialCreate(TramoVialBase):
    pass

class TramoVial(TramoVialBase):
    id: int
    class Config:
        orm_mode = True

class FuncionarioBase(BaseModel):
    nombre: str
    cargo: Optional[str]
    telefono: Optional[str]
    correo: Optional[EmailStr]
    region: Optional[str]
    activo: Optional[bool] = True

class FuncionarioCreate(FuncionarioBase):
    pass

class Funcionario(FuncionarioBase):
    id: int
    class Config:
        orm_mode = True

class ReporteFuncionarioBase(BaseModel):
    tramo_id: int
    funcionario_id: int
    estado_tramo: Optional[str]
    observaciones: Optional[str]
    foto_url: Optional[str]
    ubicacion_lat: Optional[float]
    ubicacion_lon: Optional[float]

class ReporteFuncionarioCreate(ReporteFuncionarioBase):
    pass

class ReporteFuncionario(ReporteFuncionarioBase):
    id: int
    fecha_reporte: datetime
    class Config:
        orm_mode = True
