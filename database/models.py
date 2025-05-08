from sqlalchemy import Column, String, Float
from database.session import Base

class Producto(Base):
    __tablename__ = "productos"

    codigo = Column(String, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    imagen_filename = Column(String, nullable=True)
