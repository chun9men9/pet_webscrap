import re
from scrapy import Spider, Request
from scrapy.selector import Selector
from petsmart.items import PetsmartItem


class DogFoodSpider(Spider):
    name = "dogfood_spider"
    allowed_urls = ['https://www.petsmart.com']
    start_urls = ['https://www.petsmart.com/dog/food/canned-food/?srule=best-sellers&pmin=0&sz=24&start='+ str(24*i) for i in range(2)]
    #https://www.petsmart.com/dog/food/canned-food/blue-wilderness-adult-dog-food---grain-free-natural-645.html?cgid=100245
    def parse(self, response):
        prod_urls=response.xpath('//a[@class="name-link"]/@href').extract()
        prod_urls=['https://www.petsmart.com' + url for url in prod_urls]

        for url in prod_urls:
            yield Request(url, callback=self.parse_top)

    def parse_top(self, response):
        product_path=response.xpath('//div[@class="row product-main-container product-detail"]')
        #description_path=product_path.xpath('.//div[@class="product-description"]')
        #caption_path=description_path.xpath('.//div[@class="tab-content" and @itemprop="description"]')
        description_path=product_path.xpath('.//div[@class="product-description"]//div[@class="tab-content" and @itemprop="description"]')
        product=product_path.xpath('.//h1[@class="product-name"]/text()').extract_first()
        company=product_path.xpath('.//span[@itemprop="brand"]/text()').extract_first()
        price=product_path.xpath('.//span[@class="price-sales"]/text()').extract_first()
        highlights=description_path.xpath('./text()').extract_first()
        description=caption_path.xpath('./p').extract()

        #re.sub(r'<\S{1,3}>', '', directions)
        #map(lambda txt:txt.split('\n'),deslist)
        






        #description=caption_path.xpath('.//p[1]').extract()
        
        #foodtype_head=caption_path.xpath('.//p[1]/b[1]/text()').extract()
        #foodtype=caption_path.xpath('.//p[1]/text()[2]').extract()
        
        #lifestage_head=caption_path.xpath('.//p[1]/b[2]/text()').extract()
        #lifestage=caption_path.xpath('.//p[1]/text()[3]').extract()
        
        #healthcon_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        #heatlhcon=caption_path.xpath('.//p[1]/text()[4]').extract()
        
        #flavor_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        #flavor=caption_path.xpath('.//p[1]/text()[4]').extract()

        #primary_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        #primary=caption_path.xpath('.//p[1]/text()[4]').extract()

        # nutopt_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        # nutopt=caption_path.xpath('.//p[1]/text()[4]').extract()

        # calserve_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        # calserve=caption_path.xpath('.//p[1]/text()[4]').extract()

        # weight_head=caption_path.xpath('.//p[1]/b[3]/text()').extract()
        # weight=caption_path.xpath('.//p[1]/text()[4]').extract()

        specification=caption_path.xpath('.//p[2]').extract()
        analysis=caption_path.xpath('.//p[3]').extract()






        item = PetsmartItem()
        item['product'] = product
        item['company'] = company
        item['price'] = price
        item['highlights'] = highlights
        item['description'] = description
        item['specification'] = specification
        item['analysis']=analysis

        yield item
