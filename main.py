from fastapi import FastAPI
from database import models
from database.session import engine
from routers import productos

# Crear tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API - Lista de Precios (Vendedor)",
    version="1.0.1",
    description="Endpoints accesibles para el rol de vendedor, con filtros y manejo de errores adecuado."
)

# Incluir router de productos
app.include_router(productos.router)
