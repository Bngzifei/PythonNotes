"""
除了用户定义的函数,调用运算符(即())还可以应用到其他对象上.

如果判断对象能够调用,可以使用内置的callable()函数

Python数据模型文档列出了7种可调用对象.

	1.>用户定义的函数

		使用def语句或lambda表达式创建

	2.>内置函数

		使用C语言(CPython)实现的函数,如len,或time.strftime.

	3.>内置方法

		使用C语言实现的方法,比如dict.get

	4.>方法

		在类的定义体中定义的函数

	5.>类

		调用类时会运行类的__new__方法创建一个实例,然后运行__init__方法,
		初始化实例,最后把实例返回给调用方.因为Python没有new运算符,
		所以调用类相当于调用函数.(通常,调用类会创建那个类的实例,不过覆盖
		__new__方法的话,也可能出现其他行为.)
	
	6.>类的实例

		如果类定义了__call__方法,那么它的实例可以作为函数调用.

	7.>生成器函数

		使用yield关键字的函数或方法.调用生成器函数返回的是生成器对象.

生成器函数在很多方面与其他可调用对象不同.生成器函数还可以作为协程.

	
	Python中有各种各样可调用的类型,因此判断对象能否调用,最安全的方法是使用内置的
	callable()函数.

"""


"""
用户定义的可调用类型:
	
	不仅Python函数是真正的对象,任何Python对象都可以表现得像函数.为此,
	只需实现实例方法__call__

"""

import random

class BingoCage:

	def __init__(self,items):
		self._items = list(items)
		random.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError("pick from empty BingoCage")

	def __call__(self):  # bingo.pick()的快捷方式是bingo()
		return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())  # 1
print(bingo())
print(callable(bingo))  # True


"""
实现__call__方法的类时创建函数类对象的简便方式,此时必须在内部维护一个状态,让它在
调用之间可用.装饰器就是这样.装饰器必须是函数,而且有时要在多次调用之间"记住"某些事
[例如备忘memoization],即缓存消耗大的计算结果.供后面使用.

创建保有内部状态的函数,还有一种截然不同的方式-----使用闭包.


下面讨论把函数视作对象处理的另一方面:运行时内省(反射,自我检查的意思)


"""