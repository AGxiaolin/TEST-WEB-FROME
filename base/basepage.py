# -*- coding: utf-8 -*- 
# @Time : 2021/11/16 18:38 
# @Author : 小林 
# @Site : 上海
# @File : basepage.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import FrameLog
import config


class Basepage():
    """
    共用操作属性
    """

    # def __init__(self, driver=webdriver.Chrome()):
    #     self.driver = driver
    #     self.logger = FrameLog().get_Logger()

    def __init__(self, driver=None):
        self.driver = driver
        self.logger = FrameLog().get_Logger()

    def wait_ele_visibility(self, page_name, loc, timeout=15, poll_fre=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(loc))
            # WebElement对象
            self.logger.info(f"在[{page_name}]，找到元素：{loc}可见")
        except:
            self.logger.error(f"在[{page_name}]，未找到元素：{loc} 不可见！！！")
            self.sava_page_shot(page_name)

    def get_url(self, url):
        self.driver.get(url)
        self.logger.info(f"使用浏览器打开{url}")
        # 窗口最大化操作
        self.driver.maximize_window()
        self.logger.info("窗口最大化操作")

    def locator(self, page_name, loc):
        try:
            self.wait_ele_visibility(page_name, loc)
            el = self.driver.find_element(*loc)
            self.logger.info(f"定位到元素：{loc}")
        except:
            self.logger.error(f"未定位到元素：{loc}")
            raise
        return el

    def input(self, page_name, loc, value):
        try:
            self.locator(page_name, loc).send_keys(value)
            self.logger.info(f"在{page_name}，元素{loc},输入{value}")
        except:
            self.logger.info(f"在{page_name}，元素{loc},输入{value}失败！！！")
            self.sava_page_shot(page_name)

    def click(self, page_name, loc):
        try:
            self.locator(page_name, loc).click()
            self.logger.info(f"在{page_name},点击{loc}元素成功")
        except:
            self.logger.error(f"在{page_name},点击{loc}元素失败！！！")
            self.sava_page_shot(page_name)

    def sleep(self, s):
        time.sleep(s)
        self.logger.info(f"等待时间{s}秒")

    def clone(self):
        self.driver.close()
        self.logger.info("关闭浏览器")

    # def git_batton(self,page_name,loc):
    #     git_text=self.locator(page_name,loc).text
    #     self.logger.info(f"获取{loc}元素的文本信息")
    #     return git_text
    #     pass
    def get_element_text(self, page_name, loc):
        try:
            get_text = self.locator(page_name, loc).text
            self.logger.info(f"在{page_name},获取{loc}元素的文本信息成功")
        except:
            self.logger.error(f"在{page_name},获取{loc}元素的文本信息失败！！！")
            self.sava_page_shot(page_name)
            raise
        return get_text

    def handles(self, num):
        """
        num: 句柄索引
        句柄索引
        :return:
        """
        number = self.driver.window_handles
        return self.driver.switch_to.window(number[num])

    def move_element(self, page_name, loc):
        try:
            self.wait_ele_visibility(page_name, loc)
            ActionChains(self.driver).move_to_element(self.locator(page_name, loc)).perform()
            self.logger.info(f"在[{page_name}]，鼠标移动到元素{loc}")
        except:
            self.sava_page_shot(page_name)
            self.logger.error(f"在[{page_name}],鼠标移动到元素{loc}失败！！！")

    def double_click(self, page_name, loc):
        """
        鼠标双击操作
        :param page_name:操作页面
        :param loc: 操作元素
        :return: null
        """
        try:
            ActionChains(self.driver).double_click(self.locator(page_name, loc)).perform()
            self.logger.info(f"在[{page_name}],鼠标双击{loc}元素")
        except:
            self.sava_page_shot(page_name)
            self.logger.error(f"在{page_name}，鼠标双击{loc}元素失败！！！")

    # 右键点击
    def context_click(self, page_name, loc):
        try:
            ActionChains(self.driver).context_click(self.locator(page_name, loc)).perform()
            self.logger.info(f"在【{page_name}】，鼠标右键点击{loc}元素")
        except:
            self.sava_page_shot(page_name)
            self.logger.error(f"在【{page_name}】,鼠标右键点击{loc}失败！！！")
            pass

    def sava_page_shot(self, img_name):
        filename = os.path.join(config.screen_dir, img_name + ".png")
        self.driver.save_screenshot(filename)
        self.logger.info(f"失败截图，截取当前网页，存储路径：{filename}")
        # 设置智能能等待

    def implicitly_wait(self, s):
        self.driver.implicitly_wait(s)

    # def error_count(self):
    #     return self._error_count


if __name__ == '__main__':
    base = Basepage()
