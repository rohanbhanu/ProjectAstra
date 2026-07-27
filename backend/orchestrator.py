from datetime import datetime
import logging

from backend.intent import Intent
from backend.memory import Memory
from backend import tool_manager

logger = logging.getLogger(__name__)


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
        Tool Manager
            ↓
        Selected Tool
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

    logger.debug(
        "Conversation History: %s",
        conversation_history
    )

    logger.info(
        "Retrieved %d conversation messages.",
        len(conversation_history)
    )

    # ---------------------------------------
    # Future RAG
    # ---------------------------------------
    retrieve_rag(user_input)

    # ---------------------------------------
    # Tool Selection
    # ---------------------------------------
    tool = tool_manager.get_tool(intent)


    if tool is None:
        raise ValueError(
        f"No tool registered for {intent.name}")

    logger.info(
    "Routing request to %s",
    tool.name())
    if not tool.validate_input(
    user_input,
    conversation_history
):
        raise ValueError(
        "Invalid tool input.")

    response = tool.execute(
    user_input,
    conversation_history)



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

    logger.info(
        "Pipeline completed in %.3f sec",
        pipeline_time
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

    SEARCH_KEYWORDS = {
        "search",
        "latest",
        "today",
        "current",
        "news",
        "weather"
    }

    if any(word in req for word in CALCULATOR_KEYWORDS):
        intent = Intent.CALCULATOR

    elif any(word in req for word in SEARCH_KEYWORDS):
        intent = Intent.SEARCH

    logger.info(
        "Detected intent: %s",
        intent.name
    )

    return intent


def retrieve_rag(user_input):

    logger.info(
        "Retrieval-Augmented Generation check completed"
    )

    return None