from datetime import datetime
import logging

from backend.evaluators import evaluate_search_results
from backend.intent import Intent
from backend.memory import Memory
from backend import tool_manager
from backend import prompts
from backend import llm
from backend.formatters.search_formatter import format_search_results
from backend.ranking import rank_results

logger = logging.getLogger(__name__)


def process(user_input: str) -> dict:

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

    logger.info(
        "Retrieved %d conversation messages.",
        len(conversation_history)
    )


    # ---------------------------------------
    # RAG Placeholder
    # ---------------------------------------
    rag_context = retrieve_rag(user_input)


    # ---------------------------------------
    # Tool Selection
    # ---------------------------------------
    tool = tool_manager.get_tool(intent)

    if tool is None:
        raise ValueError(
            f"No tool registered for {intent.name}"
        )


    logger.info(
        "Routing request to %s",
        tool.name()
    )


    if not tool.validate_input(
        user_input,
        conversation_history
    ):
        raise ValueError(
            "Invalid tool input."
        )


    # ---------------------------------------
    # Execute Tool
    # ---------------------------------------
    tool_response = tool.execute(
        user_input,
        conversation_history
    )


    logger.debug(
        "Raw Tool Response: %s",
        tool_response
    )


    # ---------------------------------------
    # SEARCH PIPELINE
    #
    # Search Result
    #       ↓
    # Evaluator
    #       ↓
    # Formatter
    #       ↓
    # Prompt Builder
    #       ↓
    # LLM
    #
    # ---------------------------------------

    if intent == Intent.SEARCH:


        search_results = tool_response.get(
            "search_results",
            []
        )


        if search_results:


            evaluated_results = evaluate_search_results(
            tool_response["search_results"],
            user_input
            )


            ranked_results = rank_results(
            evaluated_results,
            top_k=3)
            tool_response["search_results"] = ranked_results
            logger.info("Evaluated Search Results: %s",evaluated_results)


            formatted_results = format_search_results(
                ranked_results
            )


            logger.debug(
                "Formatted Search Results:\n%s",
                formatted_results
            )


            prompt = prompts.build_search_prompt(
                user_input,
                formatted_results,
                conversation_history
            )


            response = llm.generate_response(
                prompt
            )


        else:

            response = {
                "reply": (
                    "I could not find any relevant "
                    "search results."
                ),
                "prompt_tokens": 0,
                "completion_tokens": 0
            }


    else:

        response = tool_response



    # ---------------------------------------
    # Save Memory
    # ---------------------------------------

    if "reply" in response:

        Memory.store(
            user_input,
            response["reply"]
        )

        logger.info(
            "Conversation saved to memory."
        )


    logger.info(
        response
    )


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


    if any(
        word in req
        for word in CALCULATOR_KEYWORDS
    ):

        intent = Intent.CALCULATOR


    elif any(
        word in req
        for word in SEARCH_KEYWORDS
    ):

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