import re
from scrapy import Spider, Request
from scrapy.selector import Selector
from chewy_reviews.items import ChewyReviewsItem

def clean_lis(lisproc):
    lisproc=map(lambda p:p.replace('\n','').strip(' ').lower(),lisproc)
    return(lisproc)
def clean_str(strproc):
    return(strproc.strip('\n').strip(' '))

class ReviewSpider(Spider):
    name = "review_wetdogfood_spider"
    allowed_urls = ['https://www.chewy.com']
    start_urls = ['https://www.chewy.com/s?rh=c%3A288%2Cc%3A332%2Cc%3A293&page='+ str(i) for i in range(1,37)]
    
    def parse(self, response):
        prod_urls=response.xpath('//section[@class="results-products"]/article[@class="product-holder  cw-card cw-card-hover"]/a/@href').extract()
        prod_urls=['https://www.chewy.com' + url for url in prod_urls]

        for url in prod_urls:
            yield Request(url, callback=self.parse_top)

    def parse_top(self, response):

        main_path=response.xpath('//main[@class="main-content"]')
        rightcol_path=main_path.xpath('.//section[@id="right-column"]')
        description_path=main_path.xpath('.//article[@id="descriptions"]')

        category=main_path.xpath('./nav[@class="breadcrumbs container"]//li/a/text()').extract()
        #product_list=map(lambda p:p.strip('\n').strip(' '),product_list)
        maker=rightcol_path.xpath('.//div[@id="product-subtitle"]/a/text()').extract_first()
        #maker=maker.strip('\n').strip(' ').strip('^By ')
        maker=clean_str(maker)
        
        description_titles=description_path.xpath('./section[@class="descriptions__content cw-tabs__content--right"]//div[@class="title"]/text()').extract()
        description_values=description_path.xpath('./section[@class="descriptions__content cw-tabs__content--right"]//div[@class="value"]/text()').extract()
        description_titles=clean_lis(description_titles)
        description_values=clean_lis(description_values)
        
        
        description_titles=map(lambda t: re.sub(' ','',t),description_titles)
        
        #re.sub(r'<\S{1,3}>', '', directions)
        #map(lambda txt:txt.split('\n'),deslist)
        #item = ChewyReviewsItem()
        if (len(description_titles)==len(description_values)): #and set(description_titles).issubset(all_titles)):
             for i in range(len(description_titles)):
                if(description_titles[i] == 'itemnumber'):
                    itemnumber=description_values[i]
        
        #yield item

        review_url=response.xpath('//footer[@class="ugc-list__footer js-read-all"]/a/@href').extract_first()
        review_url='https://www.chewy.com'+review_url
        yield Request(review_url, callback=self.parse_review, meta={'maker':maker,'itemnumber':itemnumber,'category':category})

    def parse_review(self, response):
        maker=response.meta['maker']
        itemnumber=response.meta['itemnumber']
        category=response.meta['category']
        review_title=response.xpath('//section[@class="ugc-rev__helpful__block__body"]//h3[@class="ugc__title"]/span[2]/text()').extract()
        review_content=response.xpath('//section[@class="ugc-rev__helpful__block__body"]//span[@class="ugc-list__review__display"]/text()').extract()
        review_full_content=response.xpath('//section[@class="ugc-rev__helpful__block__body"]//span[@class="ugc-list__review__full"]/text()').extract()
        item = ChewyReviewsItem()
        if(len(review_full_content)>0):
            for i in range(len(review_full_content)):
                item['review_full_content_'+str(i)]=review_full_content[i]
        item['pos_review_content']=review_content[0]
        item['neg_review_content']=review_content[1]
        item['pos_review_title']=review_title[0]
        item['neg_review_title']=review_title[1]
        item['maker']=maker
        item['category']=category
        item['itemnumber']=itemnumber
        yield item
