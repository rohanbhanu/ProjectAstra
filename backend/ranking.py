import logging

logger = logging.getLogger(__name__)


def rank_results(results, top_k=3):

    """
    Sort search results based on evaluator score
    and keep only top results.
    """

    if not results:
        return []

    ranked = sorted(
        results,
        key=lambda x: x.get("score", 0),
        reverse=True
    )

    filtered = ranked[:top_k]

    logger.info(
        "Selected top %d search results",
        len(filtered)
    )

    logger.info(
        "Ranking Output: %s",
        filtered
    )

    return filtered