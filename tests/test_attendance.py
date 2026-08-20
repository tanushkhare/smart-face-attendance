import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_registered_face_verification():
    alex_vector = [0.12, -0.23, 0.45, 0.11, -0.05, 0.33, 0.51, -0.19, 0.08, -0.41, 0.15, 0.22, -0.31, 0.09, 0.18, -0.27]
    res = client.post("/api/v1/attendance/verify", json={"embedding_vector": alex_vector})
    assert res.status_code == 200
    data = res.json()
    assert data["employee_id"] == "EMP_9041"
    assert data["verification_status"] == "VERIFIED_PRESENT"

def test_unregistered_face_rejection():
    intruder_vector = [-0.85, 0.11, -0.32, 0.62, 0.18, -0.09, 0.12, 0.44, -0.21, 0.05, -0.67, 0.19, 0.02, -0.34, 0.11, 0.05]
    res = client.post("/api/v1/attendance/verify", json={"embedding_vector": intruder_vector})
    assert res.status_code == 401
