# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChewyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_list=scrapy.Field()
    company=scrapy.Field()
    list_price=scrapy.Field()
    price=scrapy.Field()
    description_titles=scrapy.Field()
    description_values=scrapy.Field()
    review_count=scrapy.Field()
    rating=scrapy.Field()
    pass
