# -*- coding: UTF-8 -*-

import os
print "在每行代码的结尾加上’；‘对实际结果没影响\n";

'''
在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾。
两种解决方式: 其一，先 close 文件，open 后再读取，其二，可以设置指针回到文件最初后再 read
'''

document = open("testfile.txt", "w+")
print 'Filename: %s' %document.name
document.write("这是我创建的第一个测试文件！\nwelcome!")
print (document.tell())
#输出当前指针位置
document.seek(os.SEEK_SET)
#设置指针回到文件最初
context = document.read()
print (context)
document.close()
'''
为了保证无论是否出错都能正确地关闭文件，我们可以使用 try ... finally 来实现:
但是每次都这么写实在太繁琐，所以，Python 引入了 with 语句来自动帮我们调用 close() 方法：
这和前面的 try ... finally 是一样的，但是代码更佳简洁，并且不必调用 f.close() 方法。
'''
with open("testfile.txt", 'r') as f:
    print f.read()