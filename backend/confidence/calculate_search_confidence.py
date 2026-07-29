import logging

logger = logging.getLogger(__name__)


def calculate_search_confidence(results):
    """
    Calculate overall confidence from ranked search results.

    Returns:
        HIGH
        MEDIUM
        LOW
    """

    if not results:
        logger.info("No search results found.")
        return "LOW"

    scores = [result.get("score", 0) for result in results]

    average_score = sum(scores) / len(scores)

    logger.info(
        "Average Search Score: %.2f",
        average_score
    )

    if average_score >= 4:
        return "HIGH"

    elif average_score >= 2:
        return "MEDIUM"

    else:
        return "LOW"