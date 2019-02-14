# coding=utf-8
import re

r1= re.compile(r'way')
with open('newfile.txt','r') as f:
    for a in f.readlines():
        s = re.search(r1,a)

        #如果加了re.M|re.I就不能用预编译的pattern
        #如果没有匹配到那么b的值就是none，此时的b是没有group属性的。先判断b再取值
        if s:
            print(a)
