import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({"name":"123", "pass":"324"})
req = urllib.request.Request(url,postdata)
req.add_header(Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/61.0)
data = urllib.request.urlopen(req).read()
fhandle = open("Documents/myweb/2.html", "wb")
fhandle.write(data)
fhandle.close()