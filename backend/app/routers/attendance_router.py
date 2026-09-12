from fastapi import APIRouter, HTTPException
from backend.app.schemas.attendance_schema import FaceRegistrationRequest, FaceVerificationRequest, AttendanceRecord
from backend.app.services.face_service import face_engine

router = APIRouter(prefix="/api/v1/attendance", tags=["Face Attendance"])

@router.post("/register")
async def register(payload: FaceRegistrationRequest):
    return face_engine.register_face(payload.user_id, payload.full_name, payload.department, payload.mock_embedding)

@router.post("/verify", response_model=AttendanceRecord)
async def verify(payload: FaceVerificationRequest):
    return face_engine.verify_and_log(payload.probe_embedding, payload.confidence_threshold)

@router.get("/logs")
async def get_attendance_logs():
    return {"total_records": len(face_engine.logs), "records": face_engine.logs}
