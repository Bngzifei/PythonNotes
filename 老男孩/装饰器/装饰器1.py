"""
装饰即修饰,意思就是为其他函数添加新功能.
装饰器:本质就是一个函数,为其他函数添加附加功能.

原则:1.>不修改被修饰函数的源代码
	 2.>不修改被修饰函数的调用方式


装饰器的知识储备:

装饰器 = 高阶函数 + 函数嵌套 + 闭包
作用:修饰其他函数,添加附加功能

高阶函数的定义:
	1.> 函数接收的参数是一个函数名
	2.> 函数的返回值是一个函数名
	3.> 满足以上条件的任意一个,都可称之为高阶函数.



"""

"""参数是函数"""
# import time
#
# def foo():
# 	time.sleep(3)
# 	print('你好!')
#
#
# def test(func):  # test就是一个高阶函数
# 	# print(func)  # 输出内存地址
# 	start_time = time.time()
# 	func()  # 调用func()函数
# 	stop_time = time.time()
# 	print('运行时间:',stop_time - start_time)

# foo()  本该这样调用,下面的就是修改了foo的调用方式,没有保证函数的调用方式
# test(foo)  # 统计的是foo的运行时间,不是test的

"""返回值是函数"""

# def foo():
# 	print('from the foo')
#
#
# def test(func):
# 	return func


# res = test(foo)  # <function foo at 0x000001B9ACEEBAE8> 这样就拿到了函数的内存地址
# # print(res)
# res() # 拿到了函数 的内存地址之后,只要加()就把函数调用了,函数就会运行起来了

# foo = test(foo)
# foo()  # 原来就是这样调用的,调用方式没有改变
import time


def foo():
	time.sleep(3)
	print('来自foo')


# 不修改foo源代码
# 不修改foo调用方式

# 多运行了一次,不合格
# def timer(func):
# 	start_time = time.time()
# 	func()
# 	stop_time = time.time()
# 	print('函数运行时间:', stop_time - start_time)
# 	return func  # 有返回值才会可以callable -->可以被调用的
#
#
# foo = timer(foo)
# foo()


def timer(func):
	start_time = time.time()
	return func  # 有返回值才会可以callable -->可以被调用的
	stop_time = time.time()
	print('函数运行时间:', stop_time - start_time)


# 反正这种还是实现不了
foo = timer(foo)
foo()









"""需求,输出程序运行时间:"""
# import time
#
# def cal(l):
# 	start_time = time.time()
# 	res = 0
# 	for i in l:
# 		time.sleep(0.1)
# 		res += i
# 	end_time = time.time()
# 	run_time = end_time - start_time
# 	print('函数的运行时间:%s' % run_time)
# 	return res
#
#
# print(cal(range(100)))


# import time
#
#
# def timer(func):
# 	def wrapper(*args, **kwargs):
# 		start_time = time.time()
# 		res = func(*args, **kwargs)
# 		stop_time = time.time()
# 		print('函数运行时间是:%s' % (stop_time - start_time))
# 		return res
#
# 	return wrapper
#
#
# @timer
# def cal(l):
# 	res = 0
# 	for i in l:
# 		time.sleep(0.1)
# 		res += i
# 	return res
#
#
# res1 = cal(range(20))
# print(res1)
