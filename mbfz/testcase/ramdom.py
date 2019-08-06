# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 4:03 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : ramdom.py
# @Software: PyCharm
import random
import string
#第一种方法
seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
sa = []
for i in range(8):
  sa.append(random.choice(seed))
salt = ''.join(sa)
print(salt)
#运行结果：l7VSbNEG
#第二种方法
salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
print(salt)
#运行结果：VOuCtHZs


