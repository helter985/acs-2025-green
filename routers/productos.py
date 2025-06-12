from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.responses import FileResponse
import os

from models.dto import ProductoDTO
from database import models, repository
from database.session import SessionLocal

router = APIRouter(prefix="/productos", tags=["Productos"])

BASE_URL = "http://localhost.localdomain:8000"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def entity_to_dto(producto: models.Producto) -> ProductoDTO:
    imagen_url = (
        f"{BASE_URL}/productos/{producto.codigo}/imagen"
        if producto.imagen_filename
        else f"{BASE_URL}/static/placeholder.png"
    )
    return ProductoDTO(
        codigo=producto.codigo,
        nombre=producto.nombre,
        precio=producto.precio,
        imagen=imagen_url
    )

@router.get("", response_model=List[ProductoDTO])
def get_productos(name: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if name is not None and not name.strip():
        raise HTTPException(status_code=400, detail="Parámetro de búsqueda inválido")
    
    productos = repository.get_all_productos(db, name)
    if not productos:
        raise HTTPException(status_code=204, detail="No se encontraron productos")
    
    return [entity_to_dto(p) for p in productos]

@router.get("/{codigo}", response_model=ProductoDTO)
def get_producto(codigo: str, db: Session = Depends(get_db)):
    producto = repository.get_producto_by_codigo(db, codigo)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return entity_to_dto(producto)

@router.get("/{codigo}/imagen")
def get_producto_imagen(codigo: str, db: Session = Depends(get_db)):
    producto = repository.get_producto_by_codigo(db, codigo)
    if not producto or not producto.imagen_filename:
        raise HTTPException(status_code=404, detail="Producto o imagen no encontrada")
    
    image_path = os.path.join("static", "images", producto.imagen_filename)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

    media_type = "image/jpeg" if producto.imagen_filename.endswith(".jpg") else "image/png"
    return FileResponse(image_path, media_type=media_type)
