from fastapi import APIRouter
from app.schemas.compose import ComposeStatus
from app.services.compose_service import get_compose_status

router = APIRouter(prefix="/api", tags=["Orchestration"])

@router.get("/compose-status", response_model=ComposeStatus)
def compose_status():
    return get_compose_status()