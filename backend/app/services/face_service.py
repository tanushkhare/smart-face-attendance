import math
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

class FaceAttendanceEngine:
    def __init__(self):
        # Seed pre-registered biometric embeddings (unit normalized)
        self.registered_users = {
            "USR-101": {
                "name": "Sarah Connor",
                "dept": "DevOps",
                "embedding": [0.35, 0.62, -0.41, 0.55]
            },
            "USR-102": {
                "name": "John Doe",
                "dept": "Frontend",
                "embedding": [-0.12, 0.81, 0.45, -0.32]
            }
        }
        self.logs: List[Dict[str, Any]] = []

    def _cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        min_len = min(len(v1), len(v2))
        dot = sum(v1[i] * v2[i] for i in range(min_len))
        mag1 = math.sqrt(sum(v1[i]**2 for i in range(min_len))) or 1e-9
        mag2 = math.sqrt(sum(v2[i]**2 for i in range(min_len))) or 1e-9
        return dot / (mag1 * mag2)

    def register_face(self, user_id: str, name: str, dept: str, embedding: Optional[List[float]] = None) -> Dict[str, Any]:
        vector = embedding if embedding else [0.25, 0.55, 0.12, 0.78]
        self.registered_users[user_id] = {
            "name": name,
            "dept": dept,
            "embedding": vector
        }
        return {"user_id": user_id, "name": name, "status": "REGISTERED", "dimensions": len(vector)}

    def verify_and_log(self, probe: List[float], threshold: float = 0.75) -> Dict[str, Any]:
        best_match = None
        highest_sim = -1.0

        for uid, profile in self.registered_users.items():
            sim = self._cosine_similarity(probe, profile["embedding"])
            if sim > highest_sim:
                highest_sim = sim
                best_match = uid

        if best_match and highest_sim >= threshold:
            user = self.registered_users[best_match]
            record = {
                "record_id": f"REC-{uuid.uuid4().hex[:8].upper()}",
                "user_id": best_match,
                "full_name": user["name"],
                "status": "VERIFIED_PRESENT",
                "confidence": round(float(highest_sim), 4),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            self.logs.append(record)
            return record

        return {
            "record_id": f"REC-{uuid.uuid4().hex[:8].upper()}",
            "user_id": "UNKNOWN",
            "full_name": "Unidentified Individual",
            "status": "ACCESS_DENIED",
            "confidence": round(float(highest_sim), 4),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

face_engine = FaceAttendanceEngine()
