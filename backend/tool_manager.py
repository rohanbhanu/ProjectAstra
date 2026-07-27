from backend.intent import Intent
from backend.tools.calculator_tool import CalculatorTool
from backend.tools.llm_tool import LLMTool
from backend.tools.search_tool import SearchTool

_TOOL_REGISTRY = {
    Intent.CHAT: LLMTool(),
    Intent.CALCULATOR: CalculatorTool(),
    Intent.SEARCH: SearchTool()
}


def get_tool(intent):
    return _TOOL_REGISTRY.get(intent)