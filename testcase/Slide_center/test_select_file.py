# -*- coding: utf-8 -*- 
# @Time : 2022/2/11 18:33 
# @Author : 小林 
# @Site : 上海
# @File : test_select_file.py
import time
import unittest

from selenium import webdriver

from base.basepage import Basepage
from common.logger import FrameLog
from pagelocations.Slideecenter_loc.home_page import Select_file_page
from pageobjects.Slidecenter.section_list_home_page import Open_files_home
from testcase.Slide_center.test_login_sucess import Test01_login


class Test_Select_file(unittest.TestCase):
    u"""测试基本搜索框的用例集合"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Test01_login().test01_sucess(driver=self.driver)
        self.home = Open_files_home(driver=self.driver)
        self.name = "aaa"

    def test01_select_yuncunchu(self):
        """登录成功，在云存储中搜索名称为aaa的切片"""
        #  输入搜索内容 name
        self.home.select_bok(name=self.name)
        # 断言 搜索到的第一条数据是否包含搜索的字符name
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")

    def test02_select_myfiles(self):
        """登录成功，在云存储中搜索名称为aaa的切片"""
        # 登录成功，点击下拉框
        self.home.yuncunchu_xiala()
        # 选择需要操作的文件夹
        self.home.open_files()
        #  输入搜索内容 name
        self.home.select_bok(name=self.name)
        # 断言 搜索到的第一条数据是否包含搜索的字符name
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")
        pass

    def test03_select_myfiles_yuncunchu(self):
        """ 在选择的文件夹中搜索为aaa的切片，切换到云存储搜索 """
        # 点击云存储下拉框
        self.home.yuncunchu_xiala()
        # 点击需要操作的文件夹
        self.home.open_files()
        # 在基本搜索框中，输入搜索内容
        self.home.select_bok(name=self.name)
        self.home.select_myfiles_yuncunchu(name=self.name)
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")

    def test04_select_myfiles_read_section(self):
        """ 在云存储搜索结果中，选择第一张切片进行阅片"""
        #  输入搜索内容 name
        self.home.select_bok(name=self.name)
        # 断言 搜索到的第一条数据是否包含搜索的字符name
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")
        # 点击第一张切片
        self.home.click_one_section()
        time.sleep(1)
        # 开始阅片
        self.home.read_section()
        pass

    def test05_select_myfiles_read_section(self):
        """ 在选择的文件夹中搜索，选择第一张切片进行阅片"""
        # 点击云存储下拉框
        self.home.yuncunchu_xiala()
        # 选择需要操作的文件夹
        self.home.open_files()
        #  输入搜索内容 name
        self.home.select_bok(name=self.name)
        # 断言 搜索到的第一条数据是否包含搜索的字符name
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")
        # 点击第一张切片
        self.home.click_one_section()
        # 开始阅片
        self.home.read_section()
        try:
            ret_text = self.home.get_element_text("获取标注文本", Select_file_page.labels_loc)
            self.assertEqual("标注", ret_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，获取的文本信息{ret_text}不等于“标注")

    def test06_select_select_myfiles_yuncunchu(self):
        """ 在选择的文件夹中搜索为aaa的切片，切换到云存储搜索，选择第一张切片进行阅片 """
        self.home.yuncunchu_xiala()
        # 点击需要操作的文件夹
        self.home.open_files()
        # 在基本搜索框中，输入搜索内容
        self.home.select_bok(name=self.name)
        self.home.select_myfiles_yuncunchu(name=self.name)
        try:
            result_text = self.home.result_text()
            self.assertIn(self.name, result_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，输入的{self.name}不在：{result_text} 字符串中")
        self.home.click_one_section()
        self.home.read_section()
        try:
            ret_text = self.home.get_element_text("获取标注文本", Select_file_page.labels_loc)
            self.assertEqual("标注", ret_text)
        except:
            FrameLog().get_Logger().error(f"断言失败，获取的文本信息{ret_text}不等于“标注")

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
