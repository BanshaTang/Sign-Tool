#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# [('User-agent', 'Firefox')]

class Sign:
    def __init__(self, account, password, login_url, log_form_index, account_label, password_label):
        self.account = account
        self.password = password
        login_page = br.open(login_url)  #the login url
        br.select_form(nr = log_form_index) #choose the form, #0 is the first form
        br[account_label] = account #the account label HTML ID
        br[password_label] = password #the password label HTML ID

    def login_act(self):
        logged_url = br.submit()   #登陆账号
        print logged_url.geturl()

    def sign_in(self, sign_form_index): #当签到按钮是form时，用这个方法签到
        br.select_form(nr = sign_form_index)
        signed_url = br.submit()
        print signed_url.geturl()


def login():
    me_ygzj = Sign("汤思泉", "tang", "http://192.168.1.201:8081/Login.aspx", 0, "AdminName", "AdminPassword") #员工之家
    me_ygzj.login_act()
    me_ygzj.sign_in(0)

    #me_xiami = Sign("tsq1020@gmail.com", "10201020", "https://login.xiami.com/member/login", 0, "email", "password") #虾米
    #me_xiami.login_act()

    #虾米的按钮是个<b>标签，触发后的网址已经记录在evernote

login()