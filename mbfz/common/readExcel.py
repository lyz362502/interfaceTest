# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 4:00 PM
# @Author  : louyong
# @Email   : louyong@yunjiacloud.com
# @File    : readExcel.py
# @Software: PyCharm
#! /usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
import os


class ReadExcel():
    def __init__(self, dataPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(dataPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
        self.keys = self.table.row_values(0)

    def dic_data(self):
        if self.nrows <= 1:
            print("总行数小于1")
        else:
            r = [ ]
            j = 1
            for i in list(range(self.table.row_values(j))):
                s = {}
                s['nrows'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.ncols)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == '__main__':
    rootPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.abspath('..')
    dataPath = os.path.join(filePath + '//date//1.xlsx')
    sheetName = "Sheet1"
    data = ReadExcel(dataPath, sheetName)
    print(data)
