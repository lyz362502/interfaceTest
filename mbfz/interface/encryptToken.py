# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 5:30 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : encryptToken.py
# @Software: PyCharm

import hashlib
import json
import string
import unittest
import time
import random
import requests
from util.testDes import TestDes


class encryptToken1(unittest.TestCase):
    def setUp(self):
        # self.bash_url = 'https://yjjktest.yunjiacloud.com/pcloud-was/healthcloud/services/f/system/100110'
        self.bash_url = 'http://192.168.50.51:8080/pcloud-was/healthcloud/services/f/system/100110'
        # self.bash_urlone = 'https://yjjktest.yunjiacloud.com/pcloud-was/healthcloud/services/f/data-node/200403'
        self.bash_urlone = 'http://192.168.50.51:8080/pcloud-was/healthcloud/services/f/data-node/200402'
        postData = {'funcode': '100110'}
        arg = {'sysCode': '10003'}
        postData['args'] = arg
        print(postData)
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.bash_url, data=json.dumps(postData), headers=headers)
        print(response.json())
        print("加密数据：" + response.json()['encryptToken'])
        str_en = response.json()['encryptToken']
        # self.str_de = des_descrypt(str_en)
        self.str_de = TestDes().des_descrypt(str_en)
        # 验证2小时token
        # self.str_de = '520135f0-2cc2-454e-bc42-19591b57d899'
        print("des_descrypt is :", self.str_de)
        h1 = hashlib.md5()
        h1.update(self.str_de.encode(encoding='utf-8'))
        self.h2 = h1.hexdigest().upper()
        print("md5token is ：", self.h2)

    def test_token1(self):
        postData = {}
        postData['funcode'] = "200402"
        postData['sysCode'] = '10003'
        t = time.time()
        signTime = int(round(t * 1000))
        print("signTime is ：", signTime)
        postData['random'] = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        print("random is :", postData['random'])
        postData['token'] = self.h2
        postData['signTime'] = signTime
        arg = {'userId': "323232"}
        postData['args'] = arg
        print(postData)
        m = hashlib.md5()
        m.update(json.dumps(postData).encode(encoding='utf-8'))
        firstMd5 = m.hexdigest()
        fi = str(firstMd5).upper() + str(self.str_de) + str(signTime) + str(postData['random'])
        m2 = hashlib.md5()
        m2.update(fi.encode(encoding='utf-8'))
        secondMd5 = m2.hexdigest()
        headers = {"Content-Type": "application/json", 'sign': secondMd5.upper()}
        response = requests.post(self.bash_urlone, data=json.dumps(postData), headers=headers)
        print(response.json())
