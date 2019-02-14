#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import poplib, getpass, sys
import re
import os
import email
import base64


def qyt_rec_mail(mailserver, mailuser, mailpasswd):
    print('Connecting...')
    server = poplib.POP3_SSL(mailserver, 995)  # 连接到邮件服务器
    server.user(mailuser)  # 邮件服务器用户名
    server.pass_(mailpasswd)  # 邮件服务器密码
    mails_list = []
    try:
        print(server.getwelcome())  # 打印服务器欢迎信息
        msgCount, msgBytes = server.stat()  # 查询邮件数量与字节数
        print('There are', msgCount, 'mail message in', msgBytes, 'bytes')  # 打印邮件数量与字节数
        print(server.list())  # 打印邮件清单

        for i in range(msgCount):  # 逐个读取邮件
            hdr, message, octets = server.retr(i + 1)  # 读取邮件
            str_message = email.message_from_bytes(b'\n'.join(message))  # 把邮件内容拼接到大字符串
            part_list = []
            mail_dict = {}
            for part in str_message.walk():  # 把邮件的多个部分添加到part_list
                part_list.append(part)

            # 把邮件的第一个[0]部分内容提取出来写入字典mail_dict
            # 注意第一部分,所有邮件都会存在,是邮件的头部信息
            for x, y in part_list[0].items():
                mail_dict[x] = y

            # 初始化附件为空列表
            mail_dict['Attachment'] = []
            # 如果邮件包含多个部分,这个时候就有可能出现正文和附件
            if len(part_list) > 1:
                # 提取第二部分往后的内容
                for i in range(1, len(part_list)):
                    # 提取文件名,如果没有文件名返回空,如果有文件名,表示这个部分为附件部分
                    filename = part_list[i].get_filename()
                    if filename:
                        # 如果有文件名就向附件列表中,追加附件文件
                        attach = mail_dict.get('Attachment')
                        attach.append((filename, part_list[i].get_payload()))
                        mail_dict['Attachment'] = attach  # 把附件列表添加到邮件字典
                    else:  # 如果没有文件名,表示是正文,把正文'Body'添加到邮件字典
                        mail_dict['Body'] = part_list[i].get_payload()
            # 把邮件字典,添加到邮件列表清单
            mails_list.append(mail_dict)

        for i in range(msgCount):  # 逐个读取邮件
            server.dele(i + 1)
    finally:
        server.quit()  # 退出服务器

    return mails_list


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    qyt_rec_mail('pop.qq.com', '3348326959@qq.com', 'dmyymagcazklcjie')
