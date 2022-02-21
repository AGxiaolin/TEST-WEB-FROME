# -*- coding: utf-8 -*- 
# @Time : 2021/11/16 19:02 
# @Author : 小林 
# @Site : 上海
# @File : config.py
import os

# 项目路径
# 项目路径
base_dir = os.path.dirname(os.path.abspath(__file__))
# 用例路径
testcases_slide_center_dir = os.path.join(base_dir, "testcases/Slide_center")
testcases_autoscope_dir = os.path.join(base_dir, "testcases/Slide_center")

# 数据路径
testdatas_dir = os.path.join(base_dir, "testdatas")
# 测试报告路径
reports_dir = os.path.join(base_dir, "Outputs/reports")
# 日志路径
logs_dir = os.path.join(base_dir, "Outputs/logs")
# 失败截图
screen_dir = os.path.join(base_dir, "Outputs/logs")
if __name__ == '__main__':
    print(base_dir)
    print(testcases_slide_center_dir)
    print(reports_dir)
