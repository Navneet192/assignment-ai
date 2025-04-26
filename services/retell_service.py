import os
import httpx
from dotenv import load_dotenv
load_dotenv()

RETELL_API_KEY = os.getenv("RETELL_API_KEY")

def create_retell_agent(request):
    url = "https://api.retellai.com/agents"
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "display_name": request.agent_name,
        "voice_type": request.voice,
        "lang_code": request.language
    }
    response = httpx.post(url, headers=headers, json=payload)
    return response.json()