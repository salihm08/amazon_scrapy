# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    pnme = scrapy.Field()
    descp = scrapy.Field()
    price = scrapy.Field()
    img = scrapy.Field()
    rating = scrapy.Field()