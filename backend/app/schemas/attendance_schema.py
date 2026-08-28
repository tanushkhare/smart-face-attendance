from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class FaceEnrollmentRequest(BaseModel):
    user_id: str = Field(..., description="Unique employee / student ID (e.g. EMP_101)")
    full_name: str = Field(..., min_length=2)
    embedding_vector: List[float] = Field(..., min_length=4, description="Extracted facial landmark feature vector")

class FaceVerificationRequest(BaseModel):
    captured_vector: List[float] = Field(..., min_length=4, description="Inbound facial embedding vector from camera")
    similarity_threshold: Optional[float] = Field(default=0.75, ge=0.5, le=0.99)

class AttendanceRecord(BaseModel):
    log_id: str
    user_id: str
    full_name: str
    similarity_score: float
    verification_status: str
    timestamp: str
