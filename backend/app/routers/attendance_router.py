from fastapi import APIRouter, HTTPException
from backend.app.schemas.attendance_schema import FaceRegistrationRequest, VerificationRequest, AttendanceRecord
from backend.app.services.face_service import face_engine
from typing import List

router = APIRouter(prefix="/api/v1/attendance", tags=["Face Attendance Verification"])

@router.post("/register", response_model=dict)
async def register_employee(payload: FaceRegistrationRequest):
    face_engine.register_face(
        emp_id=payload.employee_id,
        name=payload.employee_name,
        dept=payload.department,
        vector=payload.embedding_vector
    )
    return {"status": "success", "employee_id": payload.employee_id, "message": "Biometric template registered."}

@router.post("/verify", response_model=AttendanceRecord)
async def verify_identity(payload: VerificationRequest):
    record = face_engine.verify_and_log(payload.embedding_vector)
    if not record:
        raise HTTPException(status_code=401, detail="Biometric authentication failed: Face not recognized.")
    return AttendanceRecord(**record)

@router.get("/logs", response_model=List[AttendanceRecord])
async def get_logs():
    return [AttendanceRecord(**log) for log in face_engine.attendance_logs]
