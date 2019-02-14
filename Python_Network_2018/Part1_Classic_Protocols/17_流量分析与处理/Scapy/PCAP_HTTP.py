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
import re


def findpcapuri(pcap_filename, host_regex):
    # 本代码主要任务: 搜索PCAP文件里边的所有数据包,找到HTTP Host字段匹配正则表达式host_regex的HTTP请求数据包
    # 并收集这个HTTP请求的Host, URI , User_Agent字段
    pkts_file = rdpcap(pcap_filename)  # 使用scapy的rdpcap函数打开pcap文件
    pkt_list = pkts_file.res  # 提取每一个包到清单pkt_list
    result_list = []
    for packet in pkt_list:  # 分析每一个数据包
        try:
            if packet.getlayer(TCP).fields['dport'] == 80:  # 分析TCP目的端口为80的数据包
                http_request = packet.getlayer(Raw).fields['load'].split()
                # packet.show() 'GET /?nameAccount=4008519651&uid=3102224384&cb=JSONP_CALLBACK_5_61 HTTP/1.1\r\nHost: hb.crm2.qq.com\r\nConnection: keep-alive\r\nAccept: */*\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400\r\nReferer: http://edu.51cto.com/lecturer/index/user_id-9137368.html\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: zh-CN,zh;q=0.8\r\nCookie: cuid=7780981392; o_cookie=605658506; pgv_pvid=1509412600; RK=sSlPbf+CVr; ptcz=ce34b86a10a14784b025e777a361081e4e264d78d3e5fb1a793a8072659d499a; pt2gguin=o0605658506; uin=o0605658506; skey=@vk7UzceLE; qzone_check=605658506_1460939090\r\n\r\n'
                # print(http_request) [b'GET', b'/?nameAccount=4008519651&uid=3102224384&cb=JSONP_CALLBACK_5_61', b'HTTP/1.1', b'Host:', b'hb.crm2.qq.com', b'Connection:', b'keep-alive', b'Accept:', b'*/*', b'User-Agent:', b'Mozilla/5.0', b'(Windows', b'NT', b'10.0;', b'WOW64)', b'AppleWebKit/537.36', b'(KHTML,', b'like', b'Gecko)', b'Chrome/47.0.2526.80', b'Safari/537.36', b'Core/1.47.163.400', b'QQBrowser/9.3.7175.400', b'Referer:', b'http://edu.51cto.com/lecturer/index/user_id-9137368.html', b'Accept-Encoding:', b'gzip,', b'deflate,', b'sdch', b'Accept-Language:', b'zh-CN,zh;q=0.8', b'Cookie:', b'cuid=7780981392;', b'o_cookie=605658506;', b'pgv_pvid=1509412600;', b'RK=sSlPbf+CVr;', b'ptcz=ce34b86a10a14784b025e777a361081e4e264d78d3e5fb1a793a8072659d499a;', b'pt2gguin=o0605658506;', b'uin=o0605658506;', b'skey=@vk7UzceLE;', b'qzone_check=605658506_1460939090']
                Host_location = http_request.index(b'Host:') + 1  # 找到出现b'Host:'的下面一个位置
                Host = http_request[Host_location]  # 提取HTTP的host
                Host_ACSII = Host.decode()  # 解码为普通字符串
                if re.search(host_regex, Host_ACSII):  # 搜索匹配正则表达式的host
                    URI_location = http_request.index(b'GET') + 1
                    User_Agent_location = http_request.index(b'User-Agent:') + 1
                    URI = http_request[URI_location]  # 找到URI
                    User_Agent = http_request[User_Agent_location]  # 找到User Agent
                    result_list.append((Host, URI , User_Agent))  # 添加Host,URI和User_Agent到列表

        except:
            pass
    return result_list


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    result = findpcapuri("dos.pcap", 'sina\.com\.cn')

    # 对找到数据包进行展示,打印Host, URI , User_Agent
    # for http_info in result:
    #     print('====================================================================')
    #     print(b'Host: ' + http_info[0])
    #     print(b'URI: ' + http_info[1])
    #     print(b'User_Agent: ' + http_info[2])

    # 展示所有host, 使用集合技术, 去除重复部分
    host_list = []
    for http_info in result:
        host_list.append(http_info[0])
    print(host_list)
    print([i.decode() for i in list(set(host_list))])  # 使用集合技术,找到不重复的Host
