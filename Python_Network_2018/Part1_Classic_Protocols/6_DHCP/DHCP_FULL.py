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

from multiprocessing.pool import ThreadPool
from Part1_Classic_Protocols.Tools.Change_MAC_To_Bytes import Change_MAC_To_Bytes
from Part1_Classic_Protocols.Tools.GET_MAC_netifaces import get_mac_address
from Part1_Classic_Protocols.Tools.Change_Chaddr_To_MAC import Change_Chaddr_To_MAC
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字
from DHCP_Discover import DHCP_Discover_Sendonly
from DHCP_Request import DHCP_Request_Sendonly

pool = ThreadPool(processes=10)


def DHCP_Monitor_Control(pkt):
    try:
        if pkt.getlayer(DHCP).fields['options'][0][1] == 1:  # 发现并且打印DHCP Discover
            print('发现DHCP Discover包，MAC地址为:', end='')
            MAC_Bytes = pkt.getlayer(BOOTP).fields['chaddr']  # 提取Discover中的Client Hardware Addr
            MAC_ADDR = Change_Chaddr_To_MAC(MAC_Bytes)  # 把Client Hardware Addr转换为MAC地址
            print(MAC_ADDR)  # 打印MAC地址
            print('Request包中发现如下Options:')
            # 如下For循环,提取DHCP的选项信息,并且打印,param_req_list没有做解码字节打印
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                elif str(option[0]) == 'param_req_list':  # 记录请求参数清单
                    global param_req_list
                    param_req_list = option[1]
                # 打印所有选项
                print('%-15s ==> %s' % (str(option[0]), str(option[1])))

        elif pkt.getlayer(DHCP).fields['options'][0][1] == 2:  # 发现并且打印DHCP OFFER
            options = {}
            # 提取OFFER中的Client Hardware Addr
            MAC_Bytes = pkt.getlayer(BOOTP).fields['chaddr']
            # 把Client Hardware Addr转换为MAC地址
            MAC_ADDR = Change_Chaddr_To_MAC(MAC_Bytes)
            # 把从OFFER得到的信息读取并且写入options字典
            options['MAC'] = MAC_ADDR
            options['client_id'] = Change_MAC_To_Bytes(MAC_ADDR)
            options['requested_addr'] = pkt.getlayer(BOOTP).fields['yiaddr']
            print('发现DHCP OFFER包，请求者得到的IP为:' + pkt.getlayer(BOOTP).fields['yiaddr'])
            print('OFFER包中发现如下Options:')
            for option in pkt.getlayer(DHCP).fields['options']:
                if option == 'end':
                    break
                # 提取server_id选项,写入options字典
                elif option[0] == 'server_id':
                    options['Server_IP'] = option[1]
                # 打印所有选项
                print('%-15s ==> %s' % (str(option[0]), str(option[1])))
            # 发送DHCP Request,把从OFFER提取的选项和param_req_list信息,发送给制造DHCP Request的函数
            pool.apply_async(DHCP_Request_Sendonly, args=(Global_IF, options, param_req_list))

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


def DHCP_FULL(ifname, MAC, timeout=3):
    global Global_IF
    Global_IF = ifname
    # 发送DHCP Discover数据包
    pool.apply_async(DHCP_Discover_Sendonly, args=(Global_IF, MAC))
    # 侦听数据包,使用过滤器filter="port 68 and port 67"进行过滤,把捕获的数据包发送给DHCP_Monitor_Control函数进行处理
    sniff(prn=DHCP_Monitor_Control,
          filter="port 68 and port 67",
          store=0,
          iface=scapy_iface(Global_IF),
          timeout=timeout)


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    DHCP_FULL('ens33', get_mac_address('ens33'))
