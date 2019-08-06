# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 3:52 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : GetToken.py
# @Software: PyCharm
import unittest
import json
import os
import requests
from common.testDes import TestDes


def login():
    """把token写入到文件中"""
    url = 'https://yjjktest.yunjiacloud.com/pcloud-was/healthcloud/services/f/data-node/100110'
    postData = {'funcode': '100110'}
    arg = {'sysCode': '10003'}
    postData['args'] = arg
    # print(postData)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(postData), headers=headers)
    # print(response.json())
    # print("加密数据：" + response.json()['exceptionId'])
    a = TestDes().des_descrypt(response.json()['exceptionId'])
    # print("a is :", a)
    with open(base_dir(), 'w') as f:
        f.write(a)


def base_dir():
    """获取当前文件的目录"""
    return os.path.join(os.path.dirname(__file__), 'token.md')


def get_token():
    """读取存储在文件中的token"""
    with open(base_dir(), 'r') as f:
        return f.read()

#
# if __name__ == '__main__':
#     unittest.main()
