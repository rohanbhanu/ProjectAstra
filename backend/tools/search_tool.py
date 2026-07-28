from backend.tool_interface import Tool
from backend.services import search
from backend.services import query_rewriter
import logging
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


    def execute(self, user_input, conversation_history=None):

        rewritten_query = query_rewriter.rewrite(user_input)
        logging.info("User Query:" + user_input)
        logging.info("Rewritten query:" + rewritten_query)

        results = search.search(rewritten_query)

        return {
        "search_results": results,
        "rewritten_query": rewritten_query
    }