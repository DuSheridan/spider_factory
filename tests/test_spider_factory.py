from unittest import TestCase
from game_spiders.spiders.spider_factory import create_spider


class TestFactory(TestCase):
    def test_create_spider(self):
        spider_class = create_spider(urls=["hello.com"], crawl_id=1, keywords="doomidoomi")
        self.assertEqual(spider_class.crawler_id, 1)
