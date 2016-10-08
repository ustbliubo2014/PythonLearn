# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: decorator_learn.py
@time: 2016/10/8 16:46
@contact: ustb_liubo@qq.com
@annotation: decorator
"""
import sys
import logging
from logging.config import fileConfig
import os
import time

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')


# 在运行期间动态增加功能, 在调用前增加log, 接收一个函数,返回的是高阶函数
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数
# 装饰器有参数, 装饰函数没有参数
def log1(text):
    def decorator(func):
        start = time.time()
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        end = time.time()
        print('func.name', func.__name__, 'run_time', (end - start))
        return wrapper
    return decorator


# 最基本的函数
# 把@log放到now()函数的定义处，相当于执行了语句： now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# decorator可以接收参数, 具体写法如log1

# @log
@log1('Execute :')
def now(*args, **kwargs):
    timestamp = time.time()
    time_array = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return otherStyleTime


# 对带参数的函数进行装饰
def now1():
    timestamp = time.time()
    time_array = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    time.sleep(3)
    return otherStyleTime


# 计算函数的执行时间, 函数可以带参数, 也可以有返回值
def time_decorator(func):
    def _deco(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('func.name', func.__name__, 'run_time',(end-start))
        return ret
    return _deco


if __name__ == '__main__':
    print now(1, 2, 3, print_str='print_str')
    time.sleep(2)
    print now(1, 2, 3, print_str='print_str')
