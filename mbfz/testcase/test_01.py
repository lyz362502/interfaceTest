"""
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 11:20 AM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : test_01.py
# @Software: PyCharm
"""


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')