# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class ScrapylearnPipeline(object):
    #初始化
    def __init__(self):
        self.file = codecs.open("E:\program_file\python\crawler_learn\scrapylearn\mydata.json", "wb", encoding='utf-8')
        print(1)
    def process_item(self, item, spider):
        #设置每行内容
        print(dict(item))
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        self.file.write(line)
        return item
        #
        # l = str(item) + '\n'
        # print(l)
        # self.file.write(l)
        # return item
    #关闭文件
    def close_spider(self, spider):
        self.file.close()