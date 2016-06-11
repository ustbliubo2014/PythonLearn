# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustbliubo@qq.com
@software: PyCharm
@file: contextmanager_test.py
@time: 2016/6/11 21:12
"""

from contextlib import contextmanager
from contextlib import nested
from contextlib import closing

@contextmanager
def make_context() :
    print 'enter'
    try :
        yield {}
    except RuntimeError, err :
        print 'error' , err
    finally :
        print 'exit'

with make_context() as value :
    print value


@contextmanager
def make_context(name) :
    print 'enter', name
    yield name
    print 'exit', name

with nested(make_context('A'), make_context('B')) as (a, b) :
    print a
    print b

with make_context('A') as a, make_context('B') as b :
    print a
    print b

class Door(object) :
    def open(self) :
        print 'Door is opened'
    def close(self) :
        print 'Door is closed'

with closing(Door()) as door :
    door.open()

if __name__ == '__main__':
    pass