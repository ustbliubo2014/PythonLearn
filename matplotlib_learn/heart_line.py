# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: func.py
@time: 2017/2/6 14:46
@contact: ustb_liubo@qq.com
@annotation: heart_line
"""
import sys
import logging
from logging.config import fileConfig
import os
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


# t = np.linspace(-np.pi, np.pi, 1000)
# x = 16*np.power((sin(t)), 3)
# y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
#
# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
# show()

# 采样数一定要大
x = np.linspace(-np.pi, np.pi, 100000)
y = (np.power(np.cos(x), 1.0/2)*np.cos(200*x)+np.power(np.abs(x), 1.0/2)-0.7)*np.power(4-x*x, 1.0/100)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()