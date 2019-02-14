#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import ntplib
from time import ctime
import sys
import optparse


def ntp_client(NTP_SERVER):
    c = ntplib.NTPClient()
    response = c.request(NTP_SERVER, version=3)
    print('\t' + ctime(response.tx_time))


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    ntp_client('0.uk.pool.ntp.org')
