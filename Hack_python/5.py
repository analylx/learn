N = int(input().strip())

while N not in range(1, 20):
    print("please input an integer in range 1-20")
    N = int(input())

for x in range(0,N):
    print(x*x)