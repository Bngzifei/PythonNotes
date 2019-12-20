"""
对象的创建过程:new创建 返回
模拟实例对象的创建过程.

为啥是静态方法?

先有new后来init.因为init是需要实例对象来调用的,需要一个实例对象和self形参.所以需要new首先来创建一个实例对象.

"""


class Dog:
	pass


dog1 = Dog()

"""
类名()内部隐藏了两个魔法方法的自动调用

1.__new__:创建并返回一个新的实例对象.魔法方法,自动调用,自动传参(Python解释器自己会)
2.__init__:初始化操作,定义属性,先new后init,new后才会有实例对象,init需要使用实例对象(self形参位置需要传递一个实参过来)
"""


# print(dog1)


def dog_instance():
	"""模拟实例对象创建过程"""

	# 1.调用new方法 创建 返回
	# Dog.__new__()
	instance = object.__new__(Dog)
	# new(cls)cls:形参,new方法调用的时候需要一个实参.虽然new是一个静态方法,不会自动传参和自动调用.但是Python解释器调用这个方法的时候在内部帮我们传递了实参给形参cls.(谁调用,谁传递参数.)
	# print(instance)
	# 2.初始化,定义属性
	instance.__init__()
	# 3.把实例对象返回
	return instance


# Dog_instance()  # <__main__.Dog object at 0x000001879F5AB710>

dog2 = dog_instance()
print(dog2)  # <__main__.Dog object at 0x000001FF98428710>
