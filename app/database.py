import os
from collections.abc import Generator
from contextlib import asynccontextmanager
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url: 
    raise ValueError("Falta configurar DATABASE_URL en el archivo .env")

engine = create_engine(database_url, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
