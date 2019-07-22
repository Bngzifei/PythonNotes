"""
isinstance(obj,cls): obj是否是cls的一个实例,obj:对象,cls:类

issubclass(Bar, Foo):Bar是否是Foo的子类
"""

# class Foo:
# 	pass
#
#
# f = Foo()
# print(isinstance(f, Foo))  # True
#
#
# class Bar(Foo):
# 	pass
#
#
# b1 = Bar()
# print(isinstance(b1, Foo))  # True
# print(issubclass(Bar, Foo))  # True
# print(issubclass(Foo,Bar))  # False
# print(type(b1))  # <class '__main__.Bar'>

"""
__getattr__():不存在的属性访问,触发的是__get__attr()

"""

# class Foo:
# 	def __init__(self, x):
# 		self.x = x
#
# 	def __getattr__(self, item):
# 		print('执行的是getattr')
#
#
#
# f = Foo('你?')
# print(f.x)  # 你? 可以找到的属性,就是自己有的

# 不存在的属性访问,触发的是__get__attr()
# f.xxxxxxxxxx  # 执行的是getattr

"""
__getattribute__():有没有属性都会触发它
是__getattr__()的大哥,大哥不干了丢给小弟干
不存在就抛出异常,抛出异常后程序就奔溃了,当和__getattr__()一起出现的时候,就把异常丢给
getattr,程序就不会奔溃了.

一般没什么用.
"""


# class Foo:
# 	def __init__(self, x):
# 		self.x = x
#
# 	#
# 	# 	def __getattr__(self, item):  # 遇到raise AttributeError('抛出异常了')才可以执行
# 	# 		print('执行的是getattr')
# 	#
# 	def __getattribute__(self, item):
# 		print('执行的是getattribute')
#
# 	# raise AttributeError('抛出异常了')
#
#
# f = Foo('你?')
# f.x  # 执行的是getattribute

# print(f.x)
# 执行的是getattribute
# None

# f.xxxxxxxxxx

# raise AttributeError('抛出异常了')

# print('--------------------------')
# print('--------------------------')
# # class Foo:
# # 	pass
# # f1 = Foo()
# # f1.name
# raise AttributeError('自己找事')
# print('--------------------------')
# print('--------------------------')
# print('--------------------------')
