#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import json
from socket import *


def Client_JSON(ip, port, obj):
    # 创建TCP Socket并连接
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((ip, port))

    # 把obj转换为JSON字节字符串
    send_message = json.dumps(obj).encode()
    # 读取1024字节长度数据, 准备发送数据分片
    send_message_fragment = send_message[:1024]
    # 剩余部分数据
    send_message = send_message[1024:]

    while send_message_fragment:
        sockobj.send(send_message_fragment)  # 发送数据分片（如果分片的话）
        send_message_fragment = send_message[:1024]  # 读取1024字节长度数据
        send_message = send_message[1024:]  # 剩余部分数据
    sockobj.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    dict1 = {'key1': 'welcome to qytang', 'key2': [1, 2, 3, 4, 5], 'key3': ([3, 4], 'python'),'key4': 'python'*2048}
    dict2 = {'key1': 'welcome to qytang', 'key2': [1, 2, 3, 4, 5], 'key3': ([3, 4], 'python'), 'key4': 'python'}
    Client_JSON('10.1.1.100', 6666, dict1)
    Client_JSON('10.1.1.100', 6666, dict2)
