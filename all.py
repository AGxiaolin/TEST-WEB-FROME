# -*- coding: utf-8 -*-
# @Time : 2021/11/18 18:45
# @Author : 小林
# @Site : 上海
# @File : all.py
import time
import unittest
import os
from BeautifulReport import BeautifulReport

from config import reports_dir, testcases_slide_center_dir
from testcase.Slide_center.test_add_section_to_area import Test_Add_section_to_area
from testcase.Slide_center.test_read_section import Test_Read_section

str_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
str_time = str_time[:10]
suite = unittest.TestSuite()
testcase_lists = []
# testcase_lists.append(Test01_login("test01_sucess"))
# testcase_lists.append(Test_Select_file("test01_select_yuncunchu"))
# testcase_lists.append(Test_Select_file("test02_select_myfiles"))
# testcase_lists.append(Test_Select_file("test03_select_myfiles_yuncunchu"))
# testcase_lists.append(Test_Select_file("test04_select_file_read_section"))
# testcase_lists.append(Test_Read_section("test01_read_section"))
# testcase_lists.append(Test_Read_section("test02_read_section"))
# testcase_lists.append(Test01_check_file("test01_check_file"))
# testcase_lists.append(Test01_check_file("test02_check_files"))
# testcase_lists.append(test01_logins("test01_login"))
# testcases = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
testcase_lists.append(Test_Add_section_to_area("test03_adds_section_to_area"))
"""
# suite.addTest(Test_Read_section("test01_read_section"))
# suite.addTest(Test_Read_section("test02_read_section"))
# suite.addTest(Test01_check_file("test01_check_file"))
# suite.addTest(Test01_check_file("test02_check_files"))
# 匹配test*.py用例文件名称
# suite3 = unittest.TestSuite()
# testcases = unittest.defaultTestLoader.discover("./testcase/Slide_center", "test*.py")
# unittest.main(defaultTest="testcases")
# unittest.TestLoader().loadTestsFromTestCase()
"""
# testcases = unittest.defaultTestLoader.discover(testcases_dir+"/Slide_center", "test*.py")
# testcases = unittest.defaultTestLoader.discover(testcases_slide_center_dir,pattern='test*.py')
# runner =  unittest.main()
# runner.run(testcases)
# 基于BeautifulReport生成测试报告
suite.addTests(testcase_lists)
BeautifulReport(suite).report(description="Slide_Center自动化执行测试报告", filename="reqort",
                              report_dir=reports_dir + "/" + str_time)
# BeautifulReport(testcases).report(description="Slide_Center自动化执行测试报告",filename="reqort",report_dir=reports_dir+"/"+str_time)
