from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/reportes", tags=["Reportes de Funcionarios"])

@router.get("/", response_model=list[schemas.ReporteFuncionario])
def listar_reportes(skip: int = 0, limit: int = 100, db: Session = Depends(database.SessionLocal)):
    return crud.get_reportes(db, skip, limit)

@router.post("/", response_model=schemas.ReporteFuncionario)
def crear_reporte(reporte: schemas.ReporteFuncionarioCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_reporte(db, reporte)
