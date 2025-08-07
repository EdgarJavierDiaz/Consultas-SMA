from sqlalchemy.orm import Session
from . import models, schemas

def get_tramos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TramoVial).offset(skip).limit(limit).all()

def create_tramo(db: Session, tramo: schemas.TramoVialCreate):
    db_tramo = models.TramoVial(**tramo.dict())
    db.add(db_tramo)
    db.commit()
    db.refresh(db_tramo)
    return db_tramo

def get_funcionarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Funcionario).offset(skip).limit(limit).all()

def create_funcionario(db: Session, funcionario: schemas.FuncionarioCreate):
    db_funcionario = models.Funcionario(**funcionario.dict())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

def get_reportes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ReporteFuncionario).offset(skip).limit(limit).all()

def create_reporte(db: Session, reporte: schemas.ReporteFuncionarioCreate):
    db_reporte = models.ReporteFuncionario(**reporte.dict())
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte
