#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.


def solve(s):
    a = s.split(' ')
    return " ".join(word.capitalize() for word in a)


if __name__ == '__main__':
    s = input()
    print(solve(s))
