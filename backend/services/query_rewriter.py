import re


def rewrite(user_query: str) -> str:
    """
    Cleans a user's search query before sending it
    to the search engine.
    """

    query = user_query.lower().strip()

    # Remove common filler phrases
    fillers = [
        "can you",
        "could you",
        "please",
        "tell me",
        "show me",
        "i want to know",
        "give me",
        "find",
        "search for",
        "latest",
        "current"
    ]

    for phrase in fillers:
        query = query.replace(phrase, "")

    # Remove extra whitespace
    query = re.sub(r"\s+", " ", query)

    return query.strip()