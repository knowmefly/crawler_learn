# -*- coding: utf-8 -*-
import scrapy

from scrapylearn.items import  ScrapylearnItem
class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/',
                  'http://sports.sina.com.cn/cba/',]

    #定义新属性
    urls2 = ['https://mil.news.sina.com.cn/china/2018-10-22/doc-ifxeuwws6829537.shtml',
             ]

    # def __init__(self,myurl=None,*args,**kwargs):
    #     super(Test1Spider,self).__init__(*args,**kwargs)
    #     #把多个网站切片处理
    #     myurllist = myurl.split("|")
    #     for i in myurllist:
    #         print("要爬取的网站是: %s" % myurl)
    #     #输出要爬的网站，对应值为接收到的参数
    #     self.start_urls=myurllist


    def start_requests(self):
        for url in self.urls2:
            yield self.make_requests_from_url(url)

    def parse(self, response):

        item = ScrapylearnItem()
        item['urlname'] = response.xpath("/html/head/title/text()")
        item['key'] = response.xpath("//meta[@name = 'keywords']/@content").extract()
        #print("以下将显示爬取网站的标题")
        #print(item['urlname'],item['key'])
        #print(response.xpath())
        yield item