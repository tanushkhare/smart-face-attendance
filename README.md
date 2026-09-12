# ⚡ Smart Face Attendance

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://smart-face-attendance-six.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://smart-face-attendance-six.vercel.app](https://smart-face-attendance-six.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Biometric attendance verification service extracting 128-d face embeddings with anti-spoofing liveness checks.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** OpenCV, Dlib / FaceNet, FastAPI, SQLite
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🚀 API Contracts
```http
POST /api/v1/attendance/verify
GET /health
```

---

## 💻 Local Quickstart
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v
```
