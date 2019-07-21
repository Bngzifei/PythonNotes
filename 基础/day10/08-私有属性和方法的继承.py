"""
私有方法和属性不会被继承,但是可以由其他方式间接使用

这个下午继续看看:
"""


class Dog:
	def __init__(self):  # 严格意义上来说只是继承了方法.
		self.__type = '狗'

	def __eat(self):
		print(self.__type)

	def drink(self):
		self.__eat()


class XTQ(Dog):
	pass


xtq = XTQ()
xtq.__eat()  # 无法调用,直接报错. AttributeError: 'XTQ' object has no attribute '__eat'
xtq.drink()
