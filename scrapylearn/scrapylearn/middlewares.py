#middlewares  下载中间件
import random
#导入IPPOOL
from scrapylearn.settings import IPPOOL
#导入官网模块
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    #初始化
    def __init__(self, ip =''):
        self.ip = ip
    #process_request()  处理请求
    def process_request(self, request, spider):
        #随机选择IP
        thisip = random.choice(IPPOOL)
        #输出调用IP
        print("当前使用的IP是：" + thisip["ipaddr"])
        #代理访问
        request.meta["proxy"] = "http://" + thisip["ipaddr"]
