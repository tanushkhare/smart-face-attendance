import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_successful_face_verification():
    # Closely matching Alex Mercer's enrolled vector
    payload = {
        "captured_vector": [0.45, -0.12, 0.78, 0.33, 0.15, -0.22, 0.61, 0.05],
        "similarity_threshold": 0.80
    }
    res = client.post("/api/v1/attendance/verify", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["verification_status"] == "MATCH_CONFIRMED"
    assert data["user_id"] == "EMP_101"
    assert data["full_name"] == "Alex Mercer"
    assert data["similarity_score"] > 0.95

def test_failed_face_verification():
    # Non-matching vector
    payload = {
        "captured_vector": [-0.90, -0.90, -0.90, -0.90],
        "similarity_threshold": 0.80
    }
    res = client.post("/api/v1/attendance/verify", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["verification_status"] == "VERIFICATION_FAILED"
