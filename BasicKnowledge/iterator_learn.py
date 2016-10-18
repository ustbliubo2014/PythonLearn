# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: iterator_learn.py
@time: 2016/10/18 10:03
@contact: ustb_liubo@qq.com
@annotation: iterator_learn
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


# # 创建一个迭代器, 返回的是生成器(yield), 只需修改line_to_word, 这种方法适合复用
# def word_of_file(file_path, line_to_word=str.split):
#     '''
#     :param file_path: 文件名
#     :param line_to_word: 操作函数
#     :return:
#     '''
#     the_file = open(file_path)
#     for line in the_file:
#         for word in line_to_word(line):
#             yield word
#
# # 处理生成器
# for word in word_of_file('logger_config.ini'):
#     print word
#

# 用迭代器遍历文件
import fnmatch

def get_all_files(root_folder, patterns='*', single_level=True, yield_folder=False):
    '''
    :param root_folder: 根目录
    :param patterns: 文件匹配模式,可以包含多个
    :param single_level:
    :param yield_folder:
    :return:
    '''
    patterns = patterns.split(';')
    for path, subdirs, subfiles in os.walk(root_folder):
        if yield_folder:
            subfiles.extend(subdirs)
        subfiles.sort()
        for file in subfiles:
            for pattern in patterns:
                if fnmatch.fnmatch(file, pattern):
                    yield os.path.join(path, file)
        if single_level:
            break


for file in get_all_files('d:/data/face', patterns='*face*', single_level=False, yield_folder=True):
    print file