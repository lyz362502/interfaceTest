# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 上午9:41
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : RevisitWriteBackHis.py
# @Software: PyCharm
import requests
import unittest
import json
import time
import datetime


class InsertHis(unittest.TestCase):

    def setUp(self):
        self.bash_url = "http://192.168.109.110:8080/OcpAdapter/services/RevisitWriteBackHis"

    def test_query_01(self):
        """
        处方识别id为空
        :return:
        """
        t = time.time()
        timeDate = int(round(t * 1000))
        print(timeDate)
        headers = {"Content-Type": "application/json"}
        dataPost = {}
        yjMbfzDdxx = {"ddid": timeDate, "hzxm": "娄勤", "mblx": "糖尿病,高血压", "psdz": "西溪科创园(西湖区文一西路522号)", "pslxr": "别克顾问"
                      , "pssjhm": "15858160023", "sfzh": "362503198806215015", "sqsj": "2018-11-03 15:17:55", "ybkh":"A39197001",
                    "ysgh": "0249201257735555", "ysxm": "娄勇", "zcwc": "2018-11-13 15:59:10"}
        yjMbfzJyjcmx = []
        cmx = {"ddid": 1, "mxid": timeDate, "jyjcmc": "体检"}
        yjMbfzJyjcmx.append(cmx)
        yjMbfzYpmx = []
        pmx = {"mxId": timeDate, "ypgg": "0.5g*40片", "ypsl": "1", 'ddId': 1}
        yjMbfzYpmx.append(pmx)
        dataPost['yjMbfzDdxx'] = yjMbfzDdxx
        dataPost['yjMbfzJyjcmx'] = yjMbfzJyjcmx
        dataPost['yjMbfzYpmx'] = yjMbfzYpmx
        print(dataPost)
        repose = requests.post(self.bash_url, data=json.dumps(dataPost), headers=headers)
        print(repose.json())


if __name__ == "__main__":
    unittest.main()
