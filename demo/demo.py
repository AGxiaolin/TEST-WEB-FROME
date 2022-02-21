# -*- coding: utf-8 -*- 
# @Time : 2021/11/19 16:33 
# @Author : 小林 
# @Site : 上海
# @File : demo.py
import time

import document as document

from pagelocations.Slideecenter_loc.loggin_page import logo_loc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from base.basepage import Basepage
from selenium.webdriver.common.by import By

bases = Basepage(driver=webdriver.Chrome())

bases.get_url(logo_loc.home_url)
time.sleep(2)
user = "zlzhao"
paw = "123456"
user_loc = (By.ID, "LoginInput_UserNameOrEmailAddress")
pwd_loc = (By.ID, "LoginInput_Password")
loggin_loc = (By.NAME, "Action")
zppm_20_loc = (By.XPATH, "//div/button[text()='20']")
create_juxing_loc = (By.ID, "0HMDQU67K0ADV")

bases.input("账号", user_loc, user)
bases.sleep(1)
bases.input("密码", pwd_loc, paw)
bases.sleep(1)
bases.click("登录", loggin_loc)
bases.sleep(1)

xia_loc = (By.CSS_SELECTOR, 'div[title]>i')
bases.click("下拉框", xia_loc)
bases.sleep(2)
folder_loc = (By.ID, "/11.11测试")
bases.click("点击测试文件夹", folder_loc)
bases.sleep(2)
tupian = (By.XPATH, "//*[@id='/11.11测试/lbp07490.tron']")
# bases.click("云存储",wenjian)
bases.click("点击测试切片", tupian)
bases.sleep(2)
# aa = (By.XPATH,"//button/span[text()='开始阅片']")
aa = (By.CSS_SELECTOR, "#slide-manager-component-root>div:nth-child(2)>div>div +div>div+div>div>div+div>button")
bases.click("开始阅片", aa)
bases.sleep(1)
bases.click("切换成20倍大小", zppm_20_loc)
bases.sleep(1)
bases.click("创建矩形标注", create_juxing_loc)
js = "document.elementFromPoint(120,120)"
bases.driver.execute_script(js)
js = open(r"aa.js")
# time.sleep(3)
# element = (By.XPATH,'//*[@id="/[0p9o8iu7t6y7iopi8uy7854658.tron"]/div[1]/img')
# num = driver.find_element_by_xpath('//*[@id="/[0p9o8iu7t6y7iopi8uy7854658.tron"]/div[1]/img')
# bases.double_click("云存储",element)
# bases.sleep(2)

print("----------")
# assert 断言
# print(driver.page_source)
