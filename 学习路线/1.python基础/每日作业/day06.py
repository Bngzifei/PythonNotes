# def func1():  # 形参,位置参数
# 	i = 1
# 	sum = 0
# 	while i <= 100:
# 		sum += i
# 		i += 1
# 	return sum
#
#
# def func2(n):  # 实参,普通参数
# 	i = n
# 	sum = 0
# 	while i <= 100:
# 		sum += i
# 		i += 1
# 	return sum
#
#
# def func3(n=1, m=100):  # 形参,默认参数
# 	i = n
# 	sum = 0
# 	while i <= m:
# 		sum += i
# 		i += 1
# 	return sum
#
#
# print(func1())  # 5050
# print(func2(3))  # 5047
# print(func3())  # 5050

"""
分别定义加减乘除四个函数，然后实现多个数之间的累加累减累除累乘操作，如[1,2,3,4,5]，累加即是1+2+3+4+5，注意当使用除法时，应判断被除数不能为0


"""

# def add(n, m, *args):
# 	result = n + m
# 	if args:
# 		for i in args:
# 			result += i
# 	return print(result)
#
#
# # add(3, 5, 8, 1)
#
#
# def subtraction(n, m, *args):
# 	result = n - m
# 	if args:
# 		for i in args:
# 			result -= i
# 	return print(result)
#
#
# # subtraction(3,5,3,2)
#
# # for i in range(3):
# # 	i += 1
# # 	print(i)
#
# def multiplication(n, m, *args):
# 	result = n * m
# 	if args:
# 		for i in args:
# 			result = result * i
# 	return print(result)
#
#
# multiplication(2, 5)
# # print(multiplication(2, 5))
# # print(type(print(multiplication(2, 5))))
#
#
# def division(a, b, *args):
# 	res = a / b
# 	if b == 0:
# 		print('除数不能为0')
# 		res = a
# 	if args:
# 		for i in args:
# 			if i == 0:
# 				continue  # 是0就结束循环,跳过
# 			res = res / i
#
# 	return print(res)


# division(3, 3, 21, 8, 0)

"""
定义函数findall，实现对字符串find方法的进一步封装，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，需要找出里面所有的"hello"的位置，最后将返回一个元组(0,10,21,29)，即将h的下标全部返回出来，而find方法只能返回第一个

"""


# def findall(str1, str2):
# 	a = []
# 	i = 0
# 	while i < len(str1):
# 		if str1[i] == str2[0]:
# 			a.append(i)
# 		i += 1
#
# 	return print(tuple(a))


def findall(str1, str2):
	a = []
	while True:
		index = str1.find(str2)
		cishu = str1.count(str2)
		if index != -1:  # 可以找到
			a.append(index)
			# if index != 0:  # 不是第一个的情况

			for i in range(cishu):
				index = index + len(str2)
				a.append(index)
			print(a)
			break
			# else:
			# 	for i in range(cishu):
			# 		index = index + len(str2)
			# 		a.append(index)






			# index = str1.find(str2)
			# a.append(index)
			# index = str1.find(str2, len(str2))
			# a.append(index)
			# index = str1.find(str2, index + len(str2))
			# a.append(index)
			# index = str1.find(str2, index + len(str2))
			# a.append(index)
			# print(a)
			# break
		else:
			print('没有匹配的字符')
			break

findall('helloworldhellowpythonhelloc++hellowjavaghghgh', 'hellowo')
#
# str = 'helloworldhellowpythonhelloc++hellowjavaghghgh'
# str1 = 'hello'
# print(str.count(str1))
