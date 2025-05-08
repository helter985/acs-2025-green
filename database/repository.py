from sqlalchemy.orm import Session
from . import models
from typing import List, Optional

def get_all_productos(db: Session, name_filter: Optional[str] = None) -> List[models.Producto]:
    query = db.query(models.Producto)
    if name_filter:
        query = query.filter(models.Producto.nombre.ilike(f"%{name_filter}%"))
    return query.all()

def get_producto_by_codigo(db: Session, codigo: str) -> Optional[models.Producto]:
    return db.query(models.Producto).filter(models.Producto.codigo == codigo).first()
