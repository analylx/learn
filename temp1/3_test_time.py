from time import time

class Timer(object):
	def __enter__(self):
		self.start=time()
		return self
	def __exit__(self,*args):
		self.end=time()
		self.seconds=self.end - self.start

def isPrime(n):
	if n == 2:
		print ("2 is prime.")
		return True
	for i in range(2,int(n**0.5)+2):
		if n%i == 0:
			return False
	#print (n," is prime.")
	return True
#整个程序的重点是这个with的用法
with Timer() as t:
	for i in range(2,1000000):
		isPrime(i)
		
print(t.seconds)
