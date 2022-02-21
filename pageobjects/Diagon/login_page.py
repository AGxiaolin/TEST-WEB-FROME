# -*- coding: utf-8 -*- 
# @Time : 2021/11/17 10:14 
# @Author : 小林 
# @Site : 上海
# @File : login_page.py
from base.basepage import Basepage
from pagelocations.Diagon_loc.loggin_page import login_loc


class LoginPage(Basepage):

    def logins(self, user, paword):
        self.get_url(url=login_loc.home_url)
        self.sleep(4)
        self.input(page_name="登录页面", loc=login_loc.user, value=user)
        self.sleep(1)
        self.input(page_name="登录页面", loc=login_loc.password, value=paword)
        self.sleep(1)
        self.click(page_name="登录页面", loc=login_loc.action)
