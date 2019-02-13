# coding utf-8
#打印一串数字，从1开始

n = int(input())
for m in range(1, n + 1):
    print(m, end='')
# do the above within single line
#*range 就是对range的解包，这里的效果是将列表转化为原本的内容
#print(*range(1, int(input())+1), sep='')
