# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from scrapy.exceptions import DropItem
from decouple import config


class DjangoPipeline:
    collection_name = 'scrapy_items'
    scrape_api = config('SCRAPES_API')
    django_api_key = config('CRAWLER_API_KEY')
    headers = {'Authorization': f'Token {django_api_key}'}

    def process_item(self, item, spider):
        print(item)
        request_body = {
            'url': item['url'],
            'created_by': spider.crawler_id
        }
        try:
            result = requests.post(self.scrape_api, json=request_body, headers=self.headers)
        except Exception as e:
            raise DropItem(f"Exception occurred on posting the item the item, dropping: {e}")

        if result.status_code != 201:
            raise DropItem(f"Item was not created, dropping")
        return item
