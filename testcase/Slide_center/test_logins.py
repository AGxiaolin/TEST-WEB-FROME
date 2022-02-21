# -*- coding: utf-8 -*- 
# @Time : 2021/12/10 12:59 
# @Author : 小林 
# @Site : 上海
# @File : test_logins.py
import unittest
import warnings
import ddt
from selenium import webdriver
from common.logger import FrameLog
from pageobjects.Slidecenter.login_page import Slidecenter_login
from base.basepage import Basepage
from pagelocations.Slideecenter_loc.loggin_page import logo_loc
from common.read_yamls import read_datas

datas = read_datas("login_datas")


@ddt.ddt
class test01_logins(unittest.TestCase):

    def setUp(self) -> None:
        self.login = Slidecenter_login(driver=webdriver.Chrome())
        print("-------")

    def tearDown(self):
        self.login.sleep(3)
        self.login.clone()

    @ddt.data(*datas)
    def test01_login(self, data):
        """ 验证账号登录组合 """
        self.logger = FrameLog().get_Logger()
        # slidecenter_login = Slidecenter_login()
        self.login.lgoin(user=data["username"], paword=data["psd"])
        self.logger.info(data["eq"])


# class TestLogin(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.datas = read_datas("login")
#     def setUp(self) -> None:
#         self.login = Slidecenter_login(driver=webdriver.Chrome())
#         print("-------")
#     def tearDown(self):
#         self.login.sleep(3)
#         self.login.clone()
#     def test01_sucess(self):
#         username = self.datas["sucess"][0]
#         passwd = self.datas["sucess"][1]
#         self.login.lgoin(username,passwd)
#     def test02_login(self):
#         user = self.datas["faile"][0][0]
#         paword =self.datas["faile"][0][1]
#         self.login.lgoin(user,paword)
#         self.login.sleep(2)
#         error_text=self.login.git_batton("登录失败提示信息",logo_loc.error_text)
#         text = "用户名或密码无效"
#         if text in error_text:
#             self.login.logger.info("用户名输入错误，密码输入正确，登录失败")
#         else:
#             print("-------------------------")
if __name__ == '__main__':
    unittest.main()
