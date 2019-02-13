
d = {} #dict
for _ in range(int(input())):
    name = input()
    score = float(input())
    # if the score has names associated, get the list, otherwise empty list
    score_names = d.get(score, [])
    # append to list and store list back in dict (just in case it's new)
    score_names.append(name) 
    d[score] = score_names

# get the second of the keys when sorted ascending, use it for the dict to get names, sort + unpack to print
print(*sorted(d[sorted(d.keys())[1]]), sep='\n')
