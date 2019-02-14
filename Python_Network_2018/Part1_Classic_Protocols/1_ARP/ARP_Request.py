#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *
from Part1_Classic_Protocols.Tools.GET_IP_netifaces import get_ip_address  # 获取本机IP地址
from Part1_Classic_Protocols.Tools.GET_MAC_netifaces import get_mac_address  # 获取本机MAC地址
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字


def arp_request(ip_address, ifname='ens33'):
    # 获取本机IP地址
    localip = get_ip_address(ifname)
    # 获取本机MAC地址
    localmac = get_mac_address(ifname)
    try:  # 发送ARP请求并等待响应!
        result_raw = sr1(ARP(op=1,
                             hwsrc=localmac, hwdst='00:00:00:00:00:00',
                             psrc=localip, pdst=ip_address),
                             iface=scapy_iface(ifname),
                             timeout=1,
                             verbose=False)

        return ip_address, result_raw.getlayer(ARP).fields['hwsrc']

    except AttributeError:
        return ip_address, None


if __name__ == "__main__":
    # Windows Linux均可使用
    arp_result = arp_request('10.1.1.252', "Net1")
    print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])