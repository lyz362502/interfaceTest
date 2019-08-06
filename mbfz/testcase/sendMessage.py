# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 下午4:23
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : sendMessage.py
# @Software: PyCharm
import unittest
import requests
import json


class SendMessageTest(unittest.TestCase):
    def setUp(self):
        self.bash_url = "http://yjjktest.yunjiacloud.com/yj-mbfz-ws/services/f/220003"

    def test_phone_null(self):
        """
        电话号码为空
        :return:
        """
        postData = {}
        postData['funcode'] = "220003"
        arg = {}
        arg['phone'] = "18758115894"
        postData['args'] = arg
        print(postData)
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.bash_url, data=json.dumps(postData), headers=headers)
        print(response.text)


if __name__ == '__main__':
    unittest.main()

