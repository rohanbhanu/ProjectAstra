from datetime import datetime
import logging
from enum import Enum

from backend.prompts import build_prompt
from backend import llm
from backend.tools import calculator

logger = logging.getLogger(__name__)


class Intent(Enum):
    CHAT = 1
    CALCULATOR = 2


def process(user_input: str) -> dict:
    """
    Main orchestration pipeline for Project Astra.

    Pipeline:

        User Input
            ↓
        Intent Detection
            ↓
        Memory (future)
            ↓
        RAG (future)
            ↓
        Tool Selection
            ↓
        Prompt Builder (only for LLM)
            ↓
        LLM / Tool
            ↓
        Save Memory
            ↓
        Response
    """

    pipeline_start = datetime.now()

    logger.info("User query received.")

    # -------------------------------
    # Intent Detection
    # -------------------------------
    intent = detect_intent(user_input)

    # -------------------------------
    # Future Modules
    # -------------------------------
    memory = retrieve_memory(user_input)

    rag_context = retrieve_rag(user_input)

    tool = choose_tool(intent)

    # -------------------------------
    # Calculator Route
    # -------------------------------
    if intent == Intent.CALCULATOR:

        logger.info("Routing request to Calculator.")

        calc_start = datetime.now()

        response = calculator.calculate(user_input)

        calc_time = (datetime.now() - calc_start).total_seconds()

        logger.info(f"Calculator completed in {calc_time:.3f} sec")

    # -------------------------------
    # LLM Route
    # -------------------------------
    else:

        logger.info("Routing request to Language Model.")

        prompt_start = datetime.now()

        prompt = build_prompt(user_input)

        prompt_time = (datetime.now() - prompt_start).total_seconds()

        logger.info("Prompt generated.")
        logger.info(f"Prompt generation completed in {prompt_time:.3f} sec")

        llm_start = datetime.now()

        response = llm.generate_response(prompt)

        llm_time = (datetime.now() - llm_start).total_seconds()

        logger.info(f"LLM response received in {llm_time:.3f} sec")

    # -------------------------------
    # Future Memory Save
    # -------------------------------
    save_memory(user_input, response)

    pipeline_time = (datetime.now() - pipeline_start).total_seconds()

    logger.info("Returning response")
    logger.info(f"Pipeline completed in {pipeline_time:.3f} sec")

    return response


def detect_intent(user_input):

    intent = Intent.CHAT

    req = str(user_input).lower()

    CALCULATOR_KEYWORDS = {"+", "-", "*", "/", "calculate"}

    if any(word in req for word in CALCULATOR_KEYWORDS):
        intent = Intent.CALCULATOR

    logger.info(f"Detected intent: {intent.name}")

    return intent


def retrieve_memory(user_input):

    logger.info("Checking memory history completed")

    return None


def retrieve_rag(user_input):

    logger.info("Retrieval-Augmented Generation check completed")

    return None


def choose_tool(intent):

    logger.info("Choosing tool completed")

    return None


def save_memory(user_input, response):

    logger.info("Memory saved.")

    return None