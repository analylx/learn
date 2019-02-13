a = int(input().strip())
b = int(input().strip())

try:
    print(a//b)
    print(a/b)
except (IOError,ZeroDivisionError) as e:
    print (e)
