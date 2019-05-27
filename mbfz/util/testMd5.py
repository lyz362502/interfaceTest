# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 9:58 AM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : testMd5.py
# @Software: PyCharm
import hashlib

class TestMd5():

    def md5_xs(self, str_de):
        h1 = hashlib.md5()
        h1.update(str_de.encode(encoding='utf-8'))
        h2 = h1.hexdigest().upper()
        # print("md5token is ：", h2)
        return h2