# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: Progress_bar.py
@time: 2016/10/27 16:06
@contact: ustb_liubo@qq.com
@annotation: Progress_bar
"""
import sys
import logging
from logging.config import fileConfig
import os
from keras.utils import generic_utils
from time import sleep

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')

length = 1000
progbar = generic_utils.Progbar(length)
for i in range(length):
    sleep(0.1)
    progbar.add(1, values=[('index', i)])
