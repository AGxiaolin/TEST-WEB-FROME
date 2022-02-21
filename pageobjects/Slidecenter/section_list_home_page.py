# -*- coding: utf-8 -*- 
# @Time : 2022/2/11 15:41 
# @Author : 小林 
# @Site : 上海
# @File : section_list_home_page.py
from base.basepage import Basepage
from pagelocations.Slideecenter_loc.home_page import *


class Open_files_home(Basepage):
    def yuncunchu_xiala(self):
        self.click("点击下拉框", Select_file_page.xia_loc)
        self.sleep(2)
        # self.click("点击11.11测试文件夹", Select_file_page.test_folder_loc)

    def open_files(self):
        self.click("选择11.11测试文件夹", Select_file_page.test_folder_loc)

    def select_bok(self, name):
        name = str(name)
        self.input("搜索框", Select_file_page.seek_loc, name)
        self.sleep(2)

    def select_myfiles(self, name):
        self.yuncunchu_xiala()
        self.open_files()
        self.select_bok(name)

    def select_myfiles_yuncunchu(self, name):
        self.click("点击云存储", Select_file_page.yuncunchu_loc)

    # 搜索结果第一条数据的文本信息
    def result_text(self):
        result_text = self.get_element_text("搜索结果页面第一条数据的文本信息", Select_file_page.result_loc)
        return result_text

    def read_section(self):
        try:
            button_text = self.get_element_text("获取按钮的文本信息", Home_page.begin_loc)
            if str(button_text) == "开始阅片":
                self.click("点击开始阅片", Home_page.begin_loc)
                self.sleep(2)
        except:
            self.logger.error(f"操作的button：{button_text} != 【开始阅片】,操作失败")

    def add_to_area(self):
        try:
            button_text = self.get_element_text("获取按钮的文本信息", Home_page.add_to_area_loc)
            if str(button_text) == "加入待阅片区":
                self.click("切片列表右侧：加入待阅片区", Home_page.add_to_area_loc)
                self.sleep(2)
        except:
            self.logger.error(f"操作的button：{button_text} != 【加入待阅片区】,操作失败")

    def get_area_num(self):
        self.sleep(1)
        num_text = self.get_element_text("获取待阅片区角标数字", Home_page.area_num_loc)
        return int(num_text)

    def click_one_section(self):
        self.click("选择第一张切片", Select_file_page.result_loc)
        self.sleep(2)

    def context_menu(self):
        self.context_click("鼠标右键点击第一张切片", Select_file_page.result_loc)
        self.sleep(2)
        pass


class Open_Click_Section(Basepage):
    def click_sections(self, s):
        # 选择多张切片
        self.click(f"选择第{s}张切片", Select_file_page().result_loc_files(s))
        self.sleep(0.5)

    def adds_section_to_area(self):
        try:
            button_text = self.get_element_text("获取按钮的文本信息", Clck_files_button.add_to_area_loc)
            if str(button_text) == "加入待阅片区":
                self.click("切片列表右侧：加入待阅片区", Clck_files_button.add_to_area_loc)
                self.sleep(2)
        except:
            self.logger.error(f"操作的button：{button_text} != 【加入待阅片区】,操作失败")

    def export_jsons(self):
        self.click("点击切片列表右侧：导出json标注", Clck_files_button.export_json_loc)


class Read_section(Basepage):

    def section_name_text(self):
        return self.get_element_text("获取打开的切片名称字符", Home_page.section_name)

    def double_click_section(self):
        self.double_click("鼠标双击切片文件", Select_file_page.result_loc)
        self.sleep(2)


class Right_clicks(Basepage):
    def right_click_section(self):
        self.context_click("鼠标右键点击切片", Select_file_page.result_loc)
        self.sleep(2)

    def context_read_section(self):
        try:
            button_text = self.get_element_text("获取按钮的文本信息", Context_menu_page.begin_loc)
            if str(button_text) == "开始阅片":
                self.click("鼠标右键菜单：开始阅片", Context_menu_page.begin_loc)
                self.sleep(2)
        except:
            self.logger.error(f"操作的button：{button_text} != 【开始阅片】,操作失败")

    def add_section_to_area(self):
        self.click("鼠标右键菜单：加入待阅片区", Context_menu_page.add_section_loc)
        self.sleep(2)

    def rename_section(self):
        self.click("鼠标右键菜单：重命名切片", Context_menu_page.rename_section_loc)
        self.sleep(2)

    def delete_section(self):
        self.click("鼠标右键菜单：删除切片", Context_menu_page.delete_section_loc)
        self.sleep(2)

    def copy_section(self):
        self.click("鼠标右键菜单：复制切片到其他文件夹", Context_menu_page.copy_to_loc)

    def move_section(self):
        self.click("鼠标右键菜单：重命名切片", Context_menu_page.move_to_loc)

    def export_json(self):
        self.click("鼠标右键菜单：导出json标注", Context_menu_page.export_json_loc)

    pass
