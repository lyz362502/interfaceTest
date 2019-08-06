# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 3:21 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : untest01.py
# @Software: PyCharm

import unittest


class MyDemo(unittest.TestCase):

    def setUp(self):
        self.a = 1

    def test_01(self):
        print("i am test1 value of a is {}".format(self.a))

    def test_02(self):
        print("i am test2 value of a is {}".format(self.a))

    def test_03(self):
        print("i am test3 value of a is {}".format(self.a))


if __name__ == '__main__':
    test_runner = unittest.TextTestRunner()
    test_suit = unittest.TestSuite()
    test_suit.addTests(map(MyDemo, ["test_01", "test_02", "test_03"]))
    test_runner.run(test_suit)
