#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def scapy_ping_one(host):
    packet = IP(dst=host, ttl=1) / ICMP() / b'Welcome to qytang'  # 构造Ping数据包
    ping = sr1(packet, timeout=1, verbose=False)  # 获取响应信息，超时为2秒，关闭详细信息

    try:
        if ping.getlayer(IP).fields['src'] == host and ping.getlayer(ICMP).fields['type'] == 0:
            # 如果收到目的返回的ICMP ECHO-Reply包
            return host, 1  # 返回主机和结果，1为通
        else:
            return host, 2  # 返回主机和结果，2为不通
    except Exception:
        return host, 2  # 出现异常也返回主机和结果，2为不通


if __name__ == '__main__':
    # Windows Linux均可使用
    print(scapy_ping_one("10.1.1.253"))
    # print(scapy_ping_one(sys.argv[1]))
