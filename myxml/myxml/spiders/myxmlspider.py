# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['http://www.w3school.com.cn']
    start_urls = ['http://www.w3school.com.cn/example/xmle/plant_catalog.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'CATALOG' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        i['COMMON'] = node.xpath('/CATALOG/PLANT/COMMON/text()').extract()
        i['PRICE'] = node.xpath('/CATALOG/PLANT/PRICE/text()').extract()
        i['LIGHT'] = node.xpath('/CATALOG/PLANT/LIGHT/text()').extract()
        for j in range(len(i['COMMON'])):
            print("第" + str(j+1) +"个植物")
            print("价格是：" + i['PRICE'][j])
            print("培养方式："+ i['LIGHT'][j])
        return i
