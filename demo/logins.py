# -*- coding: utf-8 -*- 
# @Time : 2022/2/14 11:19 
# @Author : 小林 
# @Site : 上海
# @File : logins.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

users = (By.ID, "LoginInput_UserNameOrEmailAddress")
paword = (By.ID, "LoginInput_Password")
login_action = (By.NAME, "Action")
error_text = (By.XPATH, '//*[@id="AbpPageAlerts"]/div')


class logins(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.2.242:9800/")
        time.sleep(2)
        user = driver.find_element(*users)
        user.send_keys("zlzhao")
        time.sleep(2)
        password = driver.find_element(*paword)
        password.send_keys("123456")
        time.sleep(2)
        lgoin = driver.find_element(*login_action)
        lgoin.click()
        time.sleep(2)
        url = driver.current_url
        print(url)


if __name__ == '__main__':
    unittest.main()
