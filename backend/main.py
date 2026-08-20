from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import attendance_router
import uvicorn

app = FastAPI(
    title="Smart Face Attendance System API",
    description="Computer vision facial embedding recognition, cosine similarity verification, and automated attendance registry.",
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
async def health():
    return {"status": "healthy", "service": "smart-face-attendance", "cv_pipeline": "Normalized Cosine Embeddings"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
