#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from Simple_SSH_Client import QYT_SSHClient_SingleCMD


def monitor_sshd(ip):
    username = 'root'
    password = 'Cisc0123'
    result = QYT_SSHClient_SingleCMD(ip, username, password, 'systemctl status sshd')
    result_list = result.split('\n')
    for x in result_list:
        if x.split()[0] == 'Active:':
            #print(x)
            return x.split()[1] + x.split()[2]


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(monitor_sshd('10.1.1.80'))
