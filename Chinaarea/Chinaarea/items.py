# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaareaItem(scrapy.Item):
    # 城市
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 空气质量指数
    aqi = scrapy.Field()
    # 空气质量等级
    level = scrapy.Field()
    # pm2.5
    pm2_5 = scrapy.Field()
    # pm10
    pm10 = scrapy.Field()
    # 二氧化硫
    so2 = scrapy.Field()
    # 一氧化碳
    co = scrapy.Field()
    # 二氧化氮
    no2 = scrapy.Field()
    # 臭氧
    o3 = scrapy.Field()
    # 数据源
    source = scrapy.Field()
    # utctime
    utc_time = scrapy.Field()