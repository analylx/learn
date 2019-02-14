from multiprocessing import Pool

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
	with Pool(5) as p:
		print(sum(p.map(isPrime,range(100000))))