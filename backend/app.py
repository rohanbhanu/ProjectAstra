from fastapi import FastAPI
from pydantic import BaseModel
from backend import chatbot
import logging
from datetime import datetime

starttime = datetime.now()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


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

    logger = logging.getLogger(__name__)

    start_time = datetime.now()

    msg = request.message.lower()

    logger.info("User: %s", msg)

    response = chatbot.generateResponse(msg)

    logger.info(
        "Prompt Tokens      : %s",
        response.get("prompt_tokens", 0)
    )

    logger.info(
        "Completion Tokens  : %s",
        response.get("completion_tokens", 0)
    )

    latency = (
        datetime.now() - start_time
    ).total_seconds()

    logger.info(
        "Latency: %.2f sec",
        latency
    )

    logger.info("Status: Success")

    return response