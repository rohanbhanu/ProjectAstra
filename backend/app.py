from fastapi import FastAPI
from pydantic import BaseModel
from backend import chatbot

class ChatRequest(BaseModel):
    message: str

app = FastAPI(
    title="Project Astra API",
    description="Backend API for Project Astra",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Project Astra!"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    msg = request.message.lower()

    return {
        "reply": chatbot.generateResponse(msg)
    }