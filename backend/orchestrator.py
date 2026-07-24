from datetime import datetime
from backend.prompts import build_prompt
from backend import llm
import logging


def process(user_input: str) -> dict:
    pipeline_start = datetime.now()
    """
    Main orchestration pipeline for Project Astra.

    This module coordinates all backend components.

    Pipeline:
    User Input
        ↓
    Memory (future)
        ↓
    RAG (future)
        ↓
    Tools (future)
        ↓
    Prompt Builder
        ↓
    LLM
        ↓
    Response
    """
    logging.info("User query received.")
    # TODO:
    # 1. Retrieve conversation memory
    # 2. Retrieve RAG context
    # 3. Decide whether external tools are needed
    # 4. Select the appropriate LLM
    prompt_start = datetime.now()

    prompt = build_prompt(user_input)
    logging.info("Prompt generated.")
    prompt_time = (datetime.now() - prompt_start).total_seconds()
    logging.info(f"Prompt generation completed in {prompt_time:.3f} sec")

    logging.info("Sending request to language model.")
    llm_start = datetime.now()

    response = llm.generate_response(prompt)
    llm_time = (datetime.now() - llm_start).total_seconds()
    logging.info(f"LLM response received in {llm_time:.3f} sec")
    logging.info("Response received from language model.")
    logging.info("Returning response")
    pipeline_time = (datetime.now() - pipeline_start).total_seconds()
    logging.info(f"Pipeline completed in {pipeline_time:.3f} sec")


    return response