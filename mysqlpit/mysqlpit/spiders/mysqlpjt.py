# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysqlpit.items import MysqlpitItem
class MysqlpjtSpider(CrawlSpider):
    name = 'mysqlpjt'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow='.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = MysqlpitItem()
        i["name"] = response.xpath("/html/head/title/text()").extract()
        i["keywd"] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
