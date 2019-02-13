def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
        如果把全1的那行注释掉，那么if n <= len(array-1):就不会报错，应该是要报错：list和int之间不能用-号操作符。why？
    """
    if n <= len(array)-1:
        return  array[n]**n  
    return -1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    assert index_power([1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ], 8) == 1, "All 1"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
