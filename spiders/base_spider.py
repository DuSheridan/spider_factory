import scrapy


class BaseSpider(scrapy.Spider):
    name = "quotes"
    urls = []
    keywords = []
    crawler_id = None
    max_depth = 10

    def start_requests(self):
        current_depth = 0
        while self.urls and current_depth < self.max_depth:
            yield scrapy.Request(url=self.urls.pop(), callback=self.parse)
            current_depth += 1

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
                'url': response.url,
            }
