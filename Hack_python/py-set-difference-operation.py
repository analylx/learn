#print((lambda x: len(set(x[1]) - set(x[3])))([input().strip().split() for _ in range(4)]))
#_,a,_,b=[set(input().split()) for _ in '1234'];print(len(a-b))
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.difference(b)))


