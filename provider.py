from fastapi import FastAPI, HTTPException
from typing import List
from models import ContextItem, ActionRequest, ActionResult, ProviderInfo

app = FastAPI()

# Example context: a list of files
context_items = [
    ContextItem(id="1", type="file", name="example.txt"),
    ContextItem(id="2", type="file", name="notes.md"),
]

provider_info = ProviderInfo(
    name="SimpleMCPProvider",
    version="1.0",
    actions=["list_context", "read"]
)

@app.get("/provider_info", response_model=ProviderInfo)
def get_provider_info():
    return provider_info

@app.get("/context", response_model=List[ContextItem])
def list_context():
    return context_items

@app.post("/action", response_model=ActionResult)
def perform_action(request: ActionRequest):
    if request.action == "read":
        for item in context_items:
            if item.id == request.target_id:
                # Simulate reading file content
                return ActionResult(success=True, result=f"Contents of {item.name}")
        return ActionResult(success=False, error="Item not found")
    return ActionResult(success=False, error="Unknown action")

# To run: uvicorn provider:app --reload
