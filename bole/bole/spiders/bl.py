# -*- coding: utf-8 -*-
import scrapy
from bole.items import BoleItem
from scrapy_redis.spiders import RedisSpider
import re
from scrapy.loader import ItemLoader

class BlSpider(RedisSpider):
    name = 'bl'
    redis_key = 'bole:start_urls'

    def parse(self, response):
        divs = response.xpath('//div[@id="archive"]//div[@class="post-meta"]')
        for div in divs:
            item = BoleItem()
            title = div.xpath('./p[1]/a[1]/text()').extract()
            url = div.xpath('./p[2]/span/a/@href').extract()
            type = div.xpath('./p/a[2]/text()').extract()
            typeurl = div.xpath('./p[1]/a[2]/@href').extract()
            excerpt = div.xpath('./span/p/text()').extract()
            time = div.xpath('./p//text()').extract()[2].strip().replace("·", "").strip()
            title = title[0] if len(title) > 0 else '无数据'
            url = url[0] if len(url) > 0 else '无数据'
            # time = time[1] if len(time) > 0 else '无数据'
            type = type[0] if len(type) > 0 else '无数据'
            typeurl = typeurl[0] if len(typeurl) > 0 else '无数据'
            excerpt = excerpt[0] if len(excerpt) > 0 else '无数据'

            item['title'] = title
            item['url'] = url
            item['article_time'] = time
            item['article_type'] = type
            item['typeurl'] = typeurl
            item['excerpt'] = excerpt

            yield item

        for i in range(0,10):
            base_url = 'http://blog.jobbole.com/all-posts/page/{}/'.format(i)
            yield scrapy.Request(url=base_url, callback=self.parse)

            # lpush bole:start_urls http://blog.jobbole.com/all-posts/page/





