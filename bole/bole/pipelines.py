# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BolePipeline(object):
    def open_spider(self, spider):
        self.con = pymysql.connect(host="localhost", port=3306, database="bl", user="root", password="qwe123", charset="utf8")
        self.cur = self.con.cursor()


    def process_item(self, item, spider):
        sql = ("insert into bl(title,url,time,type,typeurl,excerpt)" \
               "values (%s, %s, %s, %s, %s,%s)")
        list_item = [item['title'],item['url'],item['article_time'],item['article_type'],item['typeurl'],item['excerpt']]

        print('*'*3,'数据正在抓取中','*'*3) # 这里一定要打印sql来看看sql是否正确，
        self.cur.execute(sql,list_item)
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.con.close()

# CREATE TABLE bl (title VARCHAR(100) NOT NULL,url VARCHAR(150),time VARCHAR(10),type VARCHAR(100),typeurl VARCHAR(100),excerpt VARCHAR(999));