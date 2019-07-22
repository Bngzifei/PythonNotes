"""

C++ 和Python 支持多继承,其他语言不支持

发现规律找规律记,记住区别.初始化只是一次.再次调用init()方法就是和普通的方法调用没区别了.

多态依赖继承.
鸭子类型不依赖继承.
Python中没有重载一说,即使同名函数,方法,出现2次后,第2次的慧覆盖掉第1次的.在一个类里面只能有一个,通过修改参数来进行需要的变化.


同名属性和同名方法只会继承某个父类的一个.继承链中挨的最近的那个.

"""


class Dog:
	def eat(self):
		print('肉')

	def drink(self):
		print('水')


class God:
	def fly(self):
		print('lll')

	def eat(self):
		print('丹')


# 格式:class 类名(父类1,父类2...)		派生类:延伸的类,就是一个新的类而已  也有的叫法是 class 派生类(父类1,父类2...)
class XTQ(Dog, God):
	# 如果想要控制,指定的就要重新写了.
	def eat(self):
		# super(Dog, self).eat()  # 调的是Dog后面那个,也就是God的属性了.多继承时,看着比较混乱,所以不要这么写

		God.eat(self)  # 多继承时,如果调用指定父类被重写的方法,尽量直接使用指定的父类方法名去调用


xtq = XTQ()
# xtq.fly()
# xtq.drink()
xtq.eat()  # 继承链:调用第一个的,有顺序的.

# print(XTQ.__mro__)  # 查看指定类的继承链  (<class '__main__.XTQ'>, <class '__main__.Dog'>, <class '__main__.God'>, <class 'object'>)  ,实际上注意:Dog和God是没有关系的是并列的

# print(Dog.__mro__)  # (<class '__main__.Dog'>, <class 'object'>)
# print(God.__mro__)  # (<class '__main__.God'>, <class 'object'>)
