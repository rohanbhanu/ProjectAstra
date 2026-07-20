import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

OLLAMA_URL = "http://localhost:11434/api/generate"

def generateResponse(user_input):

    payload = {
        "model": "tinyllama",
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    data = response.json()

    return data["response"]