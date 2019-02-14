#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import sqlite3
from Practice_2_Diff_Conf import diff_txt


def def_config_id(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("select md5_value as md5_value,COUNT(*) as count from configdb group by md5_value")
    yourresults = cursor.fetchall()
    md5_list = []
    for i in yourresults:
        md5_list.append(i[0])
    id_list = []
    for md5 in md5_list:
        cursor.execute("select id from configdb where md5_value = '%s'" % md5)
        yourresults = cursor.fetchall()
        id_list.append(min([x[0] for x in yourresults]))
    id_list = sorted(id_list)

    id_time_list = []
    for id in id_list:
        cursor.execute("select id,time from configdb where id = %d" % id)
        yourresults = cursor.fetchall()
        id_time_list.append(yourresults[0])

    for i in id_time_list:
        print('配置ID:', i[0], '配置时间:', i[1])

    print('请选择需要比较的配置ID:')
    id_1 = int(input('ID1:'))
    id_2 = int(input('ID2:'))
    cursor.execute("select config from configdb where id = %d" % id_1)
    yourresults = cursor.fetchall()
    id_1_config = yourresults[0][0]
    cursor.execute("select config from configdb where id = %d" % id_2)
    yourresults = cursor.fetchall()
    id_2_config = yourresults[0][0]

    print(diff_txt(id_1_config, id_2_config))


if __name__ == '__main__':
    def_config_id('configdb.sqlite')
