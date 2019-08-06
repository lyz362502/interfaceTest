# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 10:47 AM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : QueryOrder_400704.py
# @Software: PyCharm
import unittest
import requests
import json
from ddt import ddt,data,unpack
from common.sendRequest import SendRequests
from common.readExcel import ReadExcel
import os


class QueryOrder_400704(unittest.TestCase):
    def setUp(self):
        self.bash_url = "http://yjjktest.yunjiacloud.com/yj-mbfz-ws/services/f/400704"

    def test_query_01(self):
        headers = {"Content-Type": "application/json"}
        dataPost = {}
        args = {"busiOrderId": "9451111", "patientId": "150", "sysCode": "1001001"}
        dataPost['funcode'] = "400704"
        dataPost['args'] = args
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())
        self.assertEqual(repose.status_code, 200, msg="请求不成功")

    def test_query_02(self):
        headers = {"Content-Type": "application/json"}
        dataPost = {}
        args = {"busiOrderId": "9451111", "patientId": "150", "sysCode": "1001001"}
        dataPost['funcode'] = "400704"
        dataPost['args'] = args
        print(dataPost)
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())
        self.assertEqual(repose.status_code, 200, msg="请求不成功")


if __name__ == '__main__':

    unittest.main()
