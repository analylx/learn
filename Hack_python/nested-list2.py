"""
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
"""
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))