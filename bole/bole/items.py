# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class BoleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    article_time = scrapy.Field()
    article_type = scrapy.Field()
    typeurl = scrapy.Field()
    excerpt = scrapy.Field()
