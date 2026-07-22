import requests
from backend.config import *
from backend.prompts import build_prompt




def generateResponse(user_input):

    prompt = build_prompt(user_input)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "num_predict": NUM_PREDICT,
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
        timeout=REQUEST_TIMEOUT
    )

    response.raise_for_status()
    data = response.json()
    reply = data["response"]
    prompt_tokens = data.get("prompt_eval_count", 0)
    completion_tokens = data.get("eval_count", 0)


    return {
    "reply": reply,
    "prompt_tokens": prompt_tokens,
    "completion_tokens": completion_tokens
    }