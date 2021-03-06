"""
函数装饰器用于在源码中"标记"函数.以某种方式增强函数的行为.
这是一项强大的功能.但若想掌握,必须理解闭包.

nonlocal是新近出现的保留关键字.在Python3.0中引入.作为Python程序员,
如果严格遵守基于类的面向对象编程方式,即便不知道这个关键字也不会受到影响.然而,
如果你想自己实现函数装饰器,那就必须了解闭包的方方面,因此也就需要知道nonlocal.

除了在装饰器中有用处之外,闭包还是回调式异步编程和函数式编程风格的基础.


最简单的注册装饰器和较复杂的参数化装饰器.


装饰器基础知识:

	装饰器是可调用对象,其参数是另一个函数(被装饰的函数).装饰器可能会处理被装饰的函数,然后
	把它返回,或者将其替换成另一个函数或可调用对象.

"""

# 假如有个名为decorate的装饰器
@decorate
def target():
	pass

#上述代码的效果和下述写法一样:
def target():
	pass

target = decorate(target)

"""
两种写法的最终结果一样:上述两个代码片段执行完毕后得到的target不一定是原来的那个target函数,而是
decorate(target)返回的函数.

"""

# 装饰器通常把函数替换成另一个函数
def deco(func):
	def inner():
		print("running inner()")

	return inner

@deco
def target():
	print("running target()")


#>>> target 
# 审查对象,发现target现在是inner的引用
# <function deco.<locals>.inner at 0x10063b598>

"""
严格来说,装饰器只是语法糖.如前所示,装饰器可以想像常规的可调用对象那样调用,
其参数是另一个函数.有时,这样做更方便,尤其是做元编程(在运行时改变程序的的行为)时.

综上,装饰器的一大特性是,能把被装饰的函数替换成其他函数.第二个特性是,装饰器在加载
模块时立即执行.
"""
