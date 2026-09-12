import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_verify_known_user():
    payload = {"probe_embedding": [0.35, 0.62, -0.41, 0.55], "confidence_threshold": 0.75}
    res = client.post("/api/v1/attendance/verify", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "VERIFIED_PRESENT"
    assert data["user_id"] == "USR-101"

def test_verify_unknown_user():
    payload = {"probe_embedding": [-0.99, -0.99, 0.0, 0.0], "confidence_threshold": 0.85}
    res = client.post("/api/v1/attendance/verify", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ACCESS_DENIED"
