import coverage
from random import randint

cov = coverage.Coverage()
cov.start()
def isPrime(n):
	for i in range(2,int(n**0.5)+2):
		if n%i ==0:
			return "No"
		else:
			return "Yes"
		
n = randint(3,20000)
print (n,':',isPrime(n))
cov.stop()
cov.save()
cov.html_report()