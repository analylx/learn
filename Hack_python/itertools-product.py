from itertools import product

a = map(int, input().split())
b = map(int, input().split())
# print(product(a, b)) -> <itertools.product object at 0x000002A804B78048>
# 并且会消耗掉结果，下面的那个print就没有输出
print(*product(a, b))

"""
import itertools

A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

print(*itertools.product(A, B))
arr = [1, 2, 3]
print(*arr) # unpack arr --> print(1, 2, 3)
"""
