# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 1:53 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : InterfaceTest.py
# @Software: PyCharm
import requests
import unittest
import time
import random
import string
from common.testMd5 import TestMd5
from common.GetToken import get_token, login
import json


def login1():
    arg = {'userName': "convenient-admin", 'password': '21232f297a57a5a743894a0e4a801fc3'}
    return arg


class InterfaceTest(unittest.TestCase):
    login()

    def setUp(self):
        self.bash_urlone = 'https://yjjktest.yunjiacloud.com/pcloud-was/healthcloud/services/f/data-node/100301'

    def tearDown(self):
        time.sleep(1)

    def test_infoGet(self):
        """验证:测试infoGet接口是否正确"""
        postData = {'funcode': "100301", 'sysCode': '10003'}
        t = time.time()
        signTime = int(round(t * 1000))
        postData['random'] = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        postData['token'] = TestMd5().md5_xs(get_token())
        postData['signTime'] = signTime
        # arg = {'userName': "convenient-admin", 'password': '21232f297a57a5a743894a0e4a801fc3'}
        arg = login1()
        print(arg)
        postData['args'] = arg
        print(postData)
        firstMd5 = TestMd5().md5_xs(json.dumps(postData))
        fi = str(firstMd5).upper() + str(get_token()) + str(signTime) + str(postData['random'])
        secondMd5 = TestMd5().md5_xs(fi)
        headers = {'Content-Type': 'application/json', 'sign': secondMd5.upper()}
        response = requests.post(self.bash_urlone, data=json.dumps(postData), headers=headers)
        print(response.json())
        print(response.status_code)


