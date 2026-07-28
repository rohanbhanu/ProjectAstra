from backend.tool_interface import Tool
from backend.services import search
import logging


class SearchTool(Tool):


    def name(self):
        return "search"


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

        logging.info(
            "User Query: %s",
            user_input
        )

        results = search.search(
            user_input
        )

        return {
            "search_results": results
        }
    def description(self):
        return "Searches the web and retrieves relevant information."