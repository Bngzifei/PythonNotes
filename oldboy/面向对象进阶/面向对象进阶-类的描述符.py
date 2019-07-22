print('-------------------------')
"""
描述符:其本质是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()
这三个中的一个,这也被称为描述符协议.

__get__():调用一个属性的时候触发.
__set__():为一个属性赋值的时候触发
__delete__():使用del删除属性的时候触发

描述符的作用:其作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性,不能定义成
实例属性.<就是不能定义在init()方法中>

对象.属性就会触发

描述是描述别人的,描述自己就没意思了.
一个类的属性调用了另外一个类的实例对象

描述符分两种:
	1.>数据描述符:至少实现了__get_(),__set__()
	2.>非数据描述符:没有实现__set__()
注意事项:
	1.>描述符本身应该被定义为新式类,被代理的类也应该是新式类
	2.>必须把描述符定义成这个类的类属性,不能定义成实例属性
	3.>要严格遵循下列优先级,优先级从高到低分别是:
		1.类属性
		2.数据描述符
		3.实例属性
		4.非数据描述符
		5.找不到的属性触发__getattr__()

代理:就是本来属于A的事情现在全部交给了B去做.这样就称B是A的代理.
"""

# Python3中全部都是新式类
# class Foo:
# 	def __get__(self, instance, owner):
# 		print('get方法')
#
# 	def __set__(self, instance, value):
# 		print('set方法',instance,value)
# 		instance.__dict__['x'] = value  # b1.x = 1111, 1111是value
#
# 	def __delete__(self, instance):
# 		print('delete方法')
#

# class Bar:
# 	# 类属性就是一个描述符的对象
# 	x = Foo()  # 不惊讶,x的值其实是一个Foo()实例化的结果
#
# 	def __init__(self, n):
# 		self.x = n  # b1.x = 9
#
#
# # print(Bar.__dict__)
# b1 = Bar(9)  # set方法
# print(b1.__dict__)  # 没开x = Foo()这个描述符就是{'x': 9},开了就是{}为空
# # b1.x = 1111  # set方法 <__main__.Bar object at 0x0000022458657C18>这个是instance 1111这个是value
# # print(b1.__dict__)
# # 只要被代理的属性,统统归代理管,没有被代理的属性,和就不管代理了.
# b1.y = 2222
# print(b1.__dict__)

# b1.x  # get方法
# b1.x = 9  # set方法
# del b1.x  # delete方法

"""描述符的优先级: 表示查找的顺序"""


class Foo:
	def __get__(self, instance, owner):
		print('get方法')

	def __set__(self, instance, value):
		print('set方法', instance, value)

	def __delete__(self, instance):
		print('delete方法')


class Bar:
	x = Foo()

print(Bar.x)
# Bar.x = 1  # 类属性优先级更高
# print(Bar.__dict__)
# print(Bar.x)

b1 = Bar()  # b1是实例对象,实例对象才会触发描述符
# b1.x  # 触发的是描述符的get
# b1.x = 1


"""
总结:描述符是可以实现大部分Python类特性中的底层魔法.包括@classmethod,@staticmethod
@property 甚至是__slots__属性.

描述符是很多高级库和框架的重要工具之一,描述符通常是使用装饰器或者元类的大型框架中的
一个组件.
利用描述符原理完成一个自定制的@property实现延迟计算<本质就是把一个函数,利用装饰器原理做成
一个描述符:类的属性字典中函数名为key,value为描述符 类产生的对象>



Python是弱类型语言,即参数的赋值没有类型限制

"""