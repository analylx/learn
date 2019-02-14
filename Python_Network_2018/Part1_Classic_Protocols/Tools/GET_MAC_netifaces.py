#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import netifaces
import platform
from Part1_Classic_Protocols.Tools.GET_IFNAME import get_ifname


def get_mac_address(ifname):
    return netifaces.ifaddresses(get_ifname(ifname))[netifaces.AF_LINK][0]['addr']


if __name__ == '__main__':
    print(get_mac_address("Net1"))
    # print(get_mac_address("ens33"))
