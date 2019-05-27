# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 4:00 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : testRequests.py
# @Software: PyCharm
import requests
import json


class TestRequest():

    def __init__(self):

        self.headers = {"Content-Type": "application/json"}

    def get(self, url, params):

        try:
            r = requests.get(url=url, params=params, headers=self.headers)
            response = json.loads(r.text)
            print("get请求结果为：%s" % response)

        except BaseException as e:
            print("get请求错误，错误原因：%s" % e)

    def post(self, url, params):

        data = json.dumps(params)
        try:
            r = requests.post(url=url, json=data, headers=self.headers)
            response = json.loads(r.text)
            print("post请求结果为：%s" % response)

        except BaseException as e:
            print("post请求错误，错误原因：%s" % e)

