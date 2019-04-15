k = int(input())
lis = list(map(int, input().split(' ')))
set_ = set(lis)
for i in set_:
    lis.remove(i)
    if i not in lis:
        print(i)
        break