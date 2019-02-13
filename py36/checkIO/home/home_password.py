import re
"""
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.
Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.
需要一个密码强度正则表达式在用户注册时校验用户密码强度：密码至少8个字符，包括1个大写字母，1个小写字母和1个数字或特殊字符，例如#，?，!。
方案一
至少8-16个字符，至少1个大写字母，1个小写字母和1个数字，其他可以是任意字符：
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/
或者：
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,16}$
其中 [\s\S] 中的\s空白符，\S非空白符，所以[\s\S]是任意字符。也可以用 [\d\D]、[\w\W]来表示。
至少8个字符，至少1个大写字母，1个小写字母和1个数字,不能包含特殊字符（非数字字母）：
^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$
至少8个字符，至少1个字母，1个数字和1个特殊字符：
^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$
至少8个字符，至少1个大写字母，1个小写字母和1个数字：
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$
至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符：
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}
最少8个最多十个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符：
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,10}
方案二
^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$
这个正则表达式将强制执行这些规则：
至少1个大写字母English letter，(?=.*?[A-Z])
至少1个小写英文字母，(?=.*?[a-z])
至少1位数字，(?=.*?[0-9])
至少有1个特殊字符，(?=.*?[#?!@$%^&*-])
最小8个长度.{8,}
"""
def checkio(password):
	if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{3,64}$", password):
		return True
	return False

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio('pokl') == False, "0 example"
	assert checkio('A1213pokl') == False, "1st example"
	assert checkio('bAse730onE4') == True, "2nd example"
	assert checkio('asasasasasasasaas') == False, "3rd example"
	assert checkio('QWERTYqwerty') == False, "4th example"
	assert checkio('123456123456') == False, "5th example"
	assert checkio('QwErTy911poqqqq') == True, "6th example"
	assert checkio('QwErTy911poqqqqQwErTy911poqqqqQwErTy911poqqqqQwErTy911poqqqq1234') == True, "7th example"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")