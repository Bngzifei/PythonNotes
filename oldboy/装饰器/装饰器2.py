"""
函数嵌套:


"""

"""这种不是函数嵌套:只是一个函数中调用了另外一个函数而已"""
# def bar():
# 	print('from bar')
# def foo():
# 	print('from foo')
# 	bar()

"""函数嵌套:函数定义中又定义了函数"""

# def foo():
# 	print('from foo')
# 	def test():
# 		pass


# 一层就是一个包裹  wrap:包裹,包起来  wrapper:包裹,书皮

"""
闭包:关闭起来的包,把一些东西封装起来
闭:就是封装的意思,封装变量,变量包括一般意义上的变量和函数<函数也是一个变量>
就是将作用域的概念换到了闭包,范围的理解.就是换了一种叫法.


"""
# def father(auth_type):
# 	# print('from father %s' % name)
#
# 	def son():  # 函数名就和变量一样
# 		# name = 'wupeiqi'
# 		# print('我的爸爸是%s' % name)  # name先去自己的son()函数内部找,如果没有,就回去son外部去找
# 		def grandson():
# 			# name = '就是自己'
# 			print('我的爷爷是:%s'% auth_type)  # 往上一层找
# 		grandson()
# 	# print(locals())  # 打印当前层的局部变量 有一个name,还有一个son函数也是局部变量.  {'son': <function father.<locals>.son at 0x0000024C5C59BA60>, 'name': '林海峰'}
# 	son()
#
# # 给最外层定义一个变量,最里面的也会能找到
# father('林海峰')
# son不能在函数father外部调用,因为是father的局部变量


"""架子:"""
import time


# 装饰器框架
def timmer(func):  # func = test
	def wrapper():
		# print(func)
		start_time = time.time()
		func()  # 就是在运行test()
		stop_time = time.time()
		print('run time', stop_time - start_time)

	return wrapper


@timmer  # 完成的操作是: test = timmer(test)
def test():
	time.sleep(3)
	print('test函数运行完毕')


# res = timmer(test)  # 返回的是wrapper的地址
# res()  # 执行的就是wrapper()

# test = timmer(test)
# test()

"""语法糖:@"""

# @timmer  相当于  test = timmer(test)
