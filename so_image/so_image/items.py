# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoImageItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    index = scrapy.Field()
    image_urls = scrapy.Field()
    pass
