from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/funcionarios", tags=["Funcionarios"])

@router.get("/", response_model=list[schemas.Funcionario])
def listar_funcionarios(skip: int = 0, limit: int = 100, db: Session = Depends(database.SessionLocal)):
    return crud.get_funcionarios(db, skip, limit)

@router.post("/", response_model=schemas.Funcionario)
def crear_funcionario(funcionario: schemas.FuncionarioCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_funcionario(db, funcionario)
