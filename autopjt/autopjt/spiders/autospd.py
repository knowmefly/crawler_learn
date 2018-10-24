# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4011029.html']

    def parse(self, response):
        #xpath提取内容
        item = AutopjtItem()
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        #print(item["link"])
        item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item
        #通过循环爬取10页数据
        for i in range(1,3):
            url = "http://category.dangdang.com/pg" +str(i)+"-cid4011029.html"
            #通过yield返回Request，并指定要爬取的网站和回调函数
            yield Request(url, callback=self.parse)