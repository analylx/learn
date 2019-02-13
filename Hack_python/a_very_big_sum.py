#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    result = 0
    for a in ar:
        result += n*a
    return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)