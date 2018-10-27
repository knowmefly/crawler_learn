# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HexunpjtPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="mypydb")
    def process_item(self, item, spider):
        for i in range(0, len(item["name"])):
            print(item["name"][i])
            name = item["name"][i]
            url = item["url"][i]
            hits = item["hits"][i]
            comment = item["comment"][i]
            sql = "insert into myhexun(name,url,hits,comment) VALUES('"+name+"','"+url+"', '"+hits+"', '"+comment+"')"
            self.conn.query(sql)
            self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close()