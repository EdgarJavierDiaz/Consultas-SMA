from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/tramos", tags=["Tramos Viales"])

@router.get("/", response_model=list[schemas.TramoVial])
def listar_tramos(skip: int = 0, limit: int = 100, db: Session = Depends(database.SessionLocal)):
    return crud.get_tramos(db, skip, limit)

@router.post("/", response_model=schemas.TramoVial)
def crear_tramo(tramo: schemas.TramoVialCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_tramo(db, tramo)
