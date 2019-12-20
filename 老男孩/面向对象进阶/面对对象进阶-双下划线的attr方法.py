print('面对对象进阶...')

"""
__setattr__:获取
__getatrr__:设置
__delattr__:删除


"""


class Foo:
	x = 1

	def __init__(self, y):
		self.y = y

	# 调用一个对象不存在的方法或者属性的时候才会触发执行
	def __getattr__(self, item):
		print('执行__getattr__')

	def __delattr__(self, item):
		print('执行__delattr__')
		# del self.item  # 这样操作就是无限递归了
		self.__dict__.pop(item)  # 应该直接在底层这么操作

	def __setattr__(self, key, value):
		# 这么直接赋值的方式就是无限递归了
		# self.key = value  本质就是将属性的key-value键值对 存到对象的__dict__字典中
		print('执行__setattr__')
		self.__dict__[key] = value  # 最底层的操作就是操作这个字典


# f1 = Foo(10)  # 设置属性就会触发__setattr__()方法
# print(f1.y)  # 10
# print(f1.__dict__)  # {'y': 10}
# f1.z = 222
# print(f1.__dict__)  # {'y': 10, 'z': 222}
# len(str)的本质: 就是去调用str的__len__()方法
# getattr(f1,'y')
# f1.sdfd  # 执行__getattr__


# del f1.y  # 执行__delattr__
# 调用类的x属性
# print(f1.x)
# 删除类的x属性也会触发__delattr__方法
# del f1.x  # 执行__delattr__

# __dict__: 一个对象的属性字典


# RecursionError: maximum recursion depth exceeded :递归溢出,超过了最大的递归层数

"""属性字典__dict__"""


class Foo:
	def __getattr__(self, item):
		print('x属性不存在')


# print(Foo.__dict__)  # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo' objects>,
print(dir(Foo))
f = Foo()
# print(f.__dict__) # {}

"""
只有在属性不存在时候才会触发 __getattr__()的运行,
默认是报错   AttributeError: 'Foo' object has no attribute 'x'
系统默认的就是报错  AttributeError
"""
f.x  # x属性不存在
# print(f.x)  # None  --> print(print):这样输出的就是None

# del f.x  # 删除的时候会触发 __delattr__

f.y = 10  # 设置的时候会触发__setattr__
