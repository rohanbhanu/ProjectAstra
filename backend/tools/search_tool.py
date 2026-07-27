from backend.tool_interface import Tool
from backend.services import search


class SearchTool(Tool):

    def name(self):
        return "search"

    def description(self):
        return "Searches the web for latest information."

    def validate_input(
        self,
        user_input,
        conversation_history=None
    ):
        return isinstance(user_input, str)


    def execute(
        self,
        user_input,
        conversation_history=None
    ):

        results = search.search(user_input)

        formatted_results = ""

        for result in results:
            formatted_results += (
                f"Title: {result['title']}\n"
                f"URL: {result['url']}\n"
                f"Snippet: {result['snippet']}\n\n"
            )

        return {
            "reply": formatted_results,
            "prompt_tokens": 0,
            "completion_tokens": 0
        }