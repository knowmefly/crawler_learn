# -*- coding: utf-8 -*-
import scrapy
import re
from qtprj.items import QtprjItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.com/tb']

    def parse(self, response):
        item = QtprjItem()
        #获取图片链接
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        item["picurl"] = re.compile(paturl).findall(str(response.body))
        #获取文件名
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item["picid"] = re.compile(patlocal).findall(str(response.body))
        yield item

        for i in range(1,2):
            nexturl = "http://58pic.com/tb/id-"+str(i)+".html"
            yield Request(nexturl, callback=self.parse)
