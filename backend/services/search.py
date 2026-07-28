import logging
from backend.services import query_rewriter
from ddgs import DDGS

logger = logging.getLogger(__name__)


def search(query: str, max_results: int = 5):

    logger.info("Searching web for: %s", query)

    results = []

    clean_query = query_rewriter.rewrite(query)

    logger.info("Original Query : %s", query)
    logger.info("Search Query   : %s", clean_query)

    with DDGS() as ddgs:

        search_results = ddgs.text(
            clean_query,
            max_results=max_results
        )