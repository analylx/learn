#-*- coding: utf-8 -*-

"""
Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.
map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

def sun_angle(time):
    hour, min = map(int, time.split(':'))
    if 6*60 <= 60*hour+min <= 18*60:
        return round((hour*60+min-360)/(12*60)*180, 2)
    return "I don't see the sun!"
"""


def sun_angle(time):
	time_split = time.split(":")
	#print(time_split)
	minutes = int(time_split[0])*60+int(time_split[1])
	#print(minutes)
	if 360>minutes or minutes>1080:
		return "I don't see the sun!"
	angle = (minutes-360)/(1080-360)*180
	return angle

if __name__ == '__main__':
	assert sun_angle("07:00") == 15
	assert sun_angle("12:15") == 93.75
	assert sun_angle("01:23") == "I don't see the sun!"

	print("The local tests are done.")