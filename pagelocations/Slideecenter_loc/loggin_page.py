# -*- coding: utf-8 -*- 
# @Time : 2021/11/18 17:14 
# @Author : 小林 
# @Site : 上海
# @File : loggin_page.py
from selenium.webdriver.common.by import By
from common import read_yamls
from common.read_yamls import readyaml


class logo_loc:
    """
    slide center logo页面元素
    """
    home_url = readyaml("Slidecenter_url")
    user = (By.ID, "LoginInput_UserNameOrEmailAddress")
    paword = (By.ID, "LoginInput_Password")
    login_action = (By.NAME, "Action")
    error_text = (By.XPATH, '//*[@id="AbpPageAlerts"]/div')
