from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.vapi_service import create_vapi_agent
from services.retell_service import create_retell_agent

app = FastAPI()

class AgentRequest(BaseModel):
    provider: str
    agent_name: str
    voice: str
    language: str

@app.post("/create-agent")
def create_agent(request: AgentRequest):
    if request.provider == "vapi":
        return create_vapi_agent(request)
    elif request.provider == "retell":
        return create_retell_agent(request)
    else:
        raise HTTPException(status_code=400, detail="Invalid provider")