# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: __init__.py.py
@time: 2016/7/22 10:55
@contact: ustb_liubo@qq.com
@annotation: __init__.py
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='__init__.py.log',
                    filemode='a+')

if __name__ == '__main__':
    pass
