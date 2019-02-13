#return (element for element in input_list if is_prime(element))
length = int(input())
for i in range(length):
    string = input()
    print(''.join(string[n] for n in range(len(string)) if n%2==0),end=' ')
    print(''.join(string[n] for n in range(len(string)) if n%2==1))