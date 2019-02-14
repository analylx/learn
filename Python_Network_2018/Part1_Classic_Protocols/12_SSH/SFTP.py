#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import paramiko, os, sys, time


def ssh_sftp_put(ip, user, password, local_file, remote_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.put(local_file, remote_file)  # 上传本地文件到服务器


def ssh_sftp_get(ip, user, password, remote_file, local_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.get(remote_file, local_file)  # 下载服务器文件到本地


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    ssh_sftp_put('10.1.1.80', 'root', 'Cisc0123', 'Adv_SSH_Client.py', 'Adv_SSH_Client.py', port=22)
    ssh_sftp_get('10.1.1.80', 'root', 'Cisc0123', 'get-pip.py', 'get-pip.py', port=22)