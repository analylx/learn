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
from Part1_Classic_Protocols.Tools.GET_MAC_netifaces import get_mac_address
from Part1_Classic_Protocols.Tools.Change_MAC_To_Bytes import Change_MAC_To_Bytes
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字
import time
import struct
# Dynamic Host Configuration Protocol (DHCP) and Bootstrap Protocol (BOOTP) Parameters
# https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml
requested_option_1 = 1   # Subnet Mask
requested_option_2 = 6   # Domain Name Servers
requested_option_3 = 15  # Domain Name
requested_option_4 = 44  # NetBIOS (TCP/IP) Name Servers
requested_option_5 = 3   # Routers
requested_option_6 = 33  # Static Routes
requested_option_7 = 150 # TFTP Server address
requested_option_8 = 43  # Vendor Specific Information

bytes_requested_options = struct.pack("8B", requested_option_1,
                                            requested_option_2,
                                            requested_option_3,
                                            requested_option_4,
                                            requested_option_5,
                                            requested_option_6,
                                            requested_option_8,
                                            requested_option_7)


def chaddr(info):
    # chaddr一共16个字节，正常的chaddr信息里边只有MAC地址,思科比较特殊
    # MAC地址只有6个字节，所以需要把剩余部分填充b'\x00'
    return info + b'\x00' * (16 - len(info))


def DHCP_Discover_Sendonly(ifname, MAC, wait_time=1):
    Bytes_MAC = Change_MAC_To_Bytes(MAC)  # 把MAC地址转换为二进制格式
    # param_req_list为请求的参数，没有这个部分服务器只会回送IP地址，什么参数都不给
    discover = Ether(dst='ff:ff:ff:ff:ff:ff',
                     src=MAC,
                     type=0x0800) / IP(src='0.0.0.0',
                                       dst='255.255.255.255') / UDP(dport=67,
                                                                    sport=68) / BOOTP(op=1,
                                                                                      chaddr=chaddr(Bytes_MAC)) / DHCP(
                                                                                                                        options=[('message-type', 'discover'),
                                                                                                                                 ('param_req_list',
                                                                                                                                  bytes_requested_options),
                                                                                                                                 ('end')])

    if wait_time != 0:
        time.sleep(wait_time)
        sendp(discover,
              iface=scapy_iface(ifname),
              verbose=False)
    else:
        sendp(discover,
              iface=scapy_iface(ifname),
              verbose=False)


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    Local_MAC = get_mac_address('Net1')
    DHCP_Discover_Sendonly('Net1', Local_MAC)
