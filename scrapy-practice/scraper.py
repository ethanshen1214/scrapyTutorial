import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2020']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for legoset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            yield {
                'name': legoset.css(NAME_SELECTOR).extract_first()
            }

