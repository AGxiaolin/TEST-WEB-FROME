# -*- coding: utf-8 -*- 
# @Time : 2021/11/17 10:36 
# @Author : 小林 
# @Site : 上海
# @File : test_login.py
import pytest
import unittest
from selenium import webdriver
from pageobjects.Diagon.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def test_01_login(self, drivers):
        loginpage = LoginPage(driver=drivers)
        username = "zlzhao"
        paword = "123456"
        loginpage.logins(user=username, paword=paword)
