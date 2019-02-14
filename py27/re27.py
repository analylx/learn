# -*- coding: utf-8 -*-
import re
"""
r1 = re.compile("192")
with open("ifconfig.txt","r") as f:

"""
r1 = re.compile(r'world')
#match是从头开始匹配，匹配不到就返回None，再加not就返回True
if r1.match('helloworld'):
    print 'match succeeds'
else:
    print not r1.match('helloworld')
#search是整个字符串匹配,找不到返回None，但是匹配之后的返回值看不懂，加not还是会返回False
    print r1.search('helloworld')
    print not r1.search('helloworld')


#r2 = re.compile(r'n$', re.S)
#r2 = re.compile('\n$', re.S)
r2 = re.compile('World$', re.I)
if r2.search('helloworld\n'):
    print 'search succeeds'
else:
    print 'search fails' 

if re.search(r'abc','helloaaabcdworldn'):
    print 'search succeeds'
else:
    print 'search fails'

#编译后调用和直接调用split返回不一样的结果的原因是()。加了()会返回间隔符号的原理？()好像表示group
r1 = re.compile('\W+')#"\W"匹配非数字和字母
r1 = re.compile(r'\W+')
print r1.split('192.168.1.1')
print r2.split('192.168.1.1')
print re.split('\W+', '192.168.1.1')
print re.split('(\W+)', '192.168.1.1')
print re.split('(\W+)', '192.168.1.1', 1)

#findall 在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
r1 = re.compile('([.*])')#[]    Indicates a set of characters.这些特殊字符在里面就是普通字符了
print re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo")
print re.findall('.*', "hello[hi]heldfsdsf[iwonder]lo")#这里.*表示一行中的任意字符，并且单独的*无效
print re.findall('[0-9]{2}',"fdskfj1323jfkdj56778")
print re.findall('([0-9][a-z])',"fdskfj1323jfkdj")
print re.findall('(?=www)',"afdsfwwwfkdjfsdfsdwww")#只是标记出位置但是返回啥都没有
print re.findall('(?<=www)',"afdsfwwwfkdjfsdfsdwww") 