import urllib2
import cookielib
 
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    print "cookie field " + item.name + " : " + item.value

response = urllib2.urlopen('http://www.baidu.com')

print response.headers