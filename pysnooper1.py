import pysnooper


def the_max1(a,b,c):
    the_max = a if a > b else b
    the_max = c if c > the_max else the_max
    print('The max is:', the_max)

@pysnooper.snoop("d:/logs/log001.log")
def the_max2(a,b,c):
    the_max = a > b and a or b
    the_max = c > the_max and c or the_max
    print('The max is:', the_max)

def the_max3(a,b,c):
    print('The max is:', (a if a > b else b) if (a if a > b else b) > c else c)

def the_max(x, y):
	return x if x > y else y

def the_max4(a,b,c):
    print('The max is:', the_max(the_max(a, b), c))

def the_max5(a,b,c):
    print('The max is:', max(a, b, c))

if __name__ == "__main__":
    the_max1(1,2,3)
    the_max2(1,2,3)
    the_max3(1,2,3)
    the_max4(1,2,3)
    the_max5(1,2,3)

"""
the_max = a > b and a or b的逻辑如下：
先判断a>b，结果是true的话，接下来计算true and a,没短路返回第二个，就是计算a or b, 短路返回a
先判断a>b，结果是false的话，接下来计算false and a,短路返回第一个也就是false，接下来计算false or b，没短路返回第二个也就是b
In [1]: a = 1
In [2]: b = 2
or的运算结果是如果第一个是true就返回第一个，否则返回第二个，即使两个都是false
In [3]: c = a or b
In [4]: c
Out[4]: 1
In [7]: e = b or a
In [8]: e
Out[8]: 2
and的运算结果是如果第一个是False就返回第一个，否则返回第二个
In [9]: w1 = False and 1
In [10]: w1
Out[10]: False
In [11]: w2 = True and 1
In [12]: w2
Out[12]: 1
In [13]: e1 = b and a
In [14]: e1
Out[14]: 1
In [15]: e2 = a and b
In [16]: e2
Out[16]: 2
因为b=true所以无法短路，要计算后面的部分，后面的部分是a or b 结果短路
In [1]: a =1
In [2]: b =2
In [3]: c =3
In [4]: max = b and a or b
In [5]: max
Out[5]: 1
"""