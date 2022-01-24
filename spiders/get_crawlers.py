def get_crawlers():
    response = requests.get(CRAWLERS_API).json()
    results = response['results']
    start_batch_crawling(process, results)
    while response["next"] is not None:
        response = requests.get(response["next"]).json()
        results = response['results']
        start_batch_crawling(process, results)