"""
>>>sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

#难点是怎么保存排序前的正负号。先将元祖转换成字典，值就是绝对值，然后按照指排序后输出关键字
def checkio(numbers_array: tuple) -> list:
    dict1 = {}
    for num in numbers_array:
        dict1[num]=abs(num)
    #这里的x[1]就是取字典的值，x[0]就是取字典的关键字
    numbers_array = sorted(dict1.items(),key=lambda x:x[1])
    print(type(numbers_array[0]))
    return numbers_array
"""
def checkio(numbers_array):  
    numbers_array=sorted(numbers_array,key=lambda x:abs(x))  
    return numbers_array 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
