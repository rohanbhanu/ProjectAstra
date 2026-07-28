from backend.ranking import rank_results


results = [
    {
        "title": "NASA Mars",
        "score": 5
    },
    {
        "title": "Football News",
        "score": 0
    },
    {
        "title": "SpaceX Mars Mission",
        "score": 4
    }
]


output = rank_results(results)

print(output)