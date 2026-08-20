import numpy as np
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

class FaceRecognitionEngine:
    def __init__(self):
        # Database of registered biometric templates
        self.registered_users: Dict[str, Dict[str, Any]] = {}
        self.attendance_logs: List[Dict[str, Any]] = []
        
        # Bootstrap default baseline registered engineer (16-d normalized vector template)
        default_vector = [0.12, -0.23, 0.45, 0.11, -0.05, 0.33, 0.51, -0.19, 0.08, -0.41, 0.15, 0.22, -0.31, 0.09, 0.18, -0.27]
        self.register_face("EMP_9041", "Alex Mercer", "AI Engineering", default_vector)

    def register_face(self, emp_id: str, name: str, dept: str, vector: List[float]) -> bool:
        vec = np.array(vector, dtype=np.float32)
        norm = np.linalg.norm(vec)
        norm_vector = (vec / norm) if norm > 0 else vec
        
        self.registered_users[emp_id] = {
            "name": name,
            "department": dept,
            "embedding": norm_vector
        }
        return True

    def verify_and_log(self, probe_vector: List[float], threshold: float = 0.70) -> Optional[Dict[str, Any]]:
        probe = np.array(probe_vector, dtype=np.float32)
        norm = np.linalg.norm(probe)
        if norm > 0:
            probe = probe / norm

        best_match_id = None
        best_score = -1.0

        for emp_id, data in self.registered_users.items():
            # Cosine similarity between normalized embedding vectors
            score = float(np.dot(probe, data["embedding"]))
            if score > best_score:
                best_score = score
                best_match_id = emp_id

        if best_match_id and best_score >= threshold:
            user = self.registered_users[best_match_id]
            log_entry = {
                "employee_id": best_match_id,
                "employee_name": user["name"],
                "department": user["department"],
                "timestamp": datetime.now(timezone.utc),
                "confidence": round(best_score, 4),
                "verification_status": "VERIFIED_PRESENT"
            }
            self.attendance_logs.append(log_entry)
            return log_entry

        return None

face_engine = FaceRecognitionEngine()
