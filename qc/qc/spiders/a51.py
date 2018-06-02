# -*- coding: utf-8 -*-
import scrapy
from qc.items import QcItem


class A51Spider(scrapy.Spider):
    name = 'a51'
    # allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?']

    def parse(self, response):
        node_list = response.xpath('//div[@class="el"]')
        for node in node_list:
            # item对象必须写在这里..!
            item = QcItem()
            item['work_name'] = node.xpath('./p/span/a/@title').extract_first()
            item['company'] = node.xpath('./span/a/@title').extract_first()
            item['work_position'] = node.xpath('./span[@class="t3"]/text()').extract_first()
            item['salary'] = node.xpath('./span[@class="t4"]/text()').extract_first()
            item['publishTime'] = node.xpath('./span[@class="t5"]/text()').extract_first()

            # 前四个有可能是标题没有链接
            detail_href = node.xpath('./p/span/a/@href').extract_first()
            if detail_href is None:
                continue

            yield scrapy.Request(detail_href, callback=self.detail, meta={'item':item})

    def detail(self, response):
        item = response.meta['item']
        content1 = response.xpath('//div[@class="bmsg job_msg inbox"]/*/*/text()').extract()
        content2 = response.xpath('//div[@class="bmsg job_msg inbox"]/*/text()').extract()
        if len(content1) > len(content2):
            item['content'] = "".join(content1)
        else:
            item['content'] = "".join(content2)
        item['content'] = item['content'].strip()

        item['contact'] = "".join(response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()).strip()
        yield item