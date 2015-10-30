#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mechanize
import urllib2
import cookielib
from bs4 import BeautifulSoup
import re

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] # [('User-agent', 'Firefox')]
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj) #set cookies

xiami_login = br.open("http://www.xiami.com/web/login")  #the login url
br.select_form(nr = 0) #choose the form, #0 is the first form
br["email"] = "tsq1020@gmail.com" #the account label HTML ID
br["password"] = "10201020" #the password label HTML ID
br.submit()   #登陆账号

br.open('http://www.xiami.com/web') #到签到页面

html = br.response().read()
soup = BeautifulSoup(html) #建立soup

find_sign = soup.findAll('div', attrs={"class" : 'idh'}) #找到所有class为idh的div
signed = find_sign[1].renderContents() #第二个class为idh的div就是包含签到信息的

check_sign = '已连续签到' in html #在HTML里面查到字符

if check_sign == True:
    print "今天已签过到啦, " + signed
else:
    br.follow_link(url_regex="/web/checkin/id/(\d+)")
    br.open('http://www.xiami.com/web')
    print "成功签到, " + signed
