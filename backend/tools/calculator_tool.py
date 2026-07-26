from backend.tool_interface import Tool
from backend.tools import calculator

class CalculatorTool(Tool):

    def name(self):
        return "calculator"

    def description(self):
        return "Performs mathematical calculations."

    def execute(
        self,
        user_input,
        conversation_history=None
    ):
        return calculator.calculate(user_input)
    def validate_input(
    self,
    user_input,
    conversation_history=None):
        return isinstance(user_input, str)

def description(self):
    return (
        "Perform arithmetic calculations."
    )