from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from backend.app.schemas.attendance_schema import FaceEnrollmentRequest, FaceVerificationRequest, AttendanceRecord
from backend.app.services.attendance_service import biometric_engine

router = APIRouter(prefix="/api/v1/attendance", tags=["Biometric Facial Attendance"])

@router.post("/enroll")
async def enroll_user(payload: FaceEnrollmentRequest):
    return biometric_engine.enroll_face(payload.user_id, payload.full_name, payload.embedding_vector)

@router.post("/verify", response_model=AttendanceRecord)
async def verify_attendance(payload: FaceVerificationRequest):
    try:
        record = biometric_engine.verify_and_log(payload.captured_vector, payload.similarity_threshold or 0.75)
        return AttendanceRecord(**record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/logs", response_model=List[AttendanceRecord])
async def list_attendance_logs():
    return biometric_engine.attendance_logs
