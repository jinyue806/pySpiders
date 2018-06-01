# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from FuLian3spider.items import Fulian3SpiderItem

class Fl3Spider(Spider):
    name = 'fl3'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'https://movie.douban.com/subject/24773958/comments?start=0&limit=20&sort=new_score&status=P&percent_type='
        yield Request(url, headers=self.headers)

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

            item['user'] = user if len(user) > 0 else '无数据'
            item['time'] = time
            item['comment'] = "".join(comment).strip()
            item['watched'] = watched
            item['votes'] = votes

        # yield item
        # 获取下一个评论
        for i in range(1,480):
            next_url = 'https://movie.douban.com/subject/24773958/comments?start={}&limit=20&sort=new_score&status=P&percent_type='.format(i)
            yield Request(next_url, headers=self.headers,callback=self.parse)
            yield item



# scrapy crawl fl3 -o fl3.csv 存入CSV格式文件