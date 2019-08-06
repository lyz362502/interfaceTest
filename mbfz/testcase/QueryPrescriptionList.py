# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 下午3:58
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : QueryPrescriptionList.py
# @Software: PyCharm
import requests
import unittest
import json


class QueryPres(unittest.TestCase):
    def setUp(self):
        self.bash_url = "http://192.168.109.110:8080/OcpAdapter/services/10002"

    def test_query(self):
        """
        查询最近10条就诊记录
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "1912009222"}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.text)
        self.assertEqual(repose.status_code, 200)

    def test_query_jzkh_null(self):
        """
        就诊卡id为空
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": ""}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        self.assertEqual(repose.json()['msg'], "参数'jzkh'不能为空！")

    def test_query_jzkh_error(self):
        """
        就诊卡错误
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {"jzkh": "11"}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        self.assertEqual(repose.json()['msg'], "没有符合条件的记录！")
    def test_query_jzkh_none(self):
        """
        空参
        :return:
        """
        headers = {"Content-Type": "application/json"}
        dataPost = {}
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.text)
        # self.assertEqual(repose.json()['msg'], "没有符合条件的记录！")


if __name__ == '__main__':

    unittest.main()
