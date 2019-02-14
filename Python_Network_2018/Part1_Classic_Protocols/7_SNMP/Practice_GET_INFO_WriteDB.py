#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import os
import sqlite3
from GET import snmpv2_get
import datetime
import time


def get_info_writedb(ip, rocommunity, dbname, seconds):
    # 如果文件存在,删除数据库文件
    if os.path.exists(dbname):
        os.remove(dbname)
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 创建数据库
    cursor.execute("create table routerdb(id INTEGER PRIMARY KEY AUTOINCREMENT, time varchar(64), cpu int, memu int, memf int)")

    while seconds >= 0:
        # cpmCPUTotal5sec
        cpu_info = snmpv2_get(ip, rocommunity, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1]
        # cpmCPUMemoryUsed
        memu_info = snmpv2_get(ip, rocommunity, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1]
        # cpmCPUMemoryFree
        memf_info = snmpv2_get(ip, rocommunity, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1]
        # 记录当前时间
        time_info = datetime.datetime.now()
        # 把数据写入数据库
        cursor.execute("insert into routerdb (time, cpu, memu, memf) values ('%s', %d, '%d', '%d')" % (time_info, int(cpu_info), int(memu_info), int(memf_info)))
        # 每五秒采集一次数据
        time.sleep(5)
        seconds -= 5
    # 提交数据到数据库
    conn.commit()


if __name__ == '__main__':
    get_info_writedb("10.1.1.253", "tcpipro", "deviceinfo.sqlite", 60)
