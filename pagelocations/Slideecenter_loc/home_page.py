# -*- coding: utf-8 -*- 
# @Time : 2021/11/22 10:59 
# @Author : 小林 
# @Site : 上海
# @File : home_page.py

from selenium.webdriver.common.by import By


class Home_page:
    # xia_loc = (By.CSS_SELECTOR,'div[title]>i')
    xia_loc = (By.XPATH, "//div[@id='cloud']/i[2]")
    folder_loc = (By.ID, "/11.11测试")
    section_loc = (By.XPATH, "//*[@id='/11.11测试/lbp07490.tron']")
    begin_loc = (By.XPATH, "//button[@class='btn btn-border slide-button'][1]")
    # add_to_area_loc = (By.XPATH,"//div[@class='font-bold-12 pb-2 pr-1 d-flex flex-column button-content']/button[2]/i")
    add_to_area_loc = (By.XPATH, "//button[@class='btn btn-border slide-button'][2]")
    # begin_loc = (By.CSS_SELECTOR, "#slide-manager-component-root>div:nth-child(2)>div>div +div>div+div>div>div+div>button")
    # 打开切片的名称
    section_name = (By.XPATH, "//div[@class='slide-name']")
    area_num_loc = (By.XPATH, "//span[@class='number']")  # 待阅片区角标数字
    pass


class Select_file_page:
    seek_loc = (By.XPATH, "//input[@class='search-slide-input w-100']")
    yuncunchu_loc = (By.XPATH, "//button[@class='btn mr-2 unselected']")
    result_loc = (By.XPATH, "//div[@class='slider-list-container ']/div[2]/div[1]/div/div/span")
    xia_loc = (By.XPATH, "//div[@id='cloud']/i[2]")
    test_folder_loc = (By.ID, "/11.11测试")
    labels_loc = (By.XPATH, "//div[@class='annotations-title']")

    def result_loc_files(self, s):
        result_loc = (By.XPATH, f"//div[@class='slider-list-container ']/div[2]/div[{s}]/div/div/span")
        return result_loc


class Context_menu_page:
    begin_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[1]/button")
    add_section_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[2]/button")
    rename_section_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[3]/button")
    delete_section_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[4]/button")
    copy_to_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[5]/button")
    move_to_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[6]/button")
    export_json_loc = (By.XPATH, "//ul[@class='mouse-right-menu show']/li[7]/button")


class Clck_files_button:
    add_to_area_loc = (By.XPATH, "//button[@class='btn btn-border slide-button'][1]")
    export_json_loc = (By.XPATH, "//button[@class='btn btn-border slide-button'][2]")

    pass
