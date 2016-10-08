# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: tmp.py
@time: 2016/10/8 18:07
@contact: ustb_liubo@qq.com
@annotation: tmp
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')

if __name__ == '__main__':
    pass
