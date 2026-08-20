from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import compose_router

app = FastAPI(title="Project 18: Orchestration API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(compose_router.router)

@app.get("/")
def read_root():
    return {"message": "Project 18 Compose Orchestrator Backend is online!"}