def fib(n: int = 'int para') -> 'return an int list':
    '''Doc for this function'''
    print('Arguments:', n)
    print("Annotations:", fib.__annotations__)
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


if __name__ == '__main__':
    print("first1:", fib.__doc__)
    fib(60000000)
    print("\nlast:", fib.__doc__)
