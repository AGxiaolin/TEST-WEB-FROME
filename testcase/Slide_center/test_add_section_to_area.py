# -*- coding: utf-8 -*- 
# @Time : 2022/2/16 17:49 
# @Author : 小林 
# @Site : 上海
# @File : test_add_section_to_area.py
import time
import unittest

from selenium import webdriver

from common.logger import FrameLog
from pageobjects.Slidecenter.section_list_home_page import Open_files_home, Right_clicks, Open_Click_Section
from testcase.Slide_center.test_login_sucess import Test01_login


class Test_Add_section_to_area(unittest.TestCase):
    pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Test01_login().test01_sucess(driver=self.driver)
        self.home = Open_files_home(driver=self.driver)

    def test01_add_section_to_area(self):
        """ 在存储管理，切片列表中，选择切片，加入待阅片区"""
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 选择第一个文件，
        self.home.click_one_section()
        # 获取待阅片区中切片的数量
        section_num = self.home.get_area_num()
        # 鼠标右键点击选择的切片文件
        # Right_clicks(driver=self.driver).right_click_section()
        # 点击加入待阅片区
        self.home.add_to_area()
        # Right_clicks(driver=self.driver).add_section_to_area()
        try:
            # 获取选择切片加入待阅片区后的切片数量是否正确
            section_num_two = self.home.get_area_num()
            self.assertEqual(section_num + 1, section_num_two)
            FrameLog().get_Logger().info(f"断言成功，加入前的切片数量+1：{section_num + 1} = 加入后的切片数量{section_num_two}")
            print("--------------------------------------")
        except:
            FrameLog().get_Logger().error(f"断言失败，加入前的切片数量+1：{section_num + 1}！=加入后的切片数量{section_num_two}")
        pass

    def test02_context_add_section_to_area(self):
        """ 在存储管理，切片列表中，鼠标右键选择切片，加入待阅片区 """
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 选择第一个文件，
        self.home.click_one_section()
        # 获取待阅片区中切片的数量
        section_num = self.home.get_area_num()
        # 鼠标右键点击选择的切片文件
        Right_clicks(driver=self.driver).right_click_section()
        # 点击加入待阅片区
        Right_clicks(driver=self.driver).add_section_to_area()
        try:
            # 获取选择切片加入待阅片区后的切片数量是否正确
            section_num_two = self.home.get_area_num()
            self.assertEqual(section_num + 1, section_num_two)
            FrameLog().get_Logger().info(f"断言成功，加入前的切片数量+1：{section_num + 1} = 加入后的切片数量{section_num_two}")
            print("--------------------------------------")
        except:
            FrameLog().get_Logger().error(f"断言失败，加入前的切片数量+1：{section_num + 1}！=加入后的切片数量{section_num_two}")
        pass

    def test03_adds_section_to_area(self):
        """ 在切片列表中选中多张切片加入待阅片区 """
        # 点击下拉按钮
        self.home.yuncunchu_xiala()
        # 选择文件夹
        self.home.open_files()
        # 获取待阅片区中切片的数量
        section_num = self.home.get_area_num()
        # 选择第切片文件数量 3个
        num = 0
        for i in range(1, 4):
            Open_Click_Section(driver=self.driver).click_sections(i)
            num = num + 1
        # 点击加入待阅片区
        Open_Click_Section(driver=self.driver).adds_section_to_area()
        try:
            # 获取选择切片加入待阅片区后的切片数量是否正确
            section_num_two = self.home.get_area_num()
            if section_num + num != 0 and section_num_two != 0:
                self.assertEqual(section_num + num, section_num_two)
                FrameLog().get_Logger().info(f"断言成功，加入前的切片数量+{num}：{section_num + num} = 加入后的切片数量{section_num_two}")
        except:
            FrameLog().get_Logger().error(f"断言失败，加入前的切片数量+1：{section_num + num}！=加入后的切片数量{section_num_two}")
        pass

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close()
