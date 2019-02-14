#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import random


def Random_Section():
    section = random.randint(1, 254)
    return section


def Random_IP():
    IP = str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section())
    return IP


if __name__ == '__main__':
    print(Random_IP())
