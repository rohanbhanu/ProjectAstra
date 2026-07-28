def format_search_results(results):

    if not results:
        return "No search results found."

    output = ""

    for index, item in enumerate(results, start=1):

        output += (
            f"{index}.\n"
            f"Title: {item['title']}\n"
            f"URL: {item['url']}\n"
            f"Snippet: {item['snippet']}\n\n"
        )

    return output