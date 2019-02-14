from multiprocessing import Pool
from time import time

class Timer(object):
	def __enter__(self):
		self.start=time()
		return self
	def __exit__(self,*args):
		self.end=time()
		self.seconds=self.end - self.start

def isPrime(n):
	if n <2:
		return 0
	if n==2:
		return 1
	if not n&1:
		return 0
	for i in range(3,int(n**0.5)+1,2):
		if n%i==0:
			return 0
	return 1

if __name__ == '__main__':
	with Timer() as t:
		with Pool(8) as p:
			result= (sum(p.map(isPrime,range(10000000))))
			print (result)
	print(t.seconds)