#-*- coding: utf-8 -*-
"""
Input: A list of integers.
Output: The list of integers.
先将数组转换成集合，这样可以过滤出唯一的元素。如果两者的长度相等，返回空数组。
再将这个数组中的数字和这个集合中的每个元素比较一遍，如果没有相同的话就删除。
"""

def checkio(lists1):
	sets1 = set(lists1)
	#为什么下面的打印会打印相同的两行？
	#print (sets1)
	#列表和集合长度相同说明没有重复的元素
	if len(lists1)==len(sets1):
		return []
	for item in sets1:
		#print (lists1.count(item))
		if lists1.count(item)==1:
			lists1.remove(item)
			#print (lists1)

	return lists1



if __name__ == '__main__':
	assert checkio([1,2,3,4,5,6]) == []
	assert checkio([1,2,3,4,5,6,6]) == [6,6]
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
	assert checkio([1, 2, 3, 4, 5]) == []
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
	print("The local tests are done.")