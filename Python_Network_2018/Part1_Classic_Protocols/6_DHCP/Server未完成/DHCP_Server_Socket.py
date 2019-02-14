#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from socket import *
from PyQYT.Network.DHCP.DHCP_Unpack_Options import DHCP_Unpack_Options
from POOLs import pools, find_pool_config

HOST = ''
PORT = 67
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

DHCP_State_Record = {}

try:
    while True:
        print('wating for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        options = DHCP_Unpack_Options(data)
        print(find_pool_config(options[0]['GIADDR']))

except KeyboardInterrupt:  # 捕获Ctrl+C，打印信息并退出
    print("Crtl+C Pressed. Shutting down.")
    udpSerSock.close()
