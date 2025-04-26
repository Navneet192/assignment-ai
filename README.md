# AI Agent Wrapper (FastAPI)

This project provides a unified API to create agents using either Vapi or Retell.

## Run the Server

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Sample Request

POST `/create-agent`

```json
{
  "provider": "vapi",
  "agent_name": "DemoBot",
  "voice": "alloy",
  "language": "en"
}
```

Replace `provider` with `"retell"` to call the Retell API instead.

## API Keys

Update the `.env` file with your real API keys:

```
VAPI_API_KEY=your-vapi-key
RETELL_API_KEY=your-retell-key
```

## Test it

Visit Swagger UI at: http://127.0.0.1:8000/docs