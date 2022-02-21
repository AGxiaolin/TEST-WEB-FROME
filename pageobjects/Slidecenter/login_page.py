# -*- coding: utf-8 -*- 
# @Time : 2021/11/18 17:19 
# @Author : 小林 
# @Site : 上海
# @File : login_page.py
from base.basepage import Basepage
from pagelocations.Slideecenter_loc.loggin_page import logo_loc


class Slidecenter_login(Basepage):

    def lgoin(self, user, paword):
        # 打开浏览器窗口
        self.get_url(url=logo_loc.home_url)
        self.sleep(2)
        self.input(page_name="登录页面", loc=logo_loc.user, value=user)
        self.sleep(1)
        self.input(page_name="登录页面", loc=logo_loc.paword, value=paword)
        self.sleep(1)
        self.click(page_name="登录页面", loc=logo_loc.login_action)
