for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as err:
        print("Error Code:", err)
"""
Sample Input

3
1 0
2 $
3 1
"""

