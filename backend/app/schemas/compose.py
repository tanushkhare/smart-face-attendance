from pydantic import BaseModel
from typing import List

class ComposeStatus(BaseModel):
    services_active: int
    orchestrator: str
    active_services: List[str]