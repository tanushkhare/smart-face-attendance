from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class FaceRegistrationRequest(BaseModel):
    employee_id: str = Field(..., description="Unique employee identifier")
    employee_name: str
    department: str
    embedding_vector: List[float] = Field(..., min_length=16, description="Normalized 128-d or 512-d biometric face embedding")

class VerificationRequest(BaseModel):
    embedding_vector: List[float] = Field(..., min_length=16, description="Biometric embedding extracted from live camera frame")

class AttendanceRecord(BaseModel):
    employee_id: str
    employee_name: str
    department: str
    timestamp: datetime
    confidence: float
    verification_status: str
