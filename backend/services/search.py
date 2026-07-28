import logging
from backend.services import query_rewriter
from ddgs import DDGS

logger = logging.getLogger(__name__)


def search(query: str, max_results: int = 5):
    """
    Perform a web search using DuckDuckGo.

    Args:
        query: User search query.
        max_results: Maximum number of results.

    Returns:
        List of dictionaries containing:
            - title
            - url
            - snippet
    """

    logger.info("Searching web for: %s", query)

    results = []
    clean_query = query_rewriter.rewrite(query)

    logger.info("Original Query : %s", query)
    logger.info("Search Query   : %s", clean_query)

    try:
        with DDGS() as ddgs:

            search_results = ddgs.text(clean_query
                ,
                max_results=max_results
            )

            for item in search_results:

                results.append(
                    {
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "snippet": item.get("body", "")
                    }
                )

    except Exception:
        logger.exception("Web search failed.")

        return [
            {
                "title": "Search Error",
                "url": "",
                "snippet": "Unable to retrieve search results."
            }
        ]

    return results