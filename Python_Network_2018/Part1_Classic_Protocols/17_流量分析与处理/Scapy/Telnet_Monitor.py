#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
import re
from scapy.all import *
import hexdump
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface


def qythexdump(src, length=16):  # 每16个字节被提取出来，进行16进制的decode
    for i in range(0, len(src), length):
        s = src[i:i + length]
        hexdump.hexdump(s)


qyt_string = b''


def telnet_monitor_callback(pkt):
    global qyt_string
    try:
        qyt_string = qyt_string + pkt.getlayer(Raw).fields['load']  # 提取Telnet中的数据，并且把他们拼在一起
    except Exception as e:
        pass


def telnet_monitor(user_filter, ifname):
    # 捕获过滤器匹配的流量, 对流量进行解码
    PTKS = sniff(prn=telnet_monitor_callback,
                 filter=user_filter,
                 store=1,
                 iface=scapy_iface(ifname),
                 timeout=10)

    wrpcap("telnet.cap", PTKS)  # 保持捕获的数据包到文件
    qythexdump(qyt_string)  # 解码展示


if __name__ == "__main__":
    telnet_monitor('tcp port 23 and ip host 10.1.1.253', 'ens33')