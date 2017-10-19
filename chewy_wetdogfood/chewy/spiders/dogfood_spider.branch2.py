import re
from scrapy import Spider, Request
from scrapy.selector import Selector
from chewy.items import ChewyItem
all_titles=['itemnumber','weight','foodtexture','brand','breedsize','foodform','lifestage','madein','specialdiet']
def clean_lis(lisproc):
    lisproc=map(lambda p:p.replace('\n','').strip(' ').lower(),lisproc)
    return(lisproc)
def clean_str(strproc):
    return(strproc.strip('\n').strip(' '))

class DogFoodSpider(Spider):
    name = "dogfood_spider"
    allowed_urls = ['https://www.chewy.com']
    start_urls = ['https://www.chewy.com/s?rh=c%3A288%2Cc%3A332%2Cc%3A293&page='+ str(i) for i in range(37)]
    
    
    def parse(self, response):
        prod_urls=response.xpath('//section[@class="results-products"]/article[@class="product-holder  cw-card cw-card-hover"]/a/@href').extract()
        prod_urls=['https://www.chewy.com' + url for url in prod_urls]

        for url in prod_urls:
            yield Request(url, callback=self.parse_top)

    def parse_top(self, response):

        #product_path=response.xpath('//div[@class="row product-main-container product-detail"]')
        main_path=response.xpath('//main[@class="main-content"]')
        rightcol_path=main_path.xpath('.//section[@id="right-column"]')
        price_path=rightcol_path.xpath('.//div[@class="buybox-wrapper"]//ul[@class="product-pricing"]')
        description_path=main_path.xpath('.//article[@id="descriptions"]')
        rating_path=main_path.xpath('//header[@itemprop="aggregateRating"]')

        category=main_path.xpath('./nav[@class="breadcrumbs container"]//li/a/text()').extract()
        product_list=rightcol_path.xpath('.//div[@id="product-title"]/h1/text()').extract_first()
        product_list=product_list.split(',')
        product_list=clean_lis(product_list)
        #product_list=map(lambda p:p.strip('\n').strip(' '),product_list)
        company=rightcol_path.xpath('.//div[@id="product-subtitle"]/a/text()').extract_first()
        #company=company.strip('\n').strip(' ').strip('^By ')
        company=clean_str(company)
        company=company.strip('^By ')
        list_price=price_path.xpath('./li[@class="list-price"]/p[@class="price"]/text()').extract_first()
        #list_price=list_price.strip('\n').strip(' ')
        #list_price=clean_str(list_price)
        price=price_path.xpath('./li[@class="our-price"]/p[@class="price"]/span[@class="ga-eec__price"]/text()').extract_first()
        
        description_titles=description_path.xpath('./section[@class="descriptions__content cw-tabs__content--right"]//div[@class="title"]/text()').extract()
        description_values=description_path.xpath('./section[@class="descriptions__content cw-tabs__content--right"]//div[@class="value"]/text()').extract()
        description_titles=clean_lis(description_titles)
        description_values=clean_lis(description_values)
        review_count=rating_path.xpath('.//span[@class="ugc-list__header--reviews ugc-list__header--reviews--page"]/span[@itemprop="reviewCount"]/text()').extract_first()
        rating=rating_path.xpath('.//span[@class="ugc-list__header--count"]/span[@itemprop="ratingValue"]/text()').extract_first()
        
        description_titles=map(lambda t: re.sub(' ','',t),description_titles)
        #re.sub(r'<\S{1,3}>', '', directions)
        #map(lambda txt:txt.split('\n'),deslist)
        item = ChewyItem()
        item['product_list'] = product_list
        item['company'] = company
        item['list_price'] = list_price
        item['price'] = price
        #item['description_titles'] = description_titles
        #item['description_values'] = description_values
        if (len(description_titles)==len(description_values)): #and set(description_titles).issubset(all_titles)):
             for i in range(len(description_titles)):
                if(description_titles[i] in all_titles):
                    item[description_titles[i]]=description_values[i]
        

        item['review_count']=review_count
        item['rating']=rating
        #item['highlights'] = highlights
        #item['specification'] = specification
        yield item
