import random

print ("Please input a init price!")
price1 = int(input())
days = int(input("Please input the days:"))
#sum_money = int(input("Please input the sum for init:"))
units = 1000
sum_money = price1*units
pool = 0


#for i in range(1,101):
#	print (random.randint(0,100)/1000)

#function to generate a 
def rand_by_day():
	bounce = random.uniform(0.9,1.101)
	return bounce

def calc(price1,sum1):
	price2 = price1*rand_by_day()
	st = price2*units
	pool =abs(st-sum1)
	if rand_by_day()>1:
		sum2 = st-pool
	else:
		sum2 = st
	return price2,sum2
	
for i in range(1,20):
	print(calc(price1,sum_money))