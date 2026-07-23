from backend import config
import requests
def generate_response(prompt : str) -> dict:
    """
    Sends a prompt to the configured LLM and returns
    the generated response along with token usage.
    """
    payload = {
        "model": config.MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": config.TEMPERATURE,
            "top_p": config.TOP_P,
            "num_predict": config.NUM_PREDICT,
            "stop": config.STOP_WORDS
        }
    }

    response = requests.post(
        config.OLLAMA_URL,
        json=payload,
        timeout=config.REQUEST_TIMEOUT
    )

    try:


        response.raise_for_status()
        data = response.json()
        reply = data["response"]
        prompt_tokens = data.get("prompt_eval_count", 0)
        completion_tokens = data.get("eval_count", 0)

    except requests.exceptions.RequestException as e:
        return {
        "reply": reply,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens
        }

    return {
    "reply": reply,
    "prompt_tokens": prompt_tokens,
    "completion_tokens": completion_tokens
}