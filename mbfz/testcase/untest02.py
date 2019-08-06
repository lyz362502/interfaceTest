# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 5:35 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : untest02.py
# @Software: PyCharm

import unittest


class MyDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("i am setUpcal")

    def test1(self):
        print("i am test1")

    def test2(self):
        print("i am test2")

    @classmethod
    def tearDownClass(cls):
        print("i am tearDowclass")


if __name__ == '__main':
    unittest.main()
