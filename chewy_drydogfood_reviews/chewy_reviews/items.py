# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChewyReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category=scrapy.Field()
    maker=scrapy.Field()
    itemnumber=scrapy.Field()
    pos_review_content=scrapy.Field()
    pos_review_title=scrapy.Field()
    neg_review_content=scrapy.Field()
    neg_review_title=scrapy.Field()
    review_full_content_0=scrapy.Field()
    review_full_content_1=scrapy.Field()
    pass
