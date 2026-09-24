from fastapi import FastAPI
from sqlalchemy import text

from app.database import SessionDep, lifespan
from app.routers import libros, usuarios

app = FastAPI(
    title="API FastAPI EC2 RDS",
    lifespan=lifespan,
)

app.include_router(usuarios.router)
app.include_router(libros.router)


@app.get("/", tags=["estado"])
def read_root():
    return {"message": "API FastAPI funcionando creado por Josue"}


@app.get("/check-db", tags=["estado"])
def check_database(session: SessionDep):
    result = session.exec(text("SELECT 1")).one()[0]
    return {"database": "ok", "result": result}
