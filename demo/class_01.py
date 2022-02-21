# -*- coding: utf-8 -*- 
# @Time : 2021/12/8 11:35 
# @Author : 小林 
# @Site : 上海
# @File : class_01.py
import time
import unittest
from selenium import webdriver


class Test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        url = "https://www.baidu.com"
        time.sleep(1)
        cls.driver.get(url=url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()

    def test_01(self):
        print("aaaaa")


if __name__ == '__main__':
    unittest.main()
