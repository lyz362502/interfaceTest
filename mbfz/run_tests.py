# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 下午4:21
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : run_tests.py
# @Software: PyCharm
import unittest
from testcase import QueryOrder_400704
"""构建测试集"""
# suite=unittest.TestSuite()
# suite.addTest(QueryOrder_400704.QueryOrder_400704('test_query_01'))
# suite = unittest.defaultTestLoader.discover("./")
suite = unittest.TestLoader().loadTestsFromTestCase(QueryOrder_400704.QueryOrder_400704)

if __name__=='__main__':
    """执行测试"""
    runner = unittest.TextTestRunner()
    runner.run(suite)