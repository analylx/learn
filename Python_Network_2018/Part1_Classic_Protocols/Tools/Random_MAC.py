#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import random


def hex():
    hex_mac = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'e', 'f'])
    return str(hex_mac)


def Random_MAC():
    MAC = hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex()
    return MAC


if __name__ == '__main__':
    print(Random_MAC())
