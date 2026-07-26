from backend.intent import Intent
from backend.tools.calculator_tool import CalculatorTool
from backend.tools.llm_tool import LLMTool

_TOOL_REGISTRY = {
    Intent.CHAT: LLMTool(),
    Intent.CALCULATOR: CalculatorTool()
}


def get_tool(intent):
    return _TOOL_REGISTRY.get(intent)