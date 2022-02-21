# -*- coding: utf-8 -*- 
# @Time : 2021/12/10 13:16 
# @Author : 小林 
# @Site : 上海
# @File : check_file_page.py
from common.logger import FrameLog
from base.basepage import Basepage
from pagelocations.Slideecenter_loc.check_file_page import File_check


class Check_file(Basepage):

    def check_file(self):
        self.click("下拉框", File_check.xia_loc)
        self.sleep(2)
        self.click("选择测试文件夹", File_check.test_folder_loc)
        self.sleep(2)
        self.click("选择测试切片文件", File_check.test_file_01_loc)
        self.sleep(2)
        get_text = self.get_element_text("获取元素信息", File_check.file_name)
        self.sleep(2)
        file_name = self.get_element_text("选择文件名称", File_check.test_file_01_loc)
        self.sleep(2)
        try:
            assert get_text == file_name
            FrameLog().get_Logger().info(f"预期结果：{get_text} = 实际结果：{file_name}")
        except:
            FrameLog().get_Logger().error(f"断言失败：预期结果：{get_text} ！= 实际结果：{file_name} ，结果不一致")
        self.sleep(1)

    def check_files(self):
        num = 0
        self.click("下拉框", File_check.xia_loc)
        self.sleep(2)
        self.click("选择测试文件夹", File_check.test_folder_loc)
        self.sleep(2)
        self.click("勾选第一张切片", File_check.test_file_01_loc)
        num += 1
        self.sleep(2)
        self.click("勾选第二张切片", File_check.test_file_02_loc)
        num += 1
        get_text = self.get_element_text("获取选择项目数量文本", File_check.file_number)
        expect_text = (str(num) + "个项目")
        self.sleep(1)
        try:
            assert expect_text == get_text
            FrameLog().get_Logger().info(f"预期结果：{get_text} = 实际结果：{expect_text}")
        except:
            FrameLog().get_Logger().info(f"断言失败，预期结果{get_text} ！= 实际结果：{expect_text}，结果不一致")
        self.sleep(1)
