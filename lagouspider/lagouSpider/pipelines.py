# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo

class LagouspiderPipeline(object):
    def open_spider(self, spider):
        self.con = pymysql.connect(host="localhost", port=3306, database="lagou", user="root", password="qwe123", charset="utf8")
        self.cur = self.con.cursor()


    def process_item(self, item, spider):
        sql = ("insert into lagou(title,address,money,company,fintance)" \
               "values (%s, %s, %s, %s, %s)")
        list_item = [item['job_title'],item['job_address'],item['job_money'],item['job_company'],item['job_fintance']]

        print('*'*3,'数据正在抓取中','*'*3) # 这里一定要打印sql来看看sql是否正确，
        self.cur.execute(sql,list_item)
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.con.close()

class QcMongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.collection = self.client['lagou']['lagou']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

# CREATE TABLE lagou (title VARCHAR(100) NOT NULL,address VARCHAR(150),money VARCHAR(10),company VARCHAR(100),fintance VARCHAR(100));
#  #创建表的命令，可以直接复制粘贴上去



