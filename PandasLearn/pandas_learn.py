# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: pandas_learn.py
@time: 2016/7/22 14:15
@contact: ustb_liubo@qq.com
@annotation: pandas_learn
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='pandas_learn.log',
                    filemode='a+')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
df = pd.DataFrame(np.random.randn(10, 4)) # 将numpy的数据转换成pandas
print s

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')

plt.show()
