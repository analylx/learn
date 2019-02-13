#coding=utf-8
#输入一个整数，输出一个这个长度的随机整数列表，随机值是1~10倍的整数
import random

def randomList(numbers):
	a=[]
	for i in range(numbers):
		a.append(random.randint(1,numbers*10))
	return a

#list1=randomList(100)
#print (list1)