#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from Part1_Classic_Protocols.Tools.minimumTFTP import Client


def qyt_ftpclient(server, filedir, file, operation=1):
    tftpClient = Client(server, filedir, file)
    if operation == 1:
        tftpClient.get()
    if operation == 2:
        tftpClient.put()
    print()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径
    # /usr/local/lib/python3.6/site-packages/Tools/minimumTFTP.py

    qyt_ftpclient('10.1.1.80', '.', 'testupload.txt', operation=1)
    # qyt_ftpclient('10.1.1.80', '.', 'testupload.txt', operation=2)
