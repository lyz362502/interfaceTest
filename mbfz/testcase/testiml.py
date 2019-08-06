# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 3:19 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : testiml.py
# @Software: PyCharm
import unittest
import requests
import json


class ly(unittest.TestCase):
    def setUp(self):
        self.bash_url = 'http://192.168.34.190:8080/pcloud-was/healthcloud/services/f/data-node/400101'

    def test_lou(self):
        postData = {}
        postData['funcode'] = "400101"
        postData['captcha'] = "token"
        arg = {}
        arg['terminologyType'] = "ORG_LEVEL"
        postData['args'] = arg
        print(postData)
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.bash_url, data=json.dumps(postData), headers=headers)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
