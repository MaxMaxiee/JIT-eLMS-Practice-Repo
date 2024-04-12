import pytest
from fastapi.testclient import TestClient
from main import app
from db import database, models
@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def drop_all_tables():
    engine = database.engine
    yield
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)

# Unauthenticated User Tests
def test_create_user(client):
    payload = {
        "firstname": "PLACEHOLDER",
        "middlename": "PLACEHOLDER",
        "lastname": "PLACEHOLDER",
        "email": "PLACEHOLDER@example.com",
        "password": "PLACEHOLDER",
    }
    response = client.post('/admin/create', json=payload)
    assert response.status_code == 200