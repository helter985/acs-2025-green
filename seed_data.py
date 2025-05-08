from database.session import SessionLocal, engine
from database.models import Producto
from sqlalchemy.exc import IntegrityError

# Crear tablas si no existen
Producto.metadata.create_all(bind=engine)

# Productos de ejemplo
productos = [
    Producto(codigo="A100", nombre="Yerba Mate", precio=1250.0, imagen_filename="yerba.jpg"),
    Producto(codigo="A200", nombre="Café Molido", precio=2200.0, imagen_filename="cafe.jpg"),
    Producto(codigo="A300", nombre="Dulce de Leche", precio=1850.5, imagen_filename="dulce.jpg"),
    Producto(codigo="A400", nombre="Galletitas", precio=950.0, imagen_filename="galletitas.png"),
    Producto(codigo="A500", nombre="Aceite de Girasol", precio=3200.0, imagen_filename="aceite.jpg"),
]

# Insertar productos
db = SessionLocal()
for prod in productos:
    existente = db.query(Producto).filter_by(codigo=prod.codigo).first()
    if not existente:
        db.add(prod)
try:
    db.commit()
    print("✅ Productos insertados correctamente.")
except IntegrityError as e:
    db.rollback()
    print("⚠️ Ya existían productos o hubo un error de integridad.")
finally:
    db.close()
