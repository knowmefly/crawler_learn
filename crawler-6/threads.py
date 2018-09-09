import queue
import threading
import re
import urllib.request as request
import time
import urllib.error as error

urlqueue = queue.Queue()
#模拟浏览器
headers = ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.106 Chrome/68.0.3440.106 Safari/537.36')
opener = request.build_opener()
opener.addheaders = [headers]
#将openern安装为全局
request.install_opener(opener)
listurl = []
#使用代理服务器
def use_proxy(proxy_addr,url):
    import urllib.request as request
    #异常处理
    try:
        proxy = request.ProxyHandler({'http':proxy_addr})
        opener = request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)
        data = request.urlopen(url).read().decode('utf-8')
        return data
    except error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("ecception:"+str(e))
        time.sleep(1)
#线程1，获取对应网站并放入url队列
class geturl(threading.Thread):
    def __init__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue=urlqueue
        self.key = key
    def run(self):
        page = self.pagestart
        #编码key
        keycode = request.quote(key)
        #编码page
        pagecode = request.quote("&page")
        for page in range(pagestart, pageend+1):
            #构架各页url
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+"&page=" +str(page)
            #print(url)
            data1 = use_proxy(proxy, url)
            #获取文章链接正则表达式
            listurlpat = '<div class="img-box".*?(http://.*?)"'
            #将每个链接加入listurl
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("共找到"+str(len(listurl))+"页")
        for i in range(0,len(listurl)):
            time.sleep(7)
            for j in range(0,len(listurl[i])):
                try:
                    url = listurl[i][j]
                    #处理url多余元素
                    url = url.replace("amp;", "")
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except error.URLError as e:
                    if hasattr(e,"code"):
                        print(e.code)
                    if hasattr(e,"reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception:"+str(e))
                    time.sleep(1)
#线程2与线程1并行执行，获取到url并对文章信息处理
class getcontent(threading.Thread):
    def __init__(self,urlqueue,proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy
    def run(self):
        html1 = '''<html>
    <head>
    <title>微信文章</title>
    </head>
<body>
'''
        fh = open("myweb/6.html", "wb")
        fh.write(html1.encode('utf-8'))
        fh.close()
        fh = open("myweb/6.html", "ab")
        i = 1
        while(True):
            try:
                url = self.urlqueue.get()
                data = use_proxy(proxy, url)
                #文章标题正则
                titlepat = '<title>(.*?)</title>'
                #文章内容正则
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat, re.S).findall(data)
                content = re.compile(contentpat, re.S).findall(data)
                #初始化标题和内容
                thistitle = " 此次没有获取到 "
                thiscontene = " 内容没有找到 "
                if(title!= []):
                    thistitle = title[0]
                if(content!= []):
                    thiscontene = content[0]
                #内容合并
                dataall = "<p>标题为" + thistitle + "</p><p>内容为：" + thiscontene + "</p><br>"
                #内容写入
                fh.write(dataall.encode('utf-8'))
                print(" 第 "+str(i)+" 个网页处理")
                i+=1
            except error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                time.sleep(1)
        fh.close()
        html2 = '''</body>
        </html>
        '''
        fh = open("myweb/6.html", "ab")
        fh.write(html2.encode('utf-8'))
        fh.close()
class control(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
    def run (self):
        while(True):
            print("程序执行中...")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("程序执行完毕！")
                quit()
key = "人工智能"
proxy = "61.138.33.20:808"
proxy2 = "118.190.199.55:80"
#爬取页规定
pagestart = 1
pageend = 10
#创建线程1启动线程1
t1 = geturl(key,pagestart,pageend,proxy,urlqueue)
t1.start()
#创建线程2
t2 = getcontent(urlqueue,proxy2)
t2.start()
#创建线程3并启动
t3 = control(urlqueue)
t3.start()