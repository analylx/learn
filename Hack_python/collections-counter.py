import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCurst = int(input())

income = 0

for i in range(numCurst):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)


'''input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
