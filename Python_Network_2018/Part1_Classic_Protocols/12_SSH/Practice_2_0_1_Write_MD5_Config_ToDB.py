#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import os
import sqlite3
from Practice_2_Get_MD5_Config import get_md5_config
import datetime
import time


def createdb(dbname):
    if os.path.exists(dbname):
        os.remove(dbname)
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 创建数据库

    cursor.execute("create table configdb(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                         time varchar(64), \
                                         device_ip varchar(32),\
                                         md5_value varchar(32),\
                                         config varchar(40960)\
                                         )")
    conn.commit()


def writedb(time, device_ip, md5_value, config, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("insert into configdb (time, \
                                          device_ip, \
                                          md5_value, \
                                          config) values ('%s', '%s', '%s', '%s')" % (time,
                                                                                            device_ip,
                                                                                            md5_value,
                                                                                            config))
    conn.commit()


def get_config_writedb(host, username, password, dbname, seconds):
    while seconds >= 0:
        result = get_md5_config(host, username, password, operation=0)
        config = result[host][0]
        md5_value = result[host][1]
        writedb(datetime.datetime.now(), host, md5_value, config, dbname)
        time.sleep(5)
        seconds -= 5


if __name__ == '__main__':
    createdb('configdb.sqlite')
    get_config_writedb('10.1.1.253', 'admin', 'Cisc0123', 'configdb.sqlite', 60)