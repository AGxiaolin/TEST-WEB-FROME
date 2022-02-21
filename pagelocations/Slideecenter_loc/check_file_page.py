# -*- coding: utf-8 -*- 
# @Time : 2021/12/10 13:17 
# @Author : 小林 
# @Site : 上海
# @File : check_file_page.py

from selenium.webdriver.common.by import By


class File_check:
    xia_loc = (By.XPATH, "//div[@id='cloud']/i[2]")
    test_folder_loc = (By.ID, "/11.11测试")
    test_file_01_loc = (By.XPATH, '//div/span[text()="自动化专用切片"]')
    test_file_02_loc = (By.XPATH, '//div/span[text()="38"]')
    file_name = (By.XPATH, "//ul/li[2][text()]")
    file_number = (By.XPATH, "//ul/li[1][text()='2个项目']")
    pass
