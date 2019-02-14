#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import os
import sqlite3
from POP3_Final import qyt_rec_mail
import json
from dateutil import parser
import re
import base64


def createdb(dbname):
    if os.path.exists(dbname):
        os.remove(dbname)
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 创建数据库
    cursor.execute("create table maildb(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                        time varchar(64), \
                                        to_ varchar(32),\
                                        from_ varchar(32),\
                                        subject varchar(4096),\
                                        body varchar(40960),\
                                        attach_ varchar(40960000))")
    conn.commit()


def writedb(dbname, time, to_, from_, subject, body, attach):
    # 把内容写入数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("insert into maildb (time, \
                                        to_, \
                                        from_, \
                                        subject, \
                                        body, \
                                        attach_) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (time,
                                                                                                to_,
                                                                                                from_,
                                                                                                subject,
                                                                                                body,
                                                                                                attach))
    conn.commit()


def time_format(str):
    # 把时间字符串,转换为时间对象
    time = str.split(',')[1]
    time = time.split()
    time_obj = parser.parse(' '.join(time[:-1]))
    return time_obj


def decode_subject_base64(str):
    # 解码如下内容
    # =?utf-8?b?6ZmE5Lu25rWL6K+VX+S4u+mimA==?=
    #   utf-8   6ZmE5Lu25rWL6K+VX+S4u+mimA== (转码后为:附件测试_主题)
    try:
        re_result = re.match('=\?(.*)\?\w\?(.*)\?=', str).groups()
        # re_result[0] 为编码方式
        middle = re_result[1]  # 提取base64的内容 6ZmE5Lu25rWL6K+VX+S4u+mimA==
        decoded = base64.b64decode(middle)  # 对内容进行base64解码
        decoded_str = decoded.decode(re_result[0])  # 再对base64解码后内容,进行utf-8解码,转换为中文内容
    except Exception as e:
        decoded_str = str
    return decoded_str


def mails_write_db(dbname, popaddress, username, password):
    createdb(dbname)
    for mail_dict in qyt_rec_mail(popaddress, username, password):  # 获取有邮件清单
        # 获取时间,并且格式化时间
        time = mail_dict.get('Date', 'N/A')
        time_format(time)
        time = time_format(time).strftime("%Y-%m-%d %H:%M:%S")

        # 获取邮件目的
        to_ = mail_dict.get('To', 'N/A')

        # 获取邮件源
        from_ = mail_dict.get('From', 'N/A')

        # 获取邮件主题, 需要转码, 解决可能出现的中文问题
        subject = decode_subject_base64(mail_dict.get('Subject', 'N/A'))

        # 获取正文
        body = mail_dict.get('Body', 'N/A')

        # 正文可能是base64 编码后的中文,需要处理,当然如果处理失败就保留原始数据
        if body != 'N/A':
            try:
                body = base64.b64decode(mail_dict.get('Body', 'N/A')).decode('utf-8')
            except:
                pass

        # 提取附件内容
        attach = json.dumps(mail_dict.get('Attachment', 'N/A'))

        # 把邮件信息写入数据库
        writedb(dbname, time, to_, from_, subject, body, attach)


def show_mail(dbname):
    # 连接数据库,读取邮件信息
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("select * from maildb")
    yourresults = cursor.fetchall()

    # 查看是否有附件内容
    for i in yourresults:
        if i[6] == '[]':
            attch = 'NO'
        else:
            attch = 'YES'
        # 打印邮件信息
        print('ID: %d 时间: %s FROM: %s 主题: %s 正文: %s 是否有附件: %s' % (i[0], i[1], i[3], i[4], i[5][:100], attch))

    # 让客户判断是否把附件保存为文件
    mail_id = input('输入需要保存附件的邮件ID:')

    # 提取客户需要保存附件的邮件的附件
    cursor.execute("select attach_ from maildb where id=%s" % mail_id)
    yourresults = cursor.fetchall()

    # 把附件内容使用json,转换为Python对象(列表)
    files = json.loads(yourresults[0][0])

    # 把附件保存为本地文件
    for file in files:
        filename = file[0]
        fp = open(filename, 'wb')
        fp.write(base64.b64decode(file[1]))
        fp.close


if __name__ == '__main__':
    # mails_write_db('maildb.sqlite', 'pop.qq.com', '3348326959@qq.com', 'dmyymagcazklcjie')
    show_mail('maildb.sqlite')