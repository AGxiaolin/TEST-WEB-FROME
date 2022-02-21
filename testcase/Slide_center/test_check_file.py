# -*- coding: utf-8 -*- 
# @Time : 2021/12/10 16:07 
# @Author : 小林 
# @Site : 上海
# @File : test_check_file.py
import unittest

from pageobjects.Slidecenter.check_file_page import Check_file
from testcase.Slide_center.test_login_sucess import Test01_login
from selenium import webdriver
from BeautifulReport import BeautifulReport


class Test01_check_file(unittest.TestCase):

    def setUp(self) -> None:
        self.webdriver = webdriver.Chrome()

    def test01_check_file(self, webdriver=None):
        """选中切片文件，验证右侧文件信息中，切片名称是否正确 """
        Test01_login().test01_sucess(driver=self.webdriver)
        Check_file(driver=self.webdriver).check_file()

    def test02_check_files(self, webdriver=None):
        """ 选中多个切片文件，验证右侧文件信息中，选中的切片数量是否正确"""
        Test01_login().test01_sucess(driver=self.webdriver)
        Check_file(driver=self.webdriver).check_files()


if __name__ == '__main__':
    unittest.main()
