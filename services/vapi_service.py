import os
import httpx
from dotenv import load_dotenv
load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")

def create_vapi_agent(request):
    url = "https://api.vapi.ai/assistant"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": request.agent_name,
        "voice": {
            "provider": "openai",
            "voice_id": request.voice
        },
        "firstMessage": {
            "content": f"Hi! I'm {request.agent_name}, how can I assist you?"
        }
    }
    try:
        response = httpx.post(url, headers=headers, json=payload)
        response.raise_for_status()  
        return response.json()
    except httpx.RequestError as e:
        return {"error": f"Network error occurred: {str(e)}"}
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error occurred: {e.response.status_code} - {e.response.text}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}