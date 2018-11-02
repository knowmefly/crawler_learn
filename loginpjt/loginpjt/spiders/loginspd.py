# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    #start_urls = ['http://douban.com/login']

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"}

    def start_requests(self):
        #第一次登陆网页
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1},callback=self.parse
                )]
    def parse(self, response):
        #获取验证码地址
        captcha = response.xpath('img[@id="captcha_image"]/@src').extract()
        #如果有验证码
        if len(captcha)>0:
            print("此处有验证码:")
            #将图片验证码保存在本地
            localpath = "E:\program_file\python\crawler_learn\loginpjt\captcha.png"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看图片输入对应验证码：")
            captcha_value = input()
            #设置要传递的post信息
            data = {
                #设置登陆账号
                "form_email":"15963020715",
                "form_password":"1998624",
                #设置验证码
                "captcha-solution":captcha_value,
                #设置需要转向地址
                "redir":"https://www.douban.com/people/172627333/",
            }
        else:
            print("此处没有验证码")
            #设置要传递的post信息
            data ={
                #设置登陆账号
                "form_email":"15963020715",
                "form_password":"1998624",
                #设置需要转向地址
                "redir":"https://www.douban.com/people/172627333/",
            }
        print("登陆中。。。")
        #通过FormRequest.from_response()登陆
        # return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]},
        #                                      formdata=data,
        #                                      callback=self.next)]
        return [

            FormRequest.from_response(response,meta={"cookiejar":response.meta["cookiejar"]},headers = self.header,formdata=data,callback=self.next,
             )
        ]

    def next(self,response):
        print(response.__dict__)
        # print("已完成登陆并爬取")
        # xtitle="html/head/title/text()"
        # xnotetitle="//div[@class='note-header p12']/a/@title"
        # xnotetime="//dic[@class='note-header p12']//span[@class='p1']/text()"
        # xnotecontent="//div[@class='mbtr2']/div[@class='note']/text()"
        # xnoteurl="//div[@class='note-header pl2']/a/@href"
        #
        # title = response.xpath(xtitle).extract()
        # print(title[0])
        # notetitle = response.xpath(xnotetitle).extract()
        # notetime = response.xpath(xnotetime).extract()
        # notecontent = response.xpath(xnotecontent).extract()
        # noteurl = response.xpath(xnoteurl).extract()
        #
        # print("网页标题是:" + title[0])
        # for i in range(0, len(notetitle)):
        #     print("第"+str(i+1)+"篇文章：")
        #     print("文章标题为：" + notetitle[i])
        #     print("文章发表时间为:" + notetime[i])
        #     print("文章内容为：" + notecontent[i])
        #     print("文章链接为:" + noteurl)
        #     print("-------------")