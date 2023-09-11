import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, URLS


class PepSpider(scrapy.Spider):
    """
    Пайплайн для обработки данных и создания сводной таблицы статусов PEP.
    """
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = URLS

    def parse(self, response):
        all_pep = response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        )
        for pep_link in all_pep:
            pep_url = response.urljoin(pep_link.extract()) + '/'
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get().strip()
        number = name.split('–')[0].replace('PEP', '').strip()
        status = response.css('dt:contains("Status") + dd::text').get()

        data = {
            'name': name,
            'number': number,
            'status': status,
        }
        yield PepParseItem(data)
