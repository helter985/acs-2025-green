from pydantic import BaseModel, HttpUrl

class ProductoDTO(BaseModel):
    codigo: str
    nombre: str
    precio: float
    imagen: HttpUrl
