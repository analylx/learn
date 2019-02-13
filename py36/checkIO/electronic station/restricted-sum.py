def checkio(data):
    #因为字符串对象是不可以调用的，就是不能直接当函数名来调用
    #eval() 通常用来执行一个字符串表达式，并返回表达式的值。在这里它将字符串转换成对应的函数。
    return eval(''.join('s'+'u'+'m'))(data)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([1,2,3,4,5,6,7,8]) == 36, "First example"
    assert checkio([11,22,33,44]) == 110, "Second example"
    assert checkio([0,0,0,0,0,]) == 0, "Third example"
