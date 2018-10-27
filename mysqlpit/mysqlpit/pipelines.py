# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpitPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="", db="mypydb")
    def process_item(self, item, spider):
        name = item["name"][0]
        keywd = item["keywd"][0]
        print(name,keywd)
        sql = "insert into mytb(title,keywd) values('"+name+"','"+keywd+"')"
        self.conn.query(sql)
        self.conn.commit()
        return item
    def close_spider(self):
        self.conn.close()
