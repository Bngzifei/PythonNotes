"""加上返回值:"""
# import time
# # 装饰器框架
# def timmer(func):  # func = test
# 	def wrapper():
# 		start_time = time.time()
# 		res = func()  # 就是在运行test()
# 		stop_time = time.time()
# 		print('run time', stop_time - start_time)
# 		return res
# 	return wrapper
#
#
# @timmer  # 完成的操作是: test = timmer(test)
# def test():
# 	time.sleep(3)
# 	print('test函数运行完毕')
# 	return '这是test的返回值'
#
# res = test()  # 就是在运行wrapper
# print(res)  # None


"""加上参数:"""

import time


# 装饰器框架
def timmer(func):  # func = test
	def wrapper(*args, **kwargs):  # 传参数的时候参数必须加*
		start_time = time.time()
		res = func(*args, **kwargs)  # 就是在运行test()  # 这样传参数的时候参数必须加*,但是如果需要直接使用参数,比如打印,就需要去掉*了.
		stop_time = time.time()
		print('run time', stop_time - start_time)
		return res

	return wrapper


@timmer  # 完成的操作是: test = timmer(test)
def test(name, age):
	time.sleep(3)
	print('test函数运行完毕,名字是%s,年龄是%d' % (name, age))
	return '这是test的返回值'


test('123', 12)
#
#
# @timmer  # test1 = timmer(test1)
# def test1(name, age, gender):
# 	time.sleep(3)
# 	print('test函数运行完毕,名字是%s,年龄是%d,性别%s' % (name, age, gender))
# 	return '这是test的返回值'


# missing 2 required positional arguments: 'name' and 'age' --> 少了两个位置参数
# res = test('林海峰',age = 26)  # 就是在运行wrapper
# print(res)  # None


# test1('alex',28,'male')
"""参数传递的问题:"""

# def test2(name, age, gender):  # test2(*('alex',18,'male','x','y'),**{})
# 	# name, age, gender = ('alex',18,'male','x','y')
# 	print(name)
# 	print(age)
# 	print(gender)
#
#
# def test1(*args, **kwargs):
# 	test2(*args, **kwargs)  # args = ('alex',18,'male','x','y') 元组


# test2(1, 2, 3, 4, age=56)
# test2(*(1, 2, 3, 4), **{'name': 'alex'})
# test3('alex',18,gender='male')

# test1('alex',18,'male','x','y')


"""解包:解压序列"""

l = [1, 2, 3, 5, 't', 5, 6, 7, 8, 82]

# 取出第一个和最后一个
# a, *d, c = l
# print(a)
# print(d)
# print(c)

# 取出第一个和最后一个,下划线也是可以表示一个变量的,常用来表示这个变量后续不会使用,但是只在这里使用.
# 例如:下面的例子中,_在后续不会使用,就是想让func()函数执行3次,没什么意义,不要纠结.
# for _ in range(3):
# 	func()

# a, *_, b = l
# print(a)  # 1
# print(_)  # [2, 3, 5, 't', 5, 6, 7, 8]
# print(b)  # 82

# 取第一个和第二个,倒数第一个和倒数第二个
# a, b, *_, c, d = l
# print(a)
# print(b)
# print(c)
# print(d)

# 使用索引对比:
# a, b = l[0],l[-1]
# print(a)
# print(b)

# 交换 a,b 的值  比如:a = 1,b = 2
a = 1
b = 2
a, b = b, a
print(a)
print(b)
