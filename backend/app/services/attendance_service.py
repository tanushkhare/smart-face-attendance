import math
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List

class FacialBiometricEngine:
    def __init__(self):
        # In-memory enrolled vector database
        self.enrolled_users: Dict[str, Dict[str, Any]] = {
            "EMP_101": {
                "user_id": "EMP_101",
                "full_name": "Alex Mercer",
                "embedding": [0.45, -0.12, 0.78, 0.33, 0.15, -0.22, 0.61, 0.05]
            },
            "EMP_102": {
                "user_id": "EMP_102",
                "full_name": "Elena Rostova",
                "embedding": [-0.30, 0.85, 0.11, -0.42, 0.55, 0.20, -0.10, 0.40]
            }
        }
        self.attendance_logs: List[Dict[str, Any]] = []

    def _cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        min_len = min(len(v1), len(v2))
        dot_product = sum(v1[i] * v2[i] for i in range(min_len))
        norm_v1 = math.sqrt(sum(x * x for x in v1[:min_len]))
        norm_v2 = math.sqrt(sum(x * x for x in v2[:min_len]))
        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0
        return round(dot_product / (norm_v1 * norm_v2), 4)

    def enroll_face(self, user_id: str, name: str, vector: List[float]) -> Dict[str, Any]:
        self.enrolled_users[user_id] = {
            "user_id": user_id,
            "full_name": name,
            "embedding": vector
        }
        return {"status": "SUCCESS", "user_id": user_id, "full_name": name}

    def verify_and_log(self, captured_vector: List[float], threshold: float = 0.75) -> Dict[str, Any]:
        best_match = None
        highest_sim = -1.0
        
        for user_id, user_data in self.enrolled_users.items():
            sim = self._cosine_similarity(captured_vector, user_data["embedding"])
            if sim > highest_sim:
                highest_sim = sim
                best_match = user_data

        status = "MATCH_CONFIRMED" if highest_sim >= threshold else "VERIFICATION_FAILED"
        user_name = best_match["full_name"] if status == "MATCH_CONFIRMED" else "Unknown / Unregistered"
        uid = best_match["user_id"] if status == "MATCH_CONFIRMED" else "UNREGISTERED"

        record = {
            "log_id": f"ATT-{uuid.uuid4().hex[:8].upper()}",
            "user_id": uid,
            "full_name": user_name,
            "similarity_score": highest_sim,
            "verification_status": status,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        if status == "MATCH_CONFIRMED":
            self.attendance_logs.append(record)
            
        return record

biometric_engine = FacialBiometricEngine()
