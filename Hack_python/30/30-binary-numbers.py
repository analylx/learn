#思路就是把二进制的字符串用0分割，结果就是连续的1，然后取最长的那个的长度就可以了。bin(10)=0b1010
n = int(input().strip())
print(max(len(length) for length in bin(n)[2:].split('0')))