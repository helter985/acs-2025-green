# test/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.session import Base
from main import app  # O tu archivo principal de FastAPI
from fastapi.testclient import TestClient

# Crear engine para DB en memoria
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Fixture de sesión
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)  # Crear tablas
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Limpiar entre tests

# Fixture de cliente FastAPI con override
@pytest.fixture()
def client(db_session):
    from fastapi import Depends
    from database.session import SessionLocal

    def override_get_db():
        yield db_session

    app.dependency_overrides[SessionLocal] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
