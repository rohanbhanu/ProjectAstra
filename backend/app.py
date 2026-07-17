from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

# Create a FastAPI application
app = FastAPI(
    title="Project Astra API",
    description="Backend API for Project Astra",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Project Astra!"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": f"Welcome {request.message}"
    }