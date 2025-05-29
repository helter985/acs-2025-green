import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.session import Base
from database import repository, models

# Base de datos en memoria para pruebas
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    # Datos de prueba
    producto = models.Producto(
        codigo="TEST1",
        nombre="Producto Test",
        precio=999.99,
        imagen_filename="test.jpg"
    )
    session.add(producto)
    session.commit()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)

def test_get_all_productos(db):
    productos = repository.get_all_productos(db)
    assert len(productos) == 1
    assert productos[0].codigo == "TEST1"

def test_get_all_productos_filtered(db):
    productos = repository.get_all_productos(db, name_filter="test")
    assert any("test" in p.nombre.lower() for p in productos)

def test_get_producto_by_codigo(db):
    producto = repository.get_producto_by_codigo(db, "TEST1")
    assert producto is not None
    assert producto.codigo == "TEST1"
