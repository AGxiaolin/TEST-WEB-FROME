# -*- coding: utf-8 -*- 
# @Time : 2022/2/18 10:41 
# @Author : 小林 
# @Site : 上海
# @File : logger_test.py
import os
import logging
import time
from logging import handlers
# 日志根路径
from config import logs_dir


def get_logger(log_filename, level=logging.DEBUG, when='midnight', back_count=0):
    """
    :brief  日志记录
    :param log_filename: 日志名称
    :param level: 日志等级
    :param when: 间隔时间:
        S:秒
        M:分
        H:小时
        D:天
        W:每星期（interval==0时代表星期一）
        midnight: 每天凌晨
    :param back_count: 备份文件的个数，若超过该值，就会自动删除
    :return: logger
    """
    logger = logging.getLogger(log_filename)
    logger.setLevel(level)
    str_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
    str_time = str_time[:10]
    log_path = logs_dir
    # os.path.join(logs_dir, f"log_{str_time}_{log_filename}.log")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file_path = os.path.join(log_path, f"log_{str_time}_{log_filename}.log")
    # log输出格式
    formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # 输出到文件
    fh = logging.handlers.TimedRotatingFileHandler(
        filename=log_file_path,
        when=when,
        backupCount=back_count,
        encoding='utf-8')
    fh.setLevel(level)
    # 设置日志输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 添加到logger对象里
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    logger = get_logger("my.log")
    logger.debug("debug test")
    logger.info("info test")
    logger.error("error test")
