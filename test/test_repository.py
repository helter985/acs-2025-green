import pytest
from database import repository, models

@pytest.fixture
def producto_mock(db_session):
    producto = models.Producto(
        codigo="TEST1",
        nombre="Producto Test",
        precio=999.99,
        imagen_filename="test.jpg"
    )
    db_session.add(producto)
    db_session.commit()
    return producto

def test_get_all_productos(db_session, producto_mock):
    productos = repository.get_all_productos(db_session)
    assert len(productos) == 1
    assert productos[0].codigo == "TEST1"

def test_get_all_productos_filtered(db_session, producto_mock):
    productos = repository.get_all_productos(db_session, name_filter="test")
    assert any("test" in p.nombre.lower() for p in productos)

def test_get_producto_by_codigo(db_session, producto_mock):
    producto = repository.get_producto_by_codigo(db_session, "TEST1")
    assert producto is not None
    assert producto.codigo == "TEST1"