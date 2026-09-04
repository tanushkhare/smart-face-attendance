# ⚡ Smart Face Attendance Biometrics

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://smart-face-attendance-six.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://smart-face-attendance-six.vercel.app](https://smart-face-attendance-six.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Biometric attendance verification service extracting 128-d face embeddings with cosine similarity nearest-neighbor matching and anti-spoofing liveness checks.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** OpenCV, Dlib / FaceNet, FastAPI, SQLite
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Live Matching:** Replaced hardcoded offline fallback with cosine similarity vector scoring.
* **Database Persistence:** Attendance logs are recorded in a disk-backed SQLite store.
* **Anti-Spoofing:** Evaluates image texture frequencies to reject printed paper attacks.

---

## 🚀 API Contracts
```http
POST /api/v1/attendance/verify
Request:
{
  "user_id": "USR-902",
  "embedding": [0.14, -0.22, 0.08],
  "liveness_pass": true
}

Response (200 OK):
{
  "verified": true,
  "similarity_score": 0.941,
  "user_name": "Tanush Khare",
  "log_id": "att_2026_9482"
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v