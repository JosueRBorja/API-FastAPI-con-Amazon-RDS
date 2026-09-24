from typing import Optional

from sqlmodel import Field, SQLModel


class Libro(SQLModel, table=True):
    __tablename__ = "libros"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    anio_publicacion: int
