import sys

def Main():
	x = 3.3
	y = 2.2
	a = x ** y
	print(a)
	b = x // y
	print(b)
	c = x / y
	print('this is c=' + str(c))
	print('a' and 'b')
	print('' and 'b')
	print("在 Python 中， and 和 or 所执行的逻辑运算并不返回布尔值 ，而是它们实际进比较值中的一个")
	# 使用dict
	num = {
		1: 'one',
		2: 'two',
		3: 'three'
	}
	try:
		print(num[x])
	except KeyError:
		print('nothing!')
	#下面这句列表内涵太复杂了，容易出错
	s = [(x,y,x*y) for x in range(1,10) for y in range(1,10) if x>=y]
	print (s)
	
	for I in [1, 2, 3, 4, 5]:
		print(I)

	try:
		f = open('p21.py')
		s = f.readline()
		print(s)
	# 这里需要改成python3的异常处理模式
	except IOError as e:
		print("open exception: %s: %s\n" % (e.errno, e.strerror))
	# except IOError,(errno,strerror):
	# print "I/O error(%s):%s" %(errno,strerror)
	except ValueError:
		print("Could not convert data to an integer")
	except:
		print("Unexpected error:", sys.exc_info()[0])
	#raise
	finally:
		f.close()

if __name__ == "__main__":
	Main()