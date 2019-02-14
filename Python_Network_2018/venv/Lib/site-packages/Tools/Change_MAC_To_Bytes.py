#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import struct
import re


def Change_MAC_To_Bytes(mac):
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    section1 = mac_value >> 40 & 0xff
    section2 = mac_value >> 32 & 0xff
    section3 = mac_value >> 24 & 0xff
    section4 = mac_value >> 16 & 0xff
    section5 = mac_value >> 8 & 0xff
    section6 = mac_value & 0xff
    Bytes_MAC = struct.pack('!6B', section1, section2, section3, section4, section5, section6)
    return Bytes_MAC


if __name__ == "__main__":
    print(Change_MAC_To_Bytes("00:50:56:AB:25:08"))
