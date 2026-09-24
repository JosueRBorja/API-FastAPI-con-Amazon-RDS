from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.database import SessionDep
from app.models import Libro


router = APIRouter(prefix="/libros", tags=["libros"])


@router.post("/", response_model=Libro)
def crear_libro(libro: Libro, session: SessionDep):
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro


@router.get("/", response_model=list[Libro])
def listar_libros(session: SessionDep):
    return session.exec(select(Libro)).all()


@router.get("/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@router.put("/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: int, datos: Libro, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    libro.titulo = datos.titulo
    libro.autor = datos.autor
    libro.anio_publicacion = datos.anio_publicacion
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro


@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    session.delete(libro)
    session.commit()
    return {"ok": True}
