#coding=utf8
import cookielib, urllib2, urllib
import random
from parseHTML import parseHTML
__author__ = "Also"

def login(stuid = None, pwd = None):  #用户名还是我自己的
    #登陆选课网站
    cj = cookielib.CookieJar()#详见cookielib
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    exheaders = [("User-Agent","Mozilla/4.0 (compatible; MSIE 7.1; Windows NT 5.1; SV1)"),] #加入头信息
    opener.addheaders=exheaders
    url_login = 'http://202.115.47.133:7777/pls/wwwbks/bks_login2.login'
    post_data = (('stuid',stuid), ('pwd',pwd)) #TODO:更改登录名和密码
    req1 = opener.open(url_login, urllib.urlencode(post_data))  #这时，cookie已经进来了。
    url_course = "http://202.115.47.133:7777/pls/wwwbks/bkscjcx.yxkc"
    req2 = opener.open(url_course) #打开课程页面
    data2 = req2.read() #读取课程页面
    return data2.decode('gbk').encode('utf8') #要decode，否则为乱码

def crack(stuid, pwd):
    if parseHTML(login(stuid, pwd)) == 1:
        #print pwd,"error"
        return False
    else:
        print pwd,"succees!"
        return True


if __name__ == '__main__':
    pass
