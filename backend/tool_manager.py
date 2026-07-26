from backend import llm_service
from backend.tools import calculator
from backend.intent import Intent

TOOLS = {
    Intent.CHAT: llm_service.generate,
    Intent.CALCULATOR: calculator.calculate,
}


def get_tool(intent):
    return TOOLS.get(intent)


def execute(intent, user_input, conversation_history):

    tool = get_tool(intent)

    if tool is None:
        raise ValueError(f"No tool registered for {intent}")

    if intent == Intent.CALCULATOR:
        return tool(user_input)

    return tool(
        user_input,
        conversation_history
    )