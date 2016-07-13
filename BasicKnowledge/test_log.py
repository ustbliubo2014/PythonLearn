# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: test_log.py
@time: 2016/7/12 21:23
@contact: ustb_liubo@qq.com
@annotation: test_log
"""

import sys
import logging
reload(sys)
sys.setdefaultencoding("utf-8")

# 所有文件都使用同一个logger(在logger_config.ini中配置好)
from logging.config import fileConfig

fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')
logger_error.error('test5')
logger_error.info('test info')

