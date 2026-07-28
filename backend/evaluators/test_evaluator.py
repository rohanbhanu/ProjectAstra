from backend.evaluators import evaluate_search_results


results = [

    {
        "title":"NASA Moon Mission",
        "url":"abc.com",
        "snippet":
        "NASA plans future lunar missions."
    },


    {
        "title":"Football News",
        "url":"xyz.com",
        "snippet":
        "Latest football updates."
    }

]


query="latest news on moon"


clean = evaluate_search_results(
    results,
    query
)


print(clean)