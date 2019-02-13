n = int(input())
array = input().split()
x= list(map(int,array))
x.reverse()
for y in x:
    print(y,end=" ")