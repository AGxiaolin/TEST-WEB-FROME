# -*- coding: utf-8 -*- 
# @Time : 2021/11/16 18:53 
# @Author : 小林 
# @Site : 上海
# @File : read_yamls.py
import yaml
import os
import config

base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(config.base_dir, "config.yaml")


def readyaml(data_key):
    filepath = os.path.join(config.base_dir, "config.yaml")
    with open(file=filepath, encoding='utf-8') as yaml_faile:
        yaml_datas = yaml.load(yaml_faile.read(), yaml.FullLoader)
        return yaml_datas[data_key]


def read_datas(data_key):
    filepath = os.path.join(config.testdatas_dir, "testdatas.yaml")
    with open(file=filepath, encoding="utf-8") as f:
        datas = yaml.load(f.read(), yaml.FullLoader)
        return datas[data_key]


if __name__ == '__main__':
    datas = read_datas("login")
    print(datas)
    readyaml
