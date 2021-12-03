from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping(test_app):
    response = test_app.get("/value/me")
    assert response.status_code == 200
    assert response.json() == {"value": "estou logado"}