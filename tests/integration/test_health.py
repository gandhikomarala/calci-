import pytest
from fastapi.testclient import TestClient
from apps.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "HEALTHY"

def test_ready_check():
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "READY"
