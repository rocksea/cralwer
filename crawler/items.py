# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverKinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qTitle = scrapy.Field()
    qContent = scrapy.Field()
    aContent = scrapy.Field()
    aDt= scrapy.Field()
    qDt= scrapy.Field()
    pass
