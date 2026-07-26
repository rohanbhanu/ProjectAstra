from backend.tool_interface import Tool
from backend import llm_service


class LLMTool(Tool):

    def name(self):
        return "llm"

    def description(self):
        return "General conversation model."

    def execute(
        self,
        user_input,
        conversation_history
    ):
        return llm_service.generate(
            user_input,
            conversation_history
        )
    def validate_input(
    self,
    user_input,
    conversation_history=None):
        return isinstance(user_input, str)

def execute(self,user_input,conversation_history):
    return llm_service.generate(
            user_input,
            conversation_history
        )


def description(self):
    return (
        "General conversation and reasoning."
    )