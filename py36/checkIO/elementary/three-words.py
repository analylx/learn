def checkio(words):  
    i=0
    #split()里面默认的参数也就是分隔符是空格，返回一个列表
    for word in words.split():  
        if word.isalpha():  
            i+=1  
            if i==3:return True  
        else:i=0  #这里的作用是没达到3的时候清0
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
