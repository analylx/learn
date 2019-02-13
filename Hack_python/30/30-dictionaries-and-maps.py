#!/bin/python3
n = int(input())
dict1={}
for i in range(n):
    name,num = input().split()
    dict1[name]=int(num)
while True:
    query = input()
    if query in dict1:
        print("{0}={1}".format(query,dict1[query]))
    else:
        print("Not found")
