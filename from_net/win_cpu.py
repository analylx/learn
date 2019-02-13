# -*- coding: utf-8 -*-
import os
from typing import List


def get_cpu_load():
    """ Returns a list CPU Loads"""
    result: List[int] = []
    cmd = "WMIC CPU GET LoadPercentage "
    response = os.popen(cmd + ' 2>&amp;1','r').read().strip().split("\r\n")
    for load in response[1:]:
       result.append(int(load))
    return result

if __name__ == '__main__':
    print(get_cpu_load())