"""
需求:age = 0, 有人修改p.age=999
设置成公共属性:容易被其他人修改,自己还不知道已经修改了
设置成私有属性,外部使用不方便了.需要加设置属性和获取属性的方法

property:把以上两点合二为一了
既简单,又保证数据的正确性.


"""


class Person:
	def __init__(self, age):
		"""_age是被保护的属性/方法,代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入"""
		self._age = age

	@property
	def age(self):
		"""将装饰的方法 当成获取属性的方式   执行当前这个方法"""
		return self._age

	@age.setter  # 设置属性值 将方法和属性必须修改成一样的名字
	def age(self, age):
		"""如果需要让用户  对象.属性 的方式修改property装饰的属性,  将当前方法改为属性名
		并且还需要使用 @属性名.setter对当前方法进行装饰"""
		if age > 255 or age < 0:
			print('哥们,输入的年龄暂时有点超前了')
		else:
			self._age = age

	@age.deleter
	def age(self):
		"""如果需要让用户  对象.属性 的方式删除property装饰的属性,  将当前方法改为属性名
				并且还需要使用 @属性名.deleter对当前方法进行装饰"""
		print('正在删除...')
		del self._age


person = Person(18)
# 如果一个方法被property锁装饰,就可以直接使用函数名获取这个属性方法的功能
print(person.age)
person.age = 89
print(person.age)
# 就是把一个方法当做属性去使用
# del person.age
person1 = Person(20)
# 包装实例属性,各自独立
print(person1.age)
print(person.age)
"""
property:将方法包装成属性
	1.装饰器方式
	@property:将方法装饰为一个对象的实例属性
	@属性.setter:将方法装饰为一个对象的实例属性  进行设置/修改
	@属性.deleter:将方法装饰为一个对象的实例属性  进行删除
	以上这三种 只有新式类可以
	经典类只有@property

	三个方法必须同名  + 三个装饰器
	2.类属性的方式:
	# 包装成的属性 = property(获取操作,设置操作,删除操作,'属性的描述文档')



"""
