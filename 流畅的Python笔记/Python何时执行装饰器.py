"""
装饰器的一个关键特性是,它们在被装饰的函数定义之后立即执行.这通常是在
导入时(即Python加载模块时).

"""
# registration.py模块

# 1.registry保存被@register装饰的函数引用.
registry = []

def register(func):
	print("running register(%s)" % func)
	# 把func存入registry
	registry.append(func)
	# 返回func:必须返回函数;这里返回的函数与通过参数传入的一样.
	return func


@register
def f1():
	print("running f1()")


@register
def f2():
	print("running f2()")


def f3():
	print("running f3()")


def main():
	print("running main()")
	print("registry ->",registry)
	f1()
	f2()
	f3()

if __name__ == '__main__':
	# 只有把registration.py当作脚本运行时才调用main()
	main()


"""
输出:
running register(<function f1 at 0x01EDC2B8>)
running register(<function f2 at 0x01EDC348>)
running main()
registry -> [<function f1 at 0x01EDC2B8>, <function f2 at 0x01EDC348>]
running f1()
running f2()
running f3()



注意:register在模块中其他函数之前运行(两次).调用register时,传给它的参数是被装饰的
函数,例如<function f1 at 0x01EDC2B8>

加载模块后,registry中有两个被装饰函数的引用:f1和f2.这两个函数,以及f3,只有在main明确
调用它们时才执行.
如果导入registration.py模块(不作为脚本运行,而是import 方式),输出如下:



考虑到装饰器在真实代码中的常用方式,示例中有两个不寻常的地方:

	1.>装饰器函数与被装饰的函数在同一个模块中定义.实际情况是,装饰器通常在一个模块中定义,
	然后将其返回.

	2.>register装饰器返回的函数与通过参数传入的相同.实际上,大多数装饰器会在内部定义一个
	函数,然后将其返回


虽然示例中的register装饰器原封不动地返回被装饰的函数,但是这种技术并非没有用处.很多Python Web
框架使用这样的装饰器把函数添加到某种中央注册处.例如把URL模式映射到生成HTTP响应的函数上的注册处.
这种注册装饰器可能会也可能不会修改被装饰的函数.
"""