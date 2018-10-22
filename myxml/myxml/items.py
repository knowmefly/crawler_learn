# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyxmlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #存储植物名称
    COMMON = scrapy.Field()
    #存储价格
    PRICE = scrapy.Field()
    #存储培养方法
    LIGHT = scrapy.Field()