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
        f"Retrieved {len(conversation_history)} conversation messages."
    )

    # ---------------------------------------
    # Future Modules
    # ---------------------------------------
    retrieve_rag(user_input)

    # ---------------------------------------
    # Tool Selection
    # ---------------------------------------
    response = tool_manager.execute(
        intent,
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