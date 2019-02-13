a = int(input().strip())

while a not in range(1, 10**10):
    print("please input an integer in range 1-100")
    a = int(input())

b = int(input().strip())
while b not in range(1, 10**10):
    print("please input an integer in range 1-100")
    b = int(input())

print(a+b,a-b,a*b,sep='\n')