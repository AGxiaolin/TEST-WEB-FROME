# -*- coding: utf-8 -*- 
# @Time : 2021/11/18 17:25 
# @Author : 小林 
# @Site : 上海
# @File : test_login_sucess.py
import unittest
import warnings
import ddt
from selenium import webdriver
from pageobjects.Slidecenter.login_page import Slidecenter_login
from common.read_yamls import read_datas


class Test01_login(unittest.TestCase):
    def test01_sucess(self, driver=None):
        """ 成功登录 zlzhao 测试账号"""
        self.driver = driver
        username = read_datas("login")["sucess"][0]
        paword = read_datas("login")["sucess"][1]
        if self.driver == None:
            self.driver = webdriver.Chrome()
            login = Slidecenter_login(driver=self.driver)
            login.lgoin(user=username, paword=paword)
        else:
            login = Slidecenter_login(driver=self.driver)
            login.lgoin(user=username, paword=paword)
    # def openUrl(self,temWebdriver,url):
    #     temWebdriver.get(url)
    #     url =  temWebdriver.current_url
    #     home_url = "http://192.168.2.242:9800/"
    #     if home_url == url:
    #         Test01_login().test01_sucess(drivers=self.driver)
    # def test01_sucess(self):
    #     """ 成功登录 zlzhao 测试账号"""
    #     username = read_datas("login")["sucess"][0]
    #     paword = read_datas("login")["sucess"][1]
    #     login = Slidecenter_login()
    #     login.lgoin(username,paword)
# if __name__ == '__main__':
#     unittest.main()
