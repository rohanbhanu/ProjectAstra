import logging
import re

logger = logging.getLogger(__name__)


STOP_WORDS = {
    "the",
    "a",
    "an",
    "on",
    "in",
    "for",
    "about",
    "give",
    "me",
    "please",
    "latest",
    "news"
}


def normalize(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        "",
        text
    )

    return text.split()



def evaluate_search_results(results, query):

    logger.info(
        "Evaluating search results"
    )

    query_words = set(
        normalize(query)
    )


    query_words = (
        query_words
        -
        STOP_WORDS
    )


    evaluated = []


    for result in results:

        content = (
            result.get("title","")
            +
            " "
            +
            result.get("snippet","")
        )


        content_words = set(
            normalize(content)
        )


        matched_words = (
            query_words
            &
            content_words
        )


        score = len(
            matched_words
        )


        result["score"] = score


        evaluated.append(result)


        logger.info(
            "%s => Score %s",
            result["title"],
            score
        )


    evaluated.sort(
        key=lambda x:x["score"],
        reverse=True
    )


    return evaluated