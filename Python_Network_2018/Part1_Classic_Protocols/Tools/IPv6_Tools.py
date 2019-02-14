#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import re
import ipaddress


def full_ipv6(ipv6):  # 转换为完整的IPv6地址
    ipv6_section = ipv6.split(":")  # 对原始地址使用":"进行分割

    ipv6_section_len = len(ipv6.split(":"))  # 了解原始地址的分段数量

    if ipv6_section.index(''):
        null_location = ipv6_section.index('')  # 找到空位,这个地方要补0

        ipv6_section.pop(null_location)  # 把原来的空位弹出去

        add_section = 8 - ipv6_section_len + 1  # 计算需要补"0000"的个数

        for x in range(add_section):
            ipv6_section.insert(null_location, "0000")  # 开始补"0000"

        new_ipv6 = []
        for s in ipv6_section:
            if len(s) < 4:
                new_ipv6.append((4 - len(s)) * '0' + s)  # 对于不够长度的左边补"0"
            else:
                new_ipv6.append(s)
        return ':'.join(new_ipv6)  # 使用":"连接在一起成为完整的IPv6地址
    else:
        return ipv6


def Solicited_node_multicast_address(ipv6):
    return "FF02::1:FF" + full_ipv6(ipv6)[-7:]  # 拼接得到Solicited_node_multicast_address


def mac_to_ipv6_linklocal(mac):
    # 移除多余的字符 空格,冒号,点,减号
    # 转换16进制数到10进制数
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # 00:50:56:ab:4d:19为例

    # high2 使用移位">> 32"得到0050,
    # 使用"& 0xffff"确认只有4个16进制数,
    # 使用"^ 0x200"异或转换第七位,得到0250
    # 异或算法
    # >>> 0 ^ 1
    # 1
    # >>> 1 ^ 1
    # 0
    # high2 = 0250(其实是10进制,而不是这里显示的16进制)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    # high1 使用移位">> 24"得到005056,
    # 使用"& 0xff"得到最后两个16进制数,56
    # high1 = 56(其实是10进制,而不是这里显示的16进制)
    high1 = mac_value >> 24 & 0xff
    # low1 使用移位">> 16"得到005056ab,
    # 使用"& 0xff"得到最后两个16进制数,ab
    # low1 = ab(其实是10进制,而不是这里显示的16进制)
    low1 = mac_value >> 16 & 0xff
    # low2 使用"& 0xffff"得到最后4个16进制数,4d19
    # low2 = 4d19(其实是10进制,而不是这里显示的16进制)
    low2 = mac_value & 0xffff

    # 使用格式化打印,转换10进制位16进制,x为16进制字符串,并且使用02和04在控制长度,并且补0
    return 'fe80::{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(
        high2, high1, low1, low2)


def ipv6_to_mac(ipv6):
    # 以fe80::0250:56ff:feab:4d19为例
    # 把ipv6切换为完整的ipv6地址,填充0000
    # ipv6完整地址为fe80:0000:0000:0000:0250:56ff:feab:4d19
    ipv6_address = full_ipv6(ipv6)

    # 使用":"进行分离,并且提取后4个部分
    # ['0250', '56ff', 'feab', '4d19']
    last_4_sections = ipv6_address.split(":")[-4:]

    # 提取第1个部分的前2位,从16进制转为10进制,
    # 使用"^0x02"异或转换第七位
    mac_1 = int(last_4_sections[0][:2], 16) ^ 0x02
    # 提取MAC后续部分(2个16进制位单位),从16进制转为10进制,
    mac_2 = int(last_4_sections[0][2:], 16)
    mac_3 = int(last_4_sections[1][:2], 16)
    mac_4 = int(last_4_sections[2][2:], 16)
    mac_5 = int(last_4_sections[3][:2], 16)
    mac_6 = int(last_4_sections[3][2:], 16)
    # 使用格式化打印,转换10进制位16进制,x为16进制字符串,并且使用02控制长度,并且补0
    return '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(
        mac_1, mac_2, mac_3, mac_4, mac_5, mac_6)

# 微软默认并不使用EUI64地址,而是随机产生
# https://www.dan.me.uk/blog/2011/02/10/windows-7-ipv6-auto-assignment-fix/
# netsh interface ipv6 set privacy state=disabled store=active
# netsh interface ipv6 set privacy state=disabled store=persistent
# netsh interface ipv6 set global randomizeidentifiers=disabled store=active
# netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent

def mac_to_eui64(mac, prefix):
    # 移除多余的字符 空格,冒号,点,减号
    # 转换16进制数到10进制数
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # 00:50:56:ab:4d:19为例

    # high2 使用移位">> 32"得到0050,
    # 使用"& 0xffff"确认只有4个16进制数,
    # 使用"^ 0x200"异或转换第七位,得到0250
    # high2 = 0250(其实是10进制,而不是这里显示的16进制)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    # high1 使用移位">> 24"得到005056,
    # 使用"& 0xff"得到最后两个16进制数,56
    # high1 = 56(其实是10进制,而不是这里显示的16进制)
    high1 = mac_value >> 24 & 0xff
    # low1 使用移位">> 16"得到005056ab,
    # 使用"& 0xff"得到最后两个16进制数,ab
    # low1 = ab(其实是10进制,而不是这里显示的16进制)
    low1 = mac_value >> 16 & 0xff
    # low2 使用"& 0xffff"得到最后4个16进制数,4d19
    # low2 = 4d19(其实是10进制,而不是这里显示的16进制)
    low2 = mac_value & 0xffff

    # 使用格式化打印,转换10进制位16进制,x为16进制字符串,并且使用02控制长度,并且补0
    host_id = '{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)

    # 提取prefix字符串"/"之前的部分
    net = prefix.split("/")[0]

    return net + host_id


if __name__ == '__main__':
    print(mac_to_eui64(mac='06:b2:4a:00:00:9f', prefix='2001:db8:100::/64'))
