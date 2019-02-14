#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from socket import socket, AF_PACKET, SOCK_RAW
from Part1_Classic_Protocols.Tools.Checksum import do_checksum
from Part1_Classic_Protocols.Tools.Change_IP_To_Bytes import Change_IP_To_Bytes
from Part1_Classic_Protocols.Tools.Change_MAC_To_Bytes import Change_MAC_To_Bytes
import struct
import random


def Ether(src, dst, ether_type="0800"):
    # 构建源MAC地址,6个字节
    src_mac_addr = Change_MAC_To_Bytes(src)
    # 构建目的MAC地址,6个字节
    dst_mac_addr = Change_MAC_To_Bytes(dst)
    # 以太网类型为2个字节
    ether_type = struct.pack('!H', int(ether_type, 16))
    # 拼接以太网头部,并返回
    return src_mac_addr + dst_mac_addr + ether_type


def IP(version=4, header_length=5, tos=b"\x00", Total_Length=100, Identifier=random.randint(1, 65535),
       IP_Flags_D=0, IP_Flags_M=0, Offset=0, TTL=128, Protocol=17, src="127.0.0.1", dst="127.0.0.1"):
    # 构建IP版本与IP头部长度的第一个字节
    version_headerlength = struct.pack('B', (((version << 4) + header_length) & 0xff))

    # TOS为以传入的内容为准, TOS为第二个字节

    # 构建IP总长度,第三,第四个字节
    Total_Length = struct.pack("!H", Total_Length)

    # 构建IP ID,第五,第六个字节
    Identifier = struct.pack("!H", Identifier)

    # 构建分片相关部分,第七,第八个字节
    Fragment = struct.pack('!H', (((IP_Flags_D << 14) + (IP_Flags_M << 13) + Offset) & 0xffff))

    # TTL,第九个字节
    TTL = struct.pack("B", TTL)

    # 协议,第十个字节
    Protocol = struct.pack("B", Protocol)

    # 初始校验和填0,第十一,第十二个字节
    Pre_IP_CheckSUM = b"\x00\x00"

    # 源IP地址,第十三到第十六个字节
    src_ip_address = Change_IP_To_Bytes(src)

    # 目的IP地址,第十七到第二十个字节
    dst_ip_address = Change_IP_To_Bytes(dst)

    # 为了计算校验和,把IP头部拼接起来
    pre_ip_header = version_headerlength + tos + Total_Length + Identifier + Fragment + TTL + Protocol + Pre_IP_CheckSUM + src_ip_address + dst_ip_address

    # 计算校验和
    checksum = do_checksum(pre_ip_header)

    # 重新拼接IP头部,放入校验和字段
    ip_hder = version_headerlength + tos + Total_Length + Identifier + Fragment + TTL + Protocol + checksum + src_ip_address + dst_ip_address

    # 返回IP头部
    return ip_hder


def UDP(src_port, dst_port, udp_length, u_data, src_ip_address, dst_ip_address, Protocol=17):
    # 构建源端口字段, 第一,第二个字节
    sourc_port = struct.pack("!H", src_port)

    # 构建目的端口字段,第三,第四个字节
    dest_port = struct.pack("!H", dst_port)

    # 构建UDP长度字段,第五,第六个字节
    udp_length = struct.pack("!H", udp_length)

    # 初始化校验和填0
    pre_udp_checksum = b"\x00\x00"

    # UDP数据
    u_data = u_data.encode()

    # 如果长度为偶数,不用添加垫片
    if len(u_data) % 2 == 0:
        pad = b""
    # 如果长度为基数,需要添加垫片b"\x00"
    else:
        pad = b"\x00"

    # 计算UDP校验和
    udp_check_sum = do_checksum(Change_IP_To_Bytes(src_ip_address) +
                                Change_IP_To_Bytes(dst_ip_address) +
                                b"\x00" +
                                struct.pack("B", Protocol) +
                                udp_length +
                                sourc_port +
                                dest_port +
                                udp_length +
                                pre_udp_checksum +
                                u_data +
                                pad)

    # 拼接UDP头部,放入校验和
    udp_hder = sourc_port + dest_port + udp_length + udp_check_sum

    # 返回UDP头部
    return udp_hder


if __name__ == "__main__":
    # 只适用于Linux解释器
    # 创建原始套接字
    s = socket(AF_PACKET, SOCK_RAW)
    # 绑定到本地端口
    s.bind(("ens33", 0))

    # 本次试验需要WIN作为服务器,Linux作为客户端连接
    dst_ip = "10.1.1.100"
    src_ip = "10.1.1.80"

    # UDP传输数据
    udp_data = "cisco123456"
    # 计算IP总长度
    t_length = 20 + 8 + len(udp_data)
    # 计算UDP总长度
    u_length = 8 + len(udp_data)
    # 产生以太网头部
    ether_header = Ether("00-50-56-AB-5C-02", "00:50:56:ab:25:08", "0800")
    # 产生IP头部
    ip_header = IP(Total_Length=t_length, IP_Flags_D=0, IP_Flags_M=0, Offset=0, TTL=128, Protocol=17, src=src_ip,
                   dst=dst_ip)
    # 产生UDP头部
    udp_header = UDP(1024, 6666, udp_length=u_length, u_data=udp_data, src_ip_address=src_ip,
                     dst_ip_address=dst_ip)
    # 拼接以太网头部,IP头部,UDP头部
    packet = ether_header + ip_header + udp_header + udp_data.encode()
    # 发送数据包
    s.send(packet)
