"""
假设在开发一个调试Web应用的工具,我们想生成HTML,显示不同类型的Python对象.

"""

# import html

# def htmlize(obj):
# 	content = html.escape(repr(obj))
# 	return "<pre>{}</pre>".format(content)



"""
因为Python不支持重载方法或函数,所以我们不能使用不同的签名定义htmlize的变体,
也无法使用不同的处理方式处理不同的数据类型.在Python中,一种常见的做法是把htmlize
变成一个分派函数,使用一串if/elif/elif,调用专门的函数,如htmlize_str,htmlize_int,
等等.这样不便于模块的用户扩展,还显得笨拙:时间一长,分派函数htmlize会变得很大,而且它与
各个专门函数之间的耦合也很紧密.



Python3.4新增的functools.singledispatch装饰器可以把整体方案拆分成多个模块,甚至可以为你
无法修改的类提供专门的函数.使用@singledispatch装饰的普通函数会变成泛函数:根据第一个参数的
类型,以不同方式执行相同操作的一组函数.

singledispatch创建一个自定义的htmlize.register装饰器,把多个函数绑在一起组成一个泛函数.
"""

from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
	content = html.escape(text).replace("\n","<br>\n")
	return "<p>{0}</p>".format(content)


@htmlize.register(str)
def _(text):
	content = html.escape(text).replace("\n","<br>\n")
	return "<p>{0}</p>".format(content)

@htmlize.register(numbers.Integral)
def _(n):
	return "<pre>{0} (0x{0:x})</pre>".format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
	inner = "</li>\n<li>".join(htmlize(item) for item in seq)
	return "<ul>\n<li>" + inner + "</li>\n</ul>"




"""
只要可能,注册的专门函数应该处理抽象基类(如numbers.Integral和abc.MutableSequence),不要处理具体实现(如int何list)
这样,代码支持的兼容类型更广泛.例如Python扩展可以子类化numbers.Integral,
使用固定的位数实现int类型.

使用抽象基类检查类型,可以让代码支持这些抽象基类现有和未来的具体子类或虚拟子类.抽象基类的作用和虚拟子类的概念稍后讨论.


singledispatch不是机制的一个显著特征是,你可以在系统的任何地方和任何模块中注册专门函数.如果后来在新的模块中定义了新
的类型,可以轻松地添加一个新的专门的函数来处理那个类型.此外,你还可以为不是自己编写的或者不能修改的类添加自定义函数.

@singledispatch不是为了把Java的那种方法重载带入Python.在同一个类中为同一个方法定义多个重载变体,比在一个函数中使用一长串if/elif/elif/elif
块要更好.但是这两张方案都有缺陷,因为它们让代码单元(类或函数)承担的职责太多.@singledispatch的优点是支持模块化扩展:各个模块
可以为它支持的各个类型注册一个专门函数.


装饰器是函数,因此可以组合起来使用(即,可以在已经被装饰的函数上应用装饰器.)


叠放装饰器

参数化装饰器

解析源码中的装饰器时,Python把被装饰的函数作为第一个参数传给装饰器函数.那怎么让装饰器接受其他参数呢?答案是:创建一个装饰器工厂函数,
把参数传给它,返回一个装饰器,然后再把它应用到要装饰的函数上.


"""

registry = []

def register(func):
	print("running register(%s)"%func)
	registry.append(func)
	return func

@register
def f1():
	print("running f1()")

	

print("running main()")
print("registry ->",registry)
f1()


"""
一个参数化的注册装饰器

为了便于启用或禁用register执行的函数注册功能,我们为它提供一个可选的active参数.
设为False时,不注册被装饰的函数.实现方式如下,从概念上看,这个新的register函数不是装饰器,
而是装饰器工厂函数.调用它会返回真正的装饰器,这才是应用到目标函数上的装饰器.

为了接受参数,新的register装饰器必须作为函数调用

"""


# registry 现在是一个set对象,这样添加和删除速度更快
registry = set()

def register(active=True):
	def decorate(func):
		print("running register(active=%s)->decorate(%s)"%(active,func))

		if active:
			registry.add(func)
		else:
			registry.discard(func)
		return func
	return decorate


@register(active=False)
def f1():
	print("running f1()")


@register
def f2():
	print("running f2()")


def f3():
	print("running f3()")
	

















