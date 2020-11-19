import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        for product in response.xpath('//ul[@class="productlisting-ul"]/div/li'):
            yield{
                'product_title': product.xpath('.//a[@class="p_box_title"]/text()').get(),
                'product_url': response.urljoin(product.xpath('.//a[@class="p_box_title"]/@href').get()),
                'product_initial_price': product.xpath('.//div[@class="p_box_price"]/span[contains(@class, "normalprice")]/text()').get(),
                'product_special_price': product.xpath('.//div[@class="p_box_price"]/span[contains(@class, "productSpecialPrice")]/text()').get(),
            }
        
        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page)