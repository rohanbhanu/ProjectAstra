import logging

logger = logging.getLogger(__name__)


def build_context(search_results):

    context = ""

    for result in search_results:

        context += f"""
Title:
{result['title']}

Source:
{result['url']}

Information:
{result['snippet']}

-------------------------
"""

    logger.info(
        "Search context created with %d results",
        len(search_results)
    )

    return context