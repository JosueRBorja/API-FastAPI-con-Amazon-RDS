from typing import Optional

from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
