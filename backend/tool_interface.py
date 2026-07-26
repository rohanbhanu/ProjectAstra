from abc import ABC, abstractmethod


class Tool(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
    @abstractmethod
    def validate_input(self, *args, **kwargs):
        pass


class CalculatorTool(Tool):

    def name(self):
        return "calculator"

    def description(self):
        return "Performs mathematical calculations."

    def execute(self, user_input):
        return 0


class LLMTool(Tool):

    def name(self):
        return "llm"

    def description(self):
        return "General conversation model."

    def execute(self,user_input,conversation_history):
        return 0


    