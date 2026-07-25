from datetime import datetime
import logging
from enum import Enum
from backend.memory import Memory
from backend.prompts import build_prompt
from backend import llm
from backend.tools import calculator
from backend import llm_service
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
        Conversation Memory
            ↓
        RAG (future)
            ↓
        Tool Selection
            ↓
        Prompt Builder (LLM only)
            ↓
        LLM / Tool
            ↓
        Save Memory
            ↓
        Response
    """
    logger.info("User query received.")

    pipeline_start = datetime.now()

    

    # ---------------------------------------
    # Intent Detection
    # ---------------------------------------
    intent = detect_intent(user_input)

    # ---------------------------------------
    # Conversation Memory
    # ---------------------------------------
    conversation_history = Memory.retrieve()
    logger.info(str(conversation_history))

    logger.info(
        f"Retrieved {len(conversation_history)} conversation messages."
    )

    # ---------------------------------------
    # Future Modules
    # ---------------------------------------
    retrieve_rag(user_input)

    choose_tool(intent)

    # ---------------------------------------
    # Calculator Route
    # ---------------------------------------
    if intent == Intent.CALCULATOR:

        logger.info("Routing request to Calculator.")

        calc_start = datetime.now()

        response = calculator.calculate(user_input)

        calc_time = (datetime.now() - calc_start).total_seconds()

        logger.info(
            f"Calculator completed in {calc_time:.3f} sec"
        )

    # ---------------------------------------
    # LLM Route
    # ---------------------------------------
    else:

        logger.info("Routing request to Language Model.")
        response = llm_service.generate(
        user_input,
        conversation_history
        )
        

    # ---------------------------------------
    # Save Conversation
    # ---------------------------------------
    Memory.store(
        user_input,
        response["reply"]
    )

    logger.info("Conversation saved to memory.")

    pipeline_time = (
        datetime.now() - pipeline_start
    ).total_seconds()

    logger.info("Returning response")
    logger.info(
        f"Pipeline completed in {pipeline_time:.3f} sec"
    )

    return response


def detect_intent(user_input):

    intent = Intent.CHAT

    req = str(user_input).lower()

    CALCULATOR_KEYWORDS = {
        "+",
        "-",
        "*",
        "/",
        "calculate"
    }

    if any(word in req for word in CALCULATOR_KEYWORDS):
        intent = Intent.CALCULATOR

    logger.info(f"Detected intent: {intent.name}")

    return intent


def retrieve_rag(user_input):

    logger.info(
        "Retrieval-Augmented Generation check completed"
    )

    return None


def choose_tool(intent):

    logger.info("Choosing tool completed")

    return None