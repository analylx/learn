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
    server = poplib.POP3_SSL(mailserver,995)  # 连接到邮件服务器
    server.user(mailuser)  # 邮件服务器用户名
    server.pass_(mailpasswd)  # 邮件服务器密码

    try:
        print(server.getwelcome())  # 打印服务器欢迎信息
        msgCount, msgBytes = server.stat()  # 查询邮件数量与字节数
        print('There are', msgCount, 'mail message in', msgBytes, 'bytes')  # 打印邮件数量与字节数
        print(server.list())  # 打印邮件清单

        for i in range(msgCount):  # 逐个读取邮件
            hdr, message, octets = server.retr(i + 1)  # 读取邮件
            str_message = email.message_from_bytes(b'\n'.join(message))  # 把邮件内容拼接到大字符串

            for part in str_message.walk():
                if part.get_content_maintype() == 'multipart':
                    part_dict = part.items()
                    for key in part_dict:
                        if key[0] == 'Subject':
                            # =?utf-8?b?6ZmE5Lu25rWL6K+VX+S4u+mimA==?=
                            #   utf-8   6ZmE5Lu25rWL6K+VX+S4u+mimA== (转码后为:附件测试_主题)
                            if re.match('=\?(.*)\?\w\?(.*)=\?', key[1]).groups():
                                re_result = re.match('=\?(.*)\?\w\?(.*)\?=', key[1]).groups()
                                # re_result[0] 为编码方式
                                middle = re_result[1]  # 提取base64的内容 6ZmE5Lu25rWL6K+VX+S4u+mimA==
                                decoded = base64.b64decode(middle)  # 对内容进行base64解码
                                mail_prefix = str(decoded.decode(re_result[0]))  # 再对base64解码后内容,进行utf-8解码,转换为中文内容
                            else:
                                mail_prefix = key[1]  # 英文就直接显示
                    continue
                filename = part.get_filename()  # 获取文件名

                if filename is None:  # 没有文件名表示文本信息
                    mail_file_name = mail_prefix + '_' + str(i) + '.txt'
                    fp = open(mail_file_name, 'wb')  # 把文本内容写入txt文件
                    for key in part_dict:
                        string = key[0] + '===>' + key[1] + '\n'
                        fp.write(string.encode())
                    fp.write(b'Main Body ===>')
                    fp.write(part.get_payload(decode=1))  # 写入正文
                    fp.close
                else:  # 如果有文件名表示是附件,单独保存附件数据
                    filename = filename.encode("utf-8").decode()
                    mail_file_name = mail_prefix + '_' + str(i) + '+' + filename
                    fp = open(mail_file_name, 'wb')
                    fp.write(part.get_payload(decode=1))
                    fp.close
            server.dele(i + 1)  # 删除邮件

    finally:
        server.quit()  # 退出服务器
    print('Bye.')


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    qyt_rec_mail('pop.qq.com', '3348326959@qq.com', 'dmyymagcazklcjie')
