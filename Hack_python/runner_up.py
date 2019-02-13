#-*- coding: utf-8 -*-
#输入：第一行给出元素的个数，第二行输入一个整数数组。输出排列时第二大的那个数字
"""def get_runner_up(total,numbers):
    
    if  numbers.[i]>numbers.[i+1]:
        runner_up_one = numbers.[i]
    return runner_up_one
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print get_runner_up(n,arr)"""

"""
n = int(input())
nums = map(int, input().split())
print(input()==0 or sorted(list(set(map(int,input().split()))))[-2])   
#print sorted(list(set(nums)))[-2]
"""

dn,arr=(input() for _ in range(2))
nums = map(int, arr.split())
a=sorted(list(set(nums)))#通过集合去掉重复的元素
if(len(a)==1):
    print(a[0])
else:
    print(a[-2])