# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 下午3:58
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : QueryPrescriptionList.py
# @Software: PyCharm
import requests
import unittest
import json


class InsertHis(unittest.TestCase):
    def setUp(self):
        self.bash_url = "http://192.168.109.110:8080/OcpAdapter/services/10003"

    def test_query_01(self):
        """
        处方识别id为空
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "1912009222", "cfsb": ""}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())

    def test_query_jzkh_null(self):
        """
        就诊卡id为空
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "", "cfsb": "42831"}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())
        self.assertEqual(repose.json()['msg'], "参数'jzkh'不能为空！")

    def test_query_jzkh_error(self):
        """
        参数错误
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "1", "cfsb": "1"}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())

    def test_query_jzkh_none(self):
        """
        参数为空
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())

    def test_query_02(self):
        """
        参数正确
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "1100084556", "cfsb": "42831"}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())


if __name__ == '__main__':

    unittest.main()
