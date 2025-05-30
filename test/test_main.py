import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_productos_success():
    response = client.get("/productos")
    assert response.status_code == 200 or response.status_code == 204

def test_get_productos_filtered():
    response = client.get("/productos?name=yerba")
    assert response.status_code in (200, 204)
    if response.status_code == 200:
        assert any("yerba" in p["nombre"].lower() for p in response.json())

def test_get_producto_by_codigo_success():
    response = client.get("/productos/A100")
    assert response.status_code == 200
    assert response.json()["codigo"] == "A100"

def test_get_producto_by_codigo_not_found():
    response = client.get("/productos/Z999")
    assert response.status_code == 404

def test_get_imagen_producto_success():
    response = client.get("/productos/A100/imagen")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")

def test_get_imagen_producto_not_found():
    response = client.get("/productos/Z999/imagen")
    assert response.status_code == 404
