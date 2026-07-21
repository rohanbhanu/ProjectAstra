import logging
import requests

from backend.prompts import SYSTEM_PROMPT

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

OLLAMA_URL = "http://localhost:11434/api/generate"


def generateResponse(user_input):

    prompt = (
        f"{SYSTEM_PROMPT}\n"
        f"{user_input}\n\n"
        f"Assistant:"
    )

    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 700
        }
    }

    logging.info("Sending request to Ollama...")

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    logging.info("Received response from Ollama.")

    return data["response"].strip()