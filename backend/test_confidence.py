from backend.confidence import calculate_search_confidence

results = [
    {
        "title": "NASA",
        "score": 5
    },
    {
        "title": "ISRO",
        "score": 4
    },
    {
        "title": "ESA",
        "score": 5
    }
]

print(calculate_search_confidence(results))