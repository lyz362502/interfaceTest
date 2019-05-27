# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 9:46 AM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : testDes.py
# @Software: PyCharm

import base64
import hashlib
from Crypto.Cipher import DES
from Crypto.Cipher.DES import MODE_ECB
from pyDes import ECB, PAD_NORMAL, triple_des
from Crypto import *
import binascii
from pyDes import des, CBC, PAD_PKCS5


class TestDes():

    def des_encrypt(self, s):
        """
        DES 加密
        :param self: 原始字符串
        :return: 加密后字符串
        """

        secret_key = 'fr33d0m@2016!her'
        # secret_key = '12345678'

        k = triple_des(secret_key.encode('utf-8'), ECB, pad=None, padmode=PAD_PKCS5)
        # print(secret_key.encode("utf-8"))
        en = k.encrypt(binascii.b2a_base64(s), padmode=PAD_PKCS5)
        return en.decode('ascii')

    def des_descrypt(self, s):
        """位
         DES 解密 8位key
         :return: 解密后的字符串
         """
        # secret_key = 'fr33d0m@2016!her
        secret_key = '12345678'
        k = des(secret_key.encode('utf-8'), ECB, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_base64(s), padmode=PAD_PKCS5)
        return de.decode('ascii')

    def des_descrypt16(self, s):
        """
        16位key
        :param s:
        :return:
        """
        secret_key = 'fr33d0m@2016!her'
        k = triple_des(secret_key.encode('utf-8'), ECB, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_base64(s), padmode=PAD_PKCS5)
        return de.decode('utf-8')

