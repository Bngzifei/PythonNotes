import time

# def pass_argv(func):
# def get_time(func):  # 这里只能接收一个参数,即使写成了*args **kwargs的形式
# 	"""对函数运行时间进行统计"""
# 	print('in get_time')  # 灵魂代码  一旦装饰就执行
#
# 	def inner(*args, **kwargs):  # 传参数,打包  内部函数可以接收任意参数
# 		t1 = time.time()
# 		# 拆包参数  如果函数有返回值,暂时先保存,执行结束在返回
# 		# 这里的* 和** 是拆包的作用,将刚刚打包的参数进行解包
# 		res = func(*args, **kwargs) # 暂时先保存执行结果
# 		t2 = time.time()
# 		print('运行了%s s' % (t2 - t1))
# 		# 如果 这里是 func(*args, **kwargs) 那么就会把func又执行了一遍,多余.
# 		return res  # 返回执行结果
# 	return inner
#
#
# # return get_time
#
# # 先写函数
#
# @get_time  # 只要这样写,就把 装饰器执行了
# def func1(num,age = 18):
# 	for i in range(3):
# 		time.sleep(1)
# 		print('in func', num,age)
#
#
# @get_time  # 灵魂代码
# def func2(num,height = 180,**kwargs):
# 	time.sleep(2)
# 	print('in f2', num,height)
# 	print(kwargs)
# 	return 250
#
#
# func1(222)
#
# func2(999,minzgi = 333)
# 装饰器分为装饰器函数<基于闭包实现>,类装饰器<基于类实现>
# 装饰器函数的特点:有 且 只有一个函数 ,就是被装饰的函数的引用
# 不写return  和return None是一样的


"""
装饰器带参数  @装饰器(参数)
类装饰器
多个装饰器 装饰器



函数:函数代码空间的引用,可以传递,可以接收其他的引用

面向切面编程:AOP
意义:业务实现和其他细节隔开,扩展的就是细节.切面就是业务实现
其他细节就是新的功能
"""

# --------------------------装饰器带参数---------------------------->


def pass_args(age=98):  # 传普通位置参数
	print('开始装饰器的表演了...')

	def check(func):  # 传指定的被装饰的函数名
		def wrapper(*args):
			print('装饰一下')
			print('年龄是:', age)
			func()  # 调用被装饰的函数

		# print(wrapper)
		return wrapper

	# print(check)
	return check  # 每一层都要返回上一层的函数名


@pass_args()  # foo = pass_args(foo)  记得这里一定要加(),一定是 @pass_args() 这样,三层函数嵌套了.
def foo(age=99):
	print('这是foo函数,年龄是%s' % age)


foo(100)
