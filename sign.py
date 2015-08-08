#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# [('User-agent', 'Firefox')]

ygzj_login = br.open("http://192.168.1.201:8081/Login.aspx")  #the login url

br.select_form(nr = 0) #choose the form, #0 is the first form

br["AdminName"] = "汤思泉" #the account label HTML ID
br["AdminPassword"] = "tang" #the password label HTML ID
login = br.submit()   #登陆账号
login_check = login.read()
print login_check


#br.select_form(nr = 0)
#br.submit()   #签到/签退



#req = br.open("http://school.dwit.edu.np/mod/assign/").read() #accessing other url(s) after login is done this way
