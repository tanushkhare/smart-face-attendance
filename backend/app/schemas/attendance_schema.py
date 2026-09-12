from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class FaceRegistrationRequest(BaseModel):
    user_id: str = Field(..., min_length=3, description="Employee/Student unique ID")
    full_name: str = Field(..., min_length=2)
    department: str = Field(default="Engineering")
    mock_embedding: Optional[List[float]] = Field(default=None, description="128-d or 512-d feature vector")

class FaceVerificationRequest(BaseModel):
    probe_embedding: List[float] = Field(..., min_items=4, description="Extracted facial feature vector")
    confidence_threshold: float = Field(default=0.75, ge=0.5, le=0.99)

class AttendanceRecord(BaseModel):
    record_id: str
    user_id: str
    full_name: str
    status: str
    confidence: float
    timestamp: str
