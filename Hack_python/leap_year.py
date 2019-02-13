#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_leap(year):
    #year不能被400整除时要满足不能被100整除
    return year%4 ==0 and (year%400 ==0 or year%100!=0)
year = int(input())
print(is_leap(year))