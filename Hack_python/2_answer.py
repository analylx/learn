n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# neat version
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
    n % 2 == 0 and (n in range(2, 6) or n > 20)
])

"""
n = int(input())
#the deal with error is fine.
while n not in range(1, 101):
    print("please input an integer in range 1-100")
    n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):
    print("not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
else:
    print("not Weird")
"""
