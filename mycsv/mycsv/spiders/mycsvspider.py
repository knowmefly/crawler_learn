# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem
class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    headers = ['name', 'sex', 'addr', 'email']
    # delimiter = '\t'
    delimiter =','
    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].endode()
        print("名字是：" +i['name'])
        print("性别是：" +i['sex'])
        print("_________________")
        return i
