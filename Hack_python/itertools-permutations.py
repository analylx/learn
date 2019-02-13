from itertools import permutations
'''
Str, k = input().split()
temp1 = permutations(Str, int(k))
result = list(temp1)
result.sort()
for i in result:
    j = ''.join(i)
    print(j)
'''
s, n = input().split()
# the * is used to unpack list into individual elements
print(*[''.join(i) for i in permutations(sorted(s), int(n))], sep='\n')