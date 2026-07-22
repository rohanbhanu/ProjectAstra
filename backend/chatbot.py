import requests

from backend.prompts import build_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"


def generateResponse(user_input):

    prompt = build_prompt(user_input)

    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": 500,
            "stop": [
                "User:",
                "Assistant:",
                "Human:",
                "Project Astra:"
            ]
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["response"].strip()