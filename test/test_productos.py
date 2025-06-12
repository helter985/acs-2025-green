from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from database.models import Producto

client = TestClient(app)

# 📌 Producto ficticio
fake_product = Producto(
    codigo='123',
    nombre='Aceite',
    precio=123.45,
    imagen_filename='aceite.jpg'
)


# ✅ Test: obtener todos los productos
@patch("database.repository.get_all_productos")
def test_get_all_productos(mock_get_all_productos):
    mock_get_all_productos.return_value = [fake_product]

    response = client.get("/productos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["codigo"] == "123"
    assert data[0]["nombre"] == "Aceite"
    assert data[0]["imagen"].endswith("/123/imagen")


# ✅ Test: obtener producto por código
@patch("database.repository.get_producto_by_codigo")
def test_get_producto(mock_get_producto_by_codigo):
    mock_get_producto_by_codigo.return_value = fake_product

    response = client.get("/productos/123")
    assert response.status_code == 200
    data = response.json()
    assert data["codigo"] == "123"
    assert data["nombre"] == "Aceite"
    assert data["imagen"].endswith("/123/imagen")


# ✅ Test: obtener imagen del producto
@patch("database.repository.get_producto_by_codigo")
@patch("os.path.exists")
def test_get_producto_imagen(mock_exists, mock_get_producto_by_codigo):
    mock_get_producto_by_codigo.return_value = fake_product
    mock_exists.return_value = True

    response = client.get("/productos/123/imagen")
    assert response.status_code == 200
    assert response.headers["content-type"] in ["image/jpeg", "image/png"]
