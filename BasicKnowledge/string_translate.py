# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: string_translate.py
@time: 2016/10/10 23:07
"""

import logging
import os
import sys


def func():
    pass


class Main():
    def __init__(self):
        pass



from string import maketrans   # Required to call maketrans function.
from time import time

intab = ""
outtab = ""
trantab = maketrans(intab, outtab)

# 删除一个字符串中不属于指定集合的字符(使用两次translate)
str = "this is string example....wow!!!" * 100000
start = time()
del_str = str.translate(trantab, 'xm')
result = str.translate(trantab, del_str)
end = time()
print (end - start)
print result[0:100]

# 删除一个字符串中属于指定集合的字符()
str = "this is string example....wow!!!" * 100000
start = time()
str.translate(trantab, 'xm')
end = time()
print (end - start)

str = "this is string example....wow!!!" * 100000
start = time()
del_set = set(list('xm'))
new_str = []
for s in str:
    if s not in del_set:
        new_str.append(s)
new_str=''.join(new_str)
end = time()
print (end - start)

str = "this is string example....wow!!!" * 100000
start = time()
for s in 'xm':
    str.replace(s,'')
end = time()
print (end - start)