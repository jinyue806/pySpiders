# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from FuLian3spider.items import Fulian3SpiderItem
import random

class Fl3Spider(Spider):
    name = 'fl3'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['https://movie.douban.com/subject/24773958/comments?start={}&limit=20&sort=new_score&status=P&percent_type='.format(i)
                  for i in range(0, 100)]

    def parse(self, response):
        item = Fulian3SpiderItem()
        divs = response.xpath('//*[@id="comments"] | //*[@id="comments-info"]')
        for div in divs:
            user = div.xpath('.//div/h3/span[2]/a/text()').extract_first()
            time = div.xpath('.//div//h3/span[2]/span[3]/@title').extract_first()
            comment = div.xpath('.//p/text()').extract_first()
            watched = div.xpath('.//div/h3/span[2]/span[1]/text()').extract_first()
            votes = div.xpath('.//h3/span[1]/a/text()').extract_first()
            # rating = div.xpath('//span.allstar.rating/@title').extract_first()

            item['user'] = user
            item['time'] = time
            item['comment'] = "".join(comment).strip()
            item['watched'] = watched
            item['votes'] = votes
        yield item
        # 获取下一个评论
        next_page = response.xpath('//*[@id="paginator"]/a[3]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

# scrapy crawl fl3 -o fl3.csv 存入CSV格式文件