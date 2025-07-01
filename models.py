from pydantic import BaseModel
from typing import List, Optional, Any

class ContextItem(BaseModel):
    id: str
    type: str  # e.g., 'file', 'directory', 'code', etc.
    name: str
    data: Optional[Any] = None

class ActionRequest(BaseModel):
    action: str  # e.g., 'read', 'write', 'search'
    target_id: str
    parameters: Optional[dict] = None

class ActionResult(BaseModel):
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None

class ProviderInfo(BaseModel):
    name: str
    version: str
    actions: List[str]

# These models form the basis for MCP communication between agents and providers.
