from backend.prompts import build_prompt
from backend import llm


def process(user_input: str) -> dict:
    """
    Main entry point for Project Astra.
    Future versions will decide whether to use:
    - Memory
    - RAG
    - Tools
    - Direct LLM
    """

    prompt = build_prompt(user_input)

    response = llm.generate_response(prompt)

    return response