for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))


"""
for _ in range(int(input())):
    n, seta = input(), set(input().split())
    m, setb = input(), set(input().split())
    print(all([i in setb for i in seta])) 
"""