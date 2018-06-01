# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo

# Mongodb存入数据
class Fulian3SpiderPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.collection = self.client['fl3']['fl3']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

# mysql存入数据
class Fl3MysqlPipeline(object):
    def open_spider(self, spider):
        self.con = pymysql.connect(host="localhost", port=3306, database="fl3db", user="root", password="qwe123", charset="utf8")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        sql = ("insert into fl3(user,time,comment,votes,watched)" \
               "values (%s, %s, %s, %s, %s)")
        list_item = [item['user'], item['time'], item['comment'], item['votes'], item['watched'],
                     ]

        print('*' * 3, '数据正在抓取中', '*' * 3)  # 这里一定要打印sql来看看sql是否正确，
        self.cur.execute(sql, list_item)
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.con.close()
# CREATE TABLE fl3 (user VARCHAR(100) NOT NULL,time DATETIME DEFAULT "1111-11-11 11:11:11",comment VARCHAR(999),votes VARCHAR(100),watched VARCHAR(100));