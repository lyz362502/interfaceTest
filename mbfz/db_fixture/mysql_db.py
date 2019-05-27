# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 下午2:13
# @Author  : LY
# @Email   : louyong@yunjiacloud.com
# @File    : mysql_db.py
# @Software: PyCharm

import pymysql.cursors
import os
import configparser as cparser

# ========读取配置文件路径=================== #
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

# ========读取数据库配置信息================ #
cf = cparser.ConfigParser()
cf.read(file_path)
host = cf.get("mysql", "host")
port = cf.get("mysql", "port")
db = cf.get("mysql", "db_name")
user = cf.get("mysql", "user")
password = cf.get("mysql", "password")


class DB:
    def __init__(self):
        try:
            # """连接数据库"""
            self.connection = pymysql.connect(host=host, port=int(port), user=user,
                                              password=password, db=db, charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
            print("数据库连接成功")
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()


if __name__ == '__main__':
    db = DB()
