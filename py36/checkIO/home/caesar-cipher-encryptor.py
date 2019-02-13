#-*- coding: utf-8 -*-

"""
Input: A secret message as a string (lowercase letters only and white spaces)
Output: The same string, but encrypted
chr(65)='A'
ord('A')=65
''.join()将列表组合成字符串，没有分隔符的模式
#按照结果来分析，如果c不是字母的话比如空格，不该去执行转换。但是如果c是字母。就去执行转换。也就是说前面的join是对每个c都会去执行一次，后面的判断就是指出做不做转换。else就是什么都不做，但必须存在这个else
def to_encrypt(text, delta):
    return ''.join([chr((ord(c) - ord('a') + delta) % 26 + ord('a')) if c.isalpha() else c for c in text])
"""
#change函数的作用是吧每一个字符转换成加密后的字符
def change(items,delta):
	temp = ord(items) + delta
	while temp > 122:
		temp = temp - 26
	while temp < 97:
		temp = temp + 26
	return chr(temp)

def to_encrypt(words,delta):
	#list1= [chr(i) for i in range(97,123)]
	final= []
	for items in list(words):
        #空格不转换，其他的字符按照chahge规则转换
		if items == ' ':
			final.append(items) 
		else:
			final.append(change(items,delta))
	return "".join(final)

if __name__ == '__main__':
	assert to_encrypt("a b c", 3) == "d e f"
	assert to_encrypt("a b c", -3) == "x y z"
	assert to_encrypt("simple text", 16) == "iycfbu junj"
	assert to_encrypt("important text", 10) == "swzybdkxd dohd"
	assert to_encrypt("state secret", -13) == "fgngr frperg"
	print("The local tests are done.")