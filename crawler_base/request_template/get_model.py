import requests

#搜索查询
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

#爬取图片
import os 
url = "http://t2.hddhhn.com/uploads/tu/201801/9999/04fd84a337.jpg"
root = "pic/"
path = root +url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬取失败")

#查询IP地址
url = "http://m.ip138.com/ip.asp?ip="
try:
	r = requests.get(url+'61.135.169.125')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except:
	print("爬取失败")