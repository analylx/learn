n = int(input())
marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
qname = input()
print('{0:.2f}'.format(sum(marks[qname][:])/len(marks[qname])))
