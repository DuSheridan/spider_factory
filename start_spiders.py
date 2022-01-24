import requests
from decouple import config
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from spiders.spider_factory import start_batch_crawling

CRAWLERS_API = config('CRAWLERS_API')
API_KEY = config('CRAWLER_API_KEY')
HEADERS = {'Authorization': f'Token {API_KEY}'}


def main():
    process = CrawlerProcess(get_project_settings())
    response = requests.get(CRAWLERS_API, headers=HEADERS).json()
    results = response['results']
    start_batch_crawling(process, results)
    while response["next"] is not None:
        response = requests.get(response["next"]).json()
        results = response['results']
        start_batch_crawling(process, results)


if __name__ == '__main__':
    configure_logging(get_project_settings())
    main()
