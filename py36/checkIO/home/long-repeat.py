# 准备先过滤出连续的字符，再计算个数。如果没有连续超过两个的就返回1.
"""
import itertools
def long_repeat(line):
    groups = []
    for k, g in itertools.groupby(line):
        groups.append(list(g))
    try:
        return len(max(groups, key=len))
    except:
        return 0
"""        
def long_repeat(line):
    return max([i for i in range(1, len(line) + 1) if any([True for char in line if line.find(char * i) != -1])]) if line != '' else 0
"""
def long_repeat(line):
    import re
    #主要还是看这里的正则表达式怎么匹配
    lst = sorted(len(i[0]) for i in re.findall(r'((\w)\2*)', line))
    #and的用法是：如果前面的是false，就返回false，否则返回后面的计算值。len(lst)的值=0的时候就是false，返回这个0等价于false，如果这个列表里面有值，返回最后一个最大的值
    return len(lst) and lst[-1]

def long_repeat(line):
    count =0
    for char in line:
        newchar = char
        #每个字符不断的加1然后去和原始字符串比较算count，一旦没匹配了说明达到最长的重复数了，跳出循环.
        #想不明白的时候带入一个值走一遍就清楚了
        while(line.count(newchar)>0):
            newchar += char
        #print (newchar)
        if count < len(newchar)-1:
            count = len(newchar)-1
    return count
""" 
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')