from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import attendance_router
import uvicorn

app = FastAPI(
    title="Smart Facial Recognition Attendance API",
    description="Vector embedding extraction, cosine similarity matching, and attendance auditing.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(attendance_router.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "smart-face-attendance"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
