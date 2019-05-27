# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 下午5:16
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : queryMedicine.py
# @Software: PyCharm
import requests
import unittest
import json

class QueryMedicineTest(unittest.TestCase):
    def setUp(self):
        self.bash_url = 'http://yjjktest.yunjiacloud.com/yj-mbfz-ws/services/f/220013'
        # self.bash_url = 'http://192.168.109.81:8080/yj-mbfz-ws/services/f/220013'

    def test_query(self):
        postData = {}
        postData['funcode'] = "220013"
        arg = {}
        arg['revisitId'] = "198"
        postData['args'] = arg
        print(postData)
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.bash_url, data=json.dumps(postData), headers=headers)
        print(response.text)