#-*- coding: utf-8 -*-
import os

print "os.getcwd()=" + os.getcwd()
path1 = os.path.dirname(__file__)
#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
#Returns the final component of a pathname
path4 = os.path.basename(path1)
print 'The os.path.dirname(__file__) is->', path1
print 'The os.path.basename(path1) is->', path4

print "print时如果是两个字符串类型的可以用+号，下面是字符串和bool类型混合，可以用用逗号分隔，输出自动添加空格分隔:"
print "os.path.exists(path1)=" , os.path.exists(path1)
print os.path.exists('E:\\')
#win10系统如下两种都表示当前盘符下的根目录的绝对路径
path2_1 = os.path.abspath("/")
print 'The path2_1 is->', path2_1
path2_1 = os.path.abspath("\\")
print 'The path2_1 is->', path2_1
path2_2 = os.path.abspath(path1)
print 'The path2_2 is->', path2_2

print "join将目录名和文件的基名拼接成一个完整的路径:"
path3 = os.path.join(path1,"file1.txt")
print 'The os.path.join(path1,"file1.txt") is->', path3
print r"还可以加上额外的路径,不要以\开始，不然会被认作是绝对路径"
path3 = os.path.join(path1,"script\\file1.txt")
print 'The os.path.join(path1,"file1.txt") is->', path3
print "添加路径之后前面的路径就加不上去了:If any component is an absolute path, all previous path components will be discarded."
path3 = os.path.join(path1,"\\script\\file1.txt")
print 'The os.path.join(path1,"\\script\\file1.txt") is->', path3
#将路径中最后的那个斜杠后的内容拆分出来，如果是指向文件的完整路径，那就是分割出文件名和路径
print "split分割目录名，返回由其目录名和基名给成的元组"
path4 = os.path.split(path3)
print 'The path4 is->', path4
print "splitext分割文件名，返回由文件名和扩展名组成的元组.文件名包括前面的路径"
path4 = os.path.splitext(path3)
print 'The path4 is->', path4

print "如果结果是个文件的话即使存在也会返回false"
print "os.path.exists(path3):", os.path.exists(path3)
print "os.path.exists(path1):", os.path.exists(path1)

print os.listdir(path1)