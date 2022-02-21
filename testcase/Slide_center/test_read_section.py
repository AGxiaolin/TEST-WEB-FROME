# -*- coding: utf-8 -*- 
# @Time : 2021/11/22 16:10 
# @Author : 小林 
# @Site : 上海
# @File : test_read_section.py
import time
import unittest

from common.logger import FrameLog
from pageobjects.Slidecenter.section_list_home_page import Open_files_home, Read_section, Right_clicks
from testcase.Slide_center.test_login_sucess import Test01_login
from selenium import webdriver


class Test_Read_section(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Test01_login().test01_sucess(driver=self.driver)
        self.home = Open_files_home(driver=self.driver)

    def test01_read_section(self):
        """ 通过【开始阅片】按钮，进入到切片浏览界面"""
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 选择第一个文件，
        self.home.click_one_section()
        open_section_name = self.home.result_text()
        # 点击开始阅片
        self.home.read_section()
        # 断言打开的切片是否与实际打开的切片一致
        try:
            section_name = Read_section(driver=self.driver).section_name_text()
            self.assertEqual(open_section_name, section_name)
        except:
            FrameLog().get_Logger().error(f"断言失败，操作打开的切片：{open_section_name}，与实际打开的切片：{section_name} 不相等")

    def test02_double_click_section(self):
        """ 通过双击切片文件，进入到切片浏览界面"""
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 获取第一个文件的文本信息
        open_section_name = self.home.result_text()
        # 双击切片，进入到切片页面
        Read_section(driver=self.driver).double_click_section()
        # 断言打开的切片是否与实际打开的切片一致
        try:
            section_name = Read_section(driver=self.driver).section_name_text()
            self.assertEqual(open_section_name, section_name)
        except:
            FrameLog().get_Logger().error(f"断言失败，操作打开的切片：{open_section_name}，与实际打开的切片：{section_name} 不相等")

    def test03_context_read_section(self):
        """ 通过鼠标右键菜单，点击开始阅片，进行阅片"""
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 选择第一个文件，
        self.home.click_one_section()
        # 获取第一个文件的文本信息
        open_section_name = self.home.result_text()
        # 鼠标右键点击第一张切片
        Right_clicks(driver=self.driver).right_click_section()
        # 点击开始阅片
        Right_clicks(driver=self.driver).context_read_section()
        try:
            section_name = Read_section(driver=self.driver).section_name_text()
            self.assertEqual(open_section_name, section_name)
        except:
            FrameLog().get_Logger().error(f"断言失败，操作打开的切片：{open_section_name}，与实际打开的切片：{section_name} 不相等")

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
