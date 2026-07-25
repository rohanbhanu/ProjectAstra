from datetime import datetime
import logging
import requests

from backend.prompts import build_prompt
from backend import llm

logger = logging.getLogger(__name__)


def generate(user_input, conversation_history):
    """
    Handles the complete LLM pipeline.

    Pipeline:
        Preprocess Input
            ↓
        Build Prompt
            ↓
        Call LLM
            ↓
        Postprocess Response
            ↓
        Return Standard Response
    """

    service_start = datetime.now()

    try:

        # ---------------------------------------
        # Preprocess User Input
        # ---------------------------------------
        user_input = preprocess(user_input)

        # ---------------------------------------
        # Build Prompt
        # ---------------------------------------
        logger.info("Building prompt")

        prompt_start = datetime.now()

        prompt = build_prompt(
            user_input,
            conversation_history
        )

        prompt_time = (
            datetime.now() - prompt_start
        ).total_seconds()

        logger.info(
            f"Prompt generation completed in {prompt_time:.3f} sec"
        )

        # ---------------------------------------
        # Send request to LLM
        # ---------------------------------------
        logger.info("Sending request to LLM")

        llm_start = datetime.now()

        response = llm.generate_response(prompt)

        llm_time = (
            datetime.now() - llm_start
        ).total_seconds()

        logger.info(
            f"LLM response received in {llm_time:.3f} sec"
        )

        # ---------------------------------------
        # Postprocess
        # ---------------------------------------
        response = postprocess(response)

        # ---------------------------------------
        # Total Service Time
        # ---------------------------------------
        service_time = (
            datetime.now() - service_start
        ).total_seconds()

        logger.info(
            f"LLM Service completed in {service_time:.3f} sec"
        )

        # ---------------------------------------
        # Standard Response
        # ---------------------------------------
        return {
            "reply": response["reply"],
            "prompt_tokens": response["prompt_tokens"],
            "completion_tokens": response["completion_tokens"]
        }

    except requests.exceptions.RequestException as e:

        logger.exception("LLM Request Failed")

        return {
            "reply": "Sorry, I couldn't process your request.",
            "prompt_tokens": 0,
            "completion_tokens": 0
        }


class BaseLLM:

    def generate(
        self,
        user_input,
        conversation_history
    ):
        raise NotImplementedError


def preprocess(user_input: str) -> str:
    """
    Clean user input before prompt generation.
    """

    return user_input.strip()


def postprocess(response: dict) -> dict:
    """
    Clean LLM output before returning it.
    """

    if "reply" in response:
        response["reply"] = response["reply"].strip()

    return response