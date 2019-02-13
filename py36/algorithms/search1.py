#coding=utf-8
import binary_search
import random_list
import selection_sort

list1 = random_list.randomList(10)
#print (list1)
print (binary_search.binary_search(list1,25))#找到的时候的返回值什么意思？
print(selection_sort.selectionSort(list1))#输出结果没有按照需求排序，有问题