# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: file_duplicate.py
@time: 2016/10/25 22:18
"""

import logging
import os
import sys
import hashlib
import shutil


# 简单的测试一个字符串的MD5值
def GetStrMd5(src):
    m0=hashlib.md5()
    m0.update(src)
    pass

# 大文件的MD5值
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def CalcSha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

if __name__ == "__main__":
    root_folder = 'F:\USTB/'
    all_file_md5_dic = {}
    for root, sub_dir, sub_list in os.walk(root_folder):
        for file_name in sub_list:
            file_path = os.path.join(root, file_name)
            md5 = CalcMD5(file_path)
            if md5 not in all_file_md5_dic:
                all_file_md5_dic[md5] = file_path
            else:
                print file_path.decode('gbk').encode('utf-8')
                os.remove(file_path)
        print len(all_file_md5_dic)
