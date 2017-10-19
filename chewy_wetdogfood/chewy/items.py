# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChewyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category=scrapy.Field()
    product_list=scrapy.Field()
    maker=scrapy.Field()
    list_price=scrapy.Field()
    price=scrapy.Field()
    # description_titles=scrapy.Field()
    # description_values=scrapy.Field()
    itemnumber=scrapy.Field()
    weight=scrapy.Field()
    foodtexture=scrapy.Field()
    brand=scrapy.Field()
    breedsize=scrapy.Field()
    foodform=scrapy.Field()
    lifestage=scrapy.Field()
    madein=scrapy.Field()
    specialdiet=scrapy.Field()
    review_count=scrapy.Field()
    rating=scrapy.Field()
    benefits=scrapy.Field()
    ingredients=scrapy.Field()
    caloric=scrapy.Field()
    protein=scrapy.Field()
    fat=scrapy.Field()
    fibre=scrapy.Field()
    moisture=scrapy.Field()
    size=scrapy.Field()

    pass
