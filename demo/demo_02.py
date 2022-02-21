# -*- coding: utf-8 -*- 
# @Time : 2021/11/22 16:56 
# @Author : 小林 
# @Site : 上海
# @File : demo_02.py
import time
import unittest

from selenium import webdriver

# class Test_case(unittest.TestCase):
#
#     def setUp(self) -> None:
#         url = "https://www.baidu.com/"
#         self.driver = webdriver.Chrome()
#         self.driver.get(url)
#     def test_01(self):
#         self.driver.find_element_by_id("kw").send_keys("手机")
#         time.sleep(3)
#     def test_02(self):
#         self.driver.find_element_by_id("kw").send_keys("充电宝")
#         time.sleep(3)
#     def test_03(self):
#         self.driver.find_element_by_id("kw").send_keys("宝马")
#         time.sleep(3)
#     def test_04(self):
#         self.driver.find_element_by_id("kw").send_keys("支付宝")
#         time.sleep(3)
# if __name__ == '__main__':
#     unittest.main()
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
el_new = driver.find_element_by_link_text("新闻")
el_new.click()
