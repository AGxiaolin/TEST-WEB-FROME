# -*- coding: utf-8 -*- 
# @Time : 2021/11/17 10:09 
# @Author : 小林 
# @Site : 上海
# @File : login_page.py

from selenium.webdriver.common.by import By
from common import read_yamls
from common.read_yamls import readyaml


class login_loc:
    """
    login 页面的元素集合
    """
    user = (By.ID, "LoginInput_UserNameOrEmailAddress")
    password = (By.ID, "LoginInput_Password")
    action = (By.NAME, "Action")
    # readyaml("config.yaml")
    home_url = readyaml("Diagon_url")


if __name__ == '__main__':
    print(login_loc.home_url)
