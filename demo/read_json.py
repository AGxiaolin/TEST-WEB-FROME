# -*- coding: utf-8 -*- 
# @Time : 2021/12/2 15:25 
# @Author : 小林 
# @Site : 上海
# @File : read_json.py
import json
import os


def read_json(file_path):
    with open(file_path) as f:
        json_datas = json.load(f)
        datas = json_datas["Annotations"]
    for data in range(len(datas)):
        print(f'第{data + 1}条数据：', datas[data])


# 获取文件夹中 包含json的文件路径
def read_filename(file_path):
    filename_list = []
    for filename in os.listdir(file_path):
        if ".json" in str(filename):
            filename_path = os.path.join(file_path, filename)
            filename_list.append(filename_path)
        elif ".json" not in str(filename):
            filename_path = os.path.join(file_path, filename)
            zhiwenjian_path = read_filename(filename_path)
            for i in zhiwenjian_path:
                filename_list.append(i)
    return filename_list


# 读取json列表
def read_jsons(file_list):
    i = 0
    for file_path in file_list:
        i = i + 1
        print(f"第{i}次读取")
        print(f"读取的文件路径为：{file_path}")
        print("读取内容如下:")
        read_json(file_path)
        print("内容读取结束------")
        print("\t")


# 读取文件夹中所有的JSON文件
def read_folder_json(file_path):
    json_path_list = read_filename(file_path)
    i = 0
    for file_path in json_path_list:
        i = i + 1
        print(f"第{i}次读取")
        print(f"读取的文件路径为：{file_path}")
        print("读取内容如下:")
        read_json(file_path)
        print("内容读取结束------")
        print("\t")


if __name__ == '__main__':
    #
    files_path = "D:\json\\lbp07490_.json"
    read_json(files_path)
    #  读取文件夹内所有的json
    # read_folder_json("D:\json")

    # lists = read_filename("D:\json\Annotations_11.11测试")
    # read_jsons(lists)
    read_json("")
