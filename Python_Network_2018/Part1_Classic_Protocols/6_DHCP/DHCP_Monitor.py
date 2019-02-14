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
from Part1_Classic_Protocols.Tools.Change_Chaddr_To_MAC import Change_Chaddr_To_MAC
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字


def DHCP_Monitor(pkt):
    try:
        if pkt.getlayer(DHCP).fields['options'][0][1] == 1:  # 发现并且打印DHCP Discover
            print('发现DHCP Discover包，MAC地址为:', end='')
            MAC_Bytes = pkt.getlayer(BOOTP).fields['chaddr']  # 提取Discover中的Client Hardware Addr
            MAC_ADDR = Change_Chaddr_To_MAC(MAC_Bytes)  # 把Client Hardware Addr转换为MAC地址
            print(MAC_ADDR)  # 打印MAC地址
            print('Request包中发现如下Options:')
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                # 打印所有选项
                print('%-15s ==> %s' % (str(option[0]), str(option[1])))

        elif pkt.getlayer(DHCP).fields['options'][0][1] == 2:  # 发现并且打印DHCP OFFER
            print('发现DHCP OFFER包，请求者得到的IP为:' + pkt.getlayer(BOOTP).fields['yiaddr'])
            print('OFFER包中发现如下Options:')
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                # 打印所有选项
                print('%-15s ==> %s' % (str(option[0]), str(option[1])))

        elif pkt.getlayer(DHCP).fields['options'][0][1] == 3:  # 发现并且打印DHCP Request
            print('发现DHCP Request包，请求的IP为:' + pkt.getlayer(BOOTP).fields['yiaddr'])
            print('Request包中发现如下Options:')
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                elif str(option[0]) == "client_id":
                    # 在打印client_id时,转换为MAC地址,便于客户查看
                    print('%-15s ==> %s' % (str(option[0]), str(option[1])
                                            + " 转换为MAC:" + Change_Chaddr_To_MAC(option[1][1:] + b"\x00" * (16 - len(option[1][1:])))
                                            )
                         )
                else:
                    # 打印其它所有选项,param_req_list保持原始字节形式打印
                    print('%-15s ==> %s' % (str(option[0]), str(option[1])))
        elif pkt.getlayer(DHCP).fields['options'][0][1] == 5:  # 发现并且打印DHCP ACK
            print('发现DHCP ACK包，确认的IP为:' + pkt.getlayer(BOOTP).fields['yiaddr'])
            print('ACK包中发现如下Options:')
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                # 打印DHCP ACK的所有选项
                print('%-15s ==> %s' % (str(option[0]), str(option[1])))
    except Exception as e:
        print(e)
        pass


def DHCP_Sinffer(ifname):
    sniff(prn=DHCP_Monitor,
          filter="port 68 and port 67",
          iface=scapy_iface(ifname),
          store=0)


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    DHCP_Sinffer('Net1')
