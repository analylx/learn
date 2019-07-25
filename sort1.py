import pysnooper

@pysnooper.snoop("d:/logs/log111.log")
def small_least(arry):
    small_least = arry[0]
    small_least_index = 0
    for i in range(1, len(arry)):
        if arry[i] < small_least:
            small_least = arry[i]
            small_least_index = i
    return small_least_index


def sort1(arry):
    new_arry = []
    for _ in range(len(arry)):
        small = small_least(arry)
        new_arry.append(arry.pop(small))
    return new_arry

#采用递归加分治
def sort2(arry):
    if len(arry) < 2:
        print("len of arry",len(arry))
        return arry
    else:
        pivot = arry[0]
        less = [i for i in arry[1:] if i <= pivot]
        print("less is:",less)
        greater = [i for i in arry[1:] if i > pivot]
        return sort2(less)+[pivot]+sort2(greater)


arry1 = [69, 25, 75, 8, 4, 7, 789, 852, 741, 2]

print("sort2:", sort2(arry1))
print("sort1:", sort1(arry1))

