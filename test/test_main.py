# test/test_main.py

import pytest

def test_get_productos_success(client):
    response = client.get("/productos")
    assert response.status_code in (200, 204)

def test_get_productos_filtered(client):
    response = client.get("/productos?name=yerba")
    
    #averiguar como mockear la llamada a repository.get_producto_by_codigo(db, codigo)
    assert response.status_code in (200, 204)
    if response.status_code == 200: 
        assert any("yerba" in p["nombre"].lower() for p in response.json())

def test_get_producto_by_codigo_success(client):
    response = client.get("/productos/A100")
    assert response.status_code == 200
    assert response.json()["codigo"] == "A100"

def test_get_producto_by_codigo_not_found(client):
    response = client.get("/productos/Z999")
    assert response.status_code == 404

def test_get_imagen_producto_success(client):
    response = client.get("/productos/A100/imagen")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")

def test_get_imagen_producto_not_found(client):
    response = client.get("/productos/Z999/imagen")
    assert response.status_code == 404


#cuando se ejecuta normalmente se usa base en postgres, en cambio los test unitarios se corren en sqlite. verificar estos. si no esta, agregarlo