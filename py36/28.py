# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def test(arg):
    #z = 1
    print(locals())
    print('\n')


#函数test在它的局部名字空间中有两个变量:arg(它的值被传入函数)和z(它在函数内部)
#locals返回一个名字与值的字典，这个字典的键字是字符串形式的变量名
#字典的值是变量的实际值
if __name__ == '__main__':
    test(5)
    test('楚广明')
    print(globals())  #返回一个全局的字典，包括所有导入的变量`
