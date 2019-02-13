# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countrys= set()
for i in range(n):
    countrys.add(input())
print(len(set(countrys)))