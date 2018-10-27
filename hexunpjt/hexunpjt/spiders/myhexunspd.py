# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request

class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    start_urls = ['http://hexun.com/']
    uid = "19940007"
    def start_requests(self):
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html", headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"})

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        #评论数、点击数网址正则表达式
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        #print(hcurl)

        header2 = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [header2]
        #opener安装为全局
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(hcurl).read()
        #阅读数与评论数正则表达式
        pat2 = "click\d*?','(\d*?)'"
        pat3 = "comment\d*?','(\d*?)'"
        #提取阅读数、评论数并赋值
        item["hits"] = re.compile(pat2).findall(str(data))
        item["comment"] = re.compile(pat3).findall(str(data))
        yield item
        #提取总页数
        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))
        if(len(data2)>=2):
            totalurl = data2[-2]
        else:
            totalurl = 1
        print("一共"+str(totalurl)+"页")
        for i in range(2,int(totalurl)+1):
            nexturl = "http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"

            yield Request(nexturl,callback=self.parse,headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"})
            print("当前爬取到：" + str(i) + "页")