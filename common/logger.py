# -*- coding: utf-8 -*- 
# @Time : 2021/11/19 12:46 
# @Author : 小林 
# @Site : 上海
# @File : logger.py
import logging
import os
import config
import time


class FrameLog:
    def __init__(self):
        self.error_count = 0

    def get_Logger(self):
        logger = logging.getLogger()
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            SH = logging.StreamHandler()
            str_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
            str_time = str_time[:10]
            logpath = os.path.join(config.logs_dir, f"log_{str_time}.log")
            FH = logging.FileHandler(logpath, encoding="utf-8")
            formatter = logging.Formatter(
                fmt="[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s",
                datefmt='%Y/%m/%d %H:%M:%S')
            logger.addHandler(SH)
            logger.addHandler(FH)
            SH.setFormatter(formatter)
            FH.setFormatter(formatter)
        return logger

    def logger_error(self, message):
        self.get_Logger().error(message)
        self.error_count += 1
        return self.error_count


if __name__ == '__main__':
    pass
