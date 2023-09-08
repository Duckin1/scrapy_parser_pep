import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep_spider'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        # Находим ссылки на PEP-документы и передаем их для дальнейшего парсинга
        pep_links = response.css('a[href^="/pep/"]::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        item = PepParseItem()
        item['number'] = response.css('h1::text').get().strip().split()[1]
        item['name'] = response.css('h1::text').get().strip().split(maxsplit=1)[1]
        item['status'] = response.css('dt:contains("Status") + dd::text').get().strip()
        yield item
