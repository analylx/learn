def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    result = average(arr)
    print(result)