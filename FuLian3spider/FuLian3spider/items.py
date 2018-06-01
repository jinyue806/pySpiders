# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Fulian3SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user = scrapy.Field() # 用户

    time = scrapy.Field() # 时间

    watched =scrapy.Field() # 是否看过

    rating =scrapy.Field() # 评分

    votes =scrapy.Field()  #是否有用

    comment = scrapy.Field() # 评论

    pass
