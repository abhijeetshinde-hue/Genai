from fastapi import FastAPI
from datetime import datetime

api = FastAPI(title="Sample Service")

@api.get("/health")
def health_check():
    return {
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }

@api.get("/technologies")
def list_technologies():
    stack = [
        {"name": "FastAPI", "type": "backend"},
        {"name": "Docker", "type": "container"},
        {"name": "Streamlit", "type": "frontend"}
    ]
    return {
        "count": len(stack),
        "tools": stack
    }
