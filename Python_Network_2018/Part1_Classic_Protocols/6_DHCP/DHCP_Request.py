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
import time
from DHCP_Discover import chaddr
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字

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


def DHCP_Request_Sendonly(ifname, options, param_req_list, wait_time=1):
    request = Ether(dst='ff:ff:ff:ff:ff:ff',
                    src=options['MAC'],
                    type=0x0800) / IP(src='0.0.0.0',
                                      dst='255.255.255.255') / UDP(dport=67, sport=68) / BOOTP(op=1,
                                                                                               chaddr=chaddr(options['client_id']),
                                                                                               siaddr=options['Server_IP'], ) / DHCP(options=[('message-type', 'request'),
                                                                                                                                              ('server_id', options['Server_IP']),
                                                                                                                                              ('requested_addr', options['requested_addr']),
                                                                                                                                              # Hardware_Type = 1(一个字节),需要添加在client_id前面
                                                                                                                                              ('client_id', b'\x01' + options['client_id']),
                                                                                                                                              ('param_req_list', param_req_list),
                                                                                                                                              ('end')])
    if wait_time != 0:
        time.sleep(wait_time)
        sendp(request,
              iface=scapy_iface(ifname),
              verbose=False)
    else:
        sendp(request,
              iface=scapy_iface(ifname),
              verbose=False)


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    options = {'MAC': '00:0c:29:8d:5c:b6', 'Server_IP': '202.100.1.168', 'requested_addr': '202.100.1.1',
               'client_id': b'\x00\x0c)\x8d\\\xb6'}
    DHCP_Request_Sendonly('ens33', options, bytes_requested_options)
