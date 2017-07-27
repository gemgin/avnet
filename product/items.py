# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlhead = scrapy.Field()
    storeid = scrapy.Field()
    search = scrapy.Field()
    urltail = scrapy.Field()
    furl = scrapy.Field()