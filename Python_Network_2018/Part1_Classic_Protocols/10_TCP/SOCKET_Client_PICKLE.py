#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import pickle
from io import BytesIO
from socket import *


def Client_PIC(ip, port, obj):
    msg = pickle.dumps(obj)  # 把obj pickle到一个二进制字串
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((ip, port))
    send_message = BytesIO(msg)  # 由于二进制字串无法按照长度读取，所以给他写到一个BytesIO
    send_message_fragment = send_message.read(1024)  # 读取1024字节长度数据
    while send_message_fragment:
        sockobj.send(send_message_fragment)  # 发送数据分片（如果分片的话）
        send_message_fragment = send_message.read(1024)  # 继续读取数据
    print('Pickle File Sended')
    sockobj.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    dict = {'key1': 'welcome to qytang', 'key2': [1, 2, 3, 4, 5], 'key3': ([3, 4], 'python')}
    myfile = open('Logo.jpg', 'rb').read()
    Client_PIC('10.1.1.100', 6666, dict)
    Client_PIC('10.1.1.100', 6666, myfile)
