import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath('//tbody[@class="jsx-2642336383"]/tr')
        for row in rows:
            country_name = row.xpath('.//td[1]/a/text()').get()
            country_debt = row.xpath('.//td[2]/text()').get()

            yield{
                'country_name': country_name,
                'country_debt': country_debt
            }
