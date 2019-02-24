import urllib.request as request
import re
import time 
import urllib.error as error

#模拟浏览器
headers = ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.106 Chrome/68.0.3440.106 Safari/537.36')
opener = request.build_opener()
opener.addheaders = [headers]
#将openern安装为全局
request.install_opener(opener)
listurl = []
#使用代理服务器
def use_proxy(proxy_addr,url):
    #异常处理
    try:
        proxy = request.ProxyHandler({'http':proxy_addr})
        opener = request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)
        data = request.urlopen(url).read().decode('utf-8')
        time.sleep(3)
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
#获取所有文章链接
def getlisturl(key,pagestart,pageend,proxy):
    try:
        page = pagestart
        keycode = request.quote(key)
        pagecode = request.quote("&page")
        for page in range(pagestart, pageend+1):
            #构架各页url
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+"&page=" +str(page)
            print(url)
            data1 = use_proxy(proxy, url)
            print(data1)
            #获取文章链接正则表达式
            listurlpat = '<div class="img-box".*?(http://.*?)"'
            #将每个链接加入listurl
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
            print (listurl)
        print("共找到"+str(len(listurl))+"页")
        return listurl
    except error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

#通过链接获取相关内容
def getcontent(listurl,proxy):
    i = 0
    html1 = '''<html>
    <head>
    <title>微信文章</title>
    </head>
<body>
'''
    fh = open("myweb/5.html", "wb")
    fh.write(html1.encode('utf-8'))
    fh.close()
    fh = open("myweb/5.html", "ab")
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url = listurl[i][j]
                url = url.replace("amp;","")
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
                print(" 第 "+str(i)+" 个网页 第" +str(j)+ "次处理")
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
    fh = open("myweb/5.html", "ab")
    fh.write(html2.encode('utf-8'))
    fh.close()
#设置关键词
key = "戏精本精"
proxy = "115.151.1.144:9999"
proxy2= "110.52.235.34:9999"
pagestart = 1
pageend = 2
listurl = getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy2)