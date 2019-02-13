#-*- coding: utf-8 -*-
from typing import List, Any

"""
#如果列表里面的元素都是相同的，那么返回true
#切片返回的是原来的列表的一个相同类型的副本，a[:]表示所有的元素
#elements[1:]从第二个元素开始，到最后一个元素为止（包括最后一个）
elements[:-1]从第一个元素开始（默认第一个是0），到最后一个（-1）为止，但是不包括最后一个
#目的是通过错位比较相同的元素
def all_the_same(elements):
   return elements[1:] == elements[:-1]
"""
def all_the_same(elements: List[Any]) -> bool:
	if len(elements) <= 1:
		return True
	for num in range(len(elements)):
	    if elements[num] != elements[num-1]:
		    return False
	return True


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")