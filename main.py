from fastapi import FastAPI
from .routers import tramos, funcionarios, reportes
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Censo Vial y Seguridad",
    description="App para registrar y consultar tramos viales, reportes de funcionarios y condiciones de seguridad",
    version="1.0.0"
)

app.include_router(tramos.router)
app.include_router(funcionarios.router)
app.include_router(reportes.router)
