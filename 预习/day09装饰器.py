# coding:utf-8
"""
闭包:

理解:和变量名一样,函数名只是函数代码空间的引用,当函数名赋值给一个对象的时候,就是引用传递
"""

# def test1():
#     print("--- in test1 func----")
#
# # 调用函数
# test1()
#
# # 引用函数
# ret = test1
#
# print(id(ret))
# print(id(test1))
#
# #通过引用调用函数
# ret()

# def test(number):
# 	# 函数内部再定义一个函数,并且这个函数使用了外边函数的变量,那么,就把这个函数以及一些用到的变量
# # 称之为闭包
# 	def test_in(number_in):
# 		print('in test_in 函数,number_in is %d' % number_in)
# 		return number + number_in
# 	return test_in
#
#
# # 给test函数赋值,这个20就是给参数number
# res = test(20)
#
# # 注意这里的100其实给参数number_in,注意 res是test()函数的引用,这个函数return 一个test_in()函数,所以
# # 必须给res传一个参数
# print(res(100))
#
# # 注意这里的200其实给参数number_in
# print(res(200))
# -------------------------------------------------------------->
# def line_conf(a, b):
# 	def line(x):
# 		return a * x + b
#
# 	return line
#
#
# line1 = line_conf(1, 1)
# line2 = line_conf(4, 5)
#
# print(line1(5))
# print(line2(5))

"""
这个例子中,函数line与变量a,b构成闭包.在创建闭包的时候,我们通过line_conf的参数a,b 说明了这两个
变量的取值,这样,我们就确定了函数的最终形式(y = x + 1和 y = 4x + 5). 我们只需要变换参数a,b
就可以获得不同的线性表达函数.由此,我们可以看到,闭包也具有提高代码可复用性的作用.

如果没有闭包,我们需要每次创建线性函数的时候同时说明a,b,x.这样,我们就需要更多的参数传递,也减少了代码
的可移植性.

"""
# --------------------------修改外部函数中的变量------------------------------->
"""Py3中的方法:"""

# def counter(start=0):
# 	def inter():
# 		nonlocal start
# 		start += 1
# 		return start
#
# 	return inter
#
#
# c1 = counter(5)
# print(c1())  # 6
# print(c1())  # 7
# print(c1())  # 8
#
# c2 = counter(50)
# print(c2()) # 51
# print(c2()) # 52
# print(c2()) # 53

"""python2的方法:"""

# def counter(start=0):
# 	count = [start]
# 	print count
# 	def inter():
# 		print '-->',count[0]
# 		count[0] += 1
# 		return count[0]
#
# 	print inter
# 	return inter
#
#
# c1 = counter(5)
# print(c1())  # 6
# print(c1())  # 7
# print(c1())  # 8
#
# c2 = counter(100)
# print(c2())  # 101
# print(c2())  # 102
# print(c2())  # 103
"""
总结:
1.>函数名只是函数地址的引用,当函数名赋值给一个对象的时候,就是 地址的引用传递
2.>闭包就是一个嵌套定义的函数,在外层运行时才开始内层函数的定义,然后将内部函数
的引用传递给函数外的对象.
3.>内部函数 和  使用外部函数提供的变量   构成的整体  称之为闭包.
"""
# 0528  后门密码
# 2.30 - 5.50 7.30-9.50

"""装饰器"""
"""
理解:函数名仅仅是一个变量,只不过指向了定义的函数而已.所以才能通过 函数名() 调用
如果函数名 = xxx 被修改了,那么当在执行函数名() 时,调用的就不是之前的那个函数了.

可以明确一点:函数名就是一个对象,和普通对象一样,这个对象可以引用其他函数的代码.

开发中的要求:1.> 封闭:已经实现的功能代码块 2.>对扩展开放

规定了 已经实现的功能代码不能被修改,但是可以进行扩展
"""
# def w1(func):
# 	def inter():
# 		func()
# 	return inter

"""
1.>def w1(func): --> 将w1函数加载到内存
2.>@w1  原来的函数 = w1(原来的函数)

@函数名是Python的一种语法糖

记住:
@w1
def f1():

等价于 f1 = w1(f1)
"""


# ------------------多个装饰器装饰一个函数--------------------->
# 定义函数:完成包裹数据
def makeBold(fn):
	def wrapper():
		return '<b>' + fn() + '</b>'

	return wrapper


# 定义函数:完成包裹数据
def makeItalic(fn):
	def wrapper():
		return '<i>' + fn() + '</i>'

	return wrapper


# @makeBold  #  test1 = makeBold(test1)
# def test1():
# 	return 'hello word-1'
# @makeItalic
# def test2():
# 	return 'hello world-2'
#
#
# print(test1())
# print(test2())

# 谁在前面就是谁在外面
@makeBold
@makeItalic
def test3():
	return 'hello world-3'


# print(test3())

"""装饰器的应用场景:
1.>引入日志
2.>函数执行时间统计
3.>执行函数前预备处理
4.>执行函数后清理功能
5.>权限校验等场景
6.>缓存

"""

# --------------无参数的函数--------------->
# from time import ctime, sleep
#
#
# def timefun(func):
# 	def wrapper():
# 		print('%s called at %s' % (func.__name__, ctime()))
# 		func()
# 		print(func)  # <function foo at 0x000001FC95F1CD90>
#
# 	return wrapper
#
#
# @timefun
# def foo():
# 	print('I am foo')

# foo()
# sleep(2)
# foo()
"""
上面代码可以理解为:
foo = timefun(foo)
# foo首先作为参数赋值给func后,foo接收指向timefun返回的wrapper

foo()
调用foo() 等价于调用 wrapper() 因为timefun返回的wrapper函数地址值
内部函数wrapper被引用,所以外部函数的func变量(自由变量)并没有释放
func里面保存的是原来foo函数的对象
"""
# --------------------被修饰的函数有参数--------------------->

from time import ctime, sleep


def timefun(func):
	def wrapper(a, b):
		print('%s called at %s' % (func.__name__, ctime()))
		print(a, b)
		func(a, b)

	# print(func)  # <function foo at 0x000001FC95F1CD90>

	return wrapper


@timefun  # 它里面的func就是 这里的foo func里面存的一定是foo的函数地址
def foo(a, b):
	print(a + b)


# foo(3,5)
# sleep(2)
# foo(2,4)

# ---------------------------被修饰的函数有不定长参数-------------------->
from time import ctime, sleep


def timefun(func):
	def wrapper(*args, **kwargs):
		print('%s called at %s' % (func.__name__, ctime()))
		print(args, kwargs)  # 调用传进来的参数
		func(*args, **kwargs)

	# print(func)  # <function foo at 0x000001FC95F1CD90>

	return wrapper


@timefun  # 它里面的func就是 这里的foo func里面存的一定是foo的函数地址
def foo(a, b, **kwargs):
	print('--->', kwargs)
	print(a + b)


# foo(3, 5, c=100)  # 记住:执行顺序是:先执行 @timefun部分,完了才会去执行foo()自己内部的功能
# sleep(2)
# foo(2, 4, d=500)

# -------------------装饰器中的return---------------------------------------->
from time import ctime, sleep


def timefun(func):
	def wrapper():
		print('%s called at %s' % (func.__name__, ctime()))
		return func()

	return wrapper


@timefun  # 它里面的func就是 这里的foo func里面存的一定是foo的函数地址
def foo():
	print('I am foo')


@timefun
def getInfo():
	# res = print('--------你大爷的,这是个啥?----------')
	return '--------你大爷的,这是个啥?----------'


# foo()
# sleep(2)
# foo()
# print(getInfo())
# ---------------------------装饰器带参数,在原有装饰器的基础上,设置外部变量----------------->

from time import ctime, sleep

def timefun_arg(pre='hello'):
	def timefun(func):
		def wrapper():
			print('%s called at %s %s' % (func.__name__, ctime(),pre))
			return func()

		return wrapper
	return timefun


@timefun_arg('python')
def foo():
	print('I am foo')

@timefun_arg('itcast')
def too():
	print('I am too')


# foo()
# sleep(2)
# foo()
#
# too()
# sleep(4)
# too()
"""
可以理解为:
	foo() = timefun_arg('python')(foo)()    timefun_arg('python') --> timefun
	所以就是foo() = timefun(foo) ()
	
"""

# -----------------------类的装饰器---------------------------->
"""
装饰器函数其实就是这样一个接口约束,它必须接受一个callable<可以被调用的>对象作为参数,
然后返回一个callable对象.
在Python中一般callable对象都是函数.但是,也有例外.只要某个对象重写了__call__()方法,
那么,这个对象就是可以callable的.

"""
# class Test:
# 	def __call__(self, *args, **kwargs):
# 		print('call me!')

# t = Test()
# # 调用
# t()

# -----------类装饰器 demo--------------------->

class Test:
	def __init__(self,func):
		print('---初始化---')
		print('func name is %s' % func.__name__)
		self.__func = func

	def __call__(self, *args, **kwargs):
		print('---装饰器中的功能---')
		self.__func()  # 调用

@Test
def test():
	print('----test----')

test()

"""总结:
1.>装饰器函数只有一个参数-->就是被装饰的函数
2.>装饰器能够将一个函数的功能在 不修改代码的情况下进行扩展
3.>在函数定义的上方 写上 @装饰器函数名 就可以直接使用装饰器 对 这个函数进行装饰.



函数概念:

1.> 函数名是一个引用函数 代码空间的对象,这个对象在被赋值的时候,也可以引用其他空间

2.>闭包的特点:
	通过在函数内部嵌套重新定义了 一个函数,并且该函数还可以直接使用外部函数提供食物变量

3.>装饰器在我们需要一个函数功能进行扩展而又不想去修改代码的时候使用.
"""
















































