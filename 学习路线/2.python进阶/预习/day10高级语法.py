# ---------------------单独调用父类的方法--------------------------------->
"""
子类初始化的时候需要手动调用父类的初始化方法进行父类的属性的构造.
不然就不能使用提供的属性.

子类中调用父类的初始化方法,父类名.__init__(self)

多继承:一个子类同时继承自多个父类,又称菱形继承,钻石继承.
"""
# class Parent:
# 	def __init__(self,name):
# 		print('parent的init开始被调用')
# 		self.name = name
# 		print('parent的init结束被调用')
# class Son1(Parent):
# 	def __init__(self,name,age):
# 		print('Son1的init开始被调用')
# 		self.age = age
# 		Parent.__init__(self,name)
# 		print('Son1的init结束被调用')
# class Son2(Parent):
# 	def __init__(self,name,gender):
# 		print('Son2的init开始被调用')
# 		self.gender = gender
# 		Parent.__init__(self,name)
# 		print('Son2的init结束被调用')
# class Grandson(Son1,Son2):
# 	def __init__(self,name,age,gender):
# 		print('Grandson的init开始被调用')
# 		Son1.__init__(self,name,age)
# 		Son2.__init__(self,name,gender)
# 		print('Grandson的init结束被调用')
#
# g = Grandson('grandson',12,'男')
# print('姓名:',g.name)
# print('年龄:',g.age)
# print('性别:',g.gender)

# -------------------------MRO顺序------------------------------------>
"""
由于多继承的情况,parent类的属性被构造了两次,....
为了解决这个问题,Python 官方采用了一个算法将复杂结构上所有的类全部都映射到
一个线性顺序上,而根据这个顺序就能够保证所有的类都会被构造一次.这个顺序就是MRO
顺序.
查看MRO顺序:
类名.__mro__()
类名.mro()
"""

# ----------------多继承中super调用所有父类被重写的方法----------------------->
"""
super本质上就是使用MRO这个顺序去调用,当前类在MRO顺序中的下一个类
super.__init__()则调用了下一个类的初始化方法进行构造
"""

# class Parent:
# 	def __init__(self, name, *args, **kwargs):
# 		print('parent的init开始被调用')
# 		self.name = name
# 		print('parent的init结束被调用')
#
#
# class Son1(Parent):
# 	def __init__(self, name, age, *args, **kwargs):
# 		print('Son1的init开始被调用')
# 		self.age = age
# 		super(Son1, self).__init__(name, *args, **kwargs)
# 		print('Son1的init结束被调用')
#
#
# class Son2(Parent):
# 	def __init__(self, name, gender, *args, **kwargs):
# 		print('Son2的init开始被调用')
# 		self.gender = gender
# 		super(Son2, self).__init__(name, *args, **kwargs)
# 		print('Son2的init结束被调用')
#
#
# class Grandson(Son1, Son2):
# 	def __init__(self, name, age, gender):
# 		print('Grandson的init开始被调用')
# 		"""
# 		多继承时候,相对于使用类名.__init__方法,要把每个父类全部写一遍
# 		而super只用一句话,执行了全部父类的方法,这也是为何多继承需要全部传参的一个原因
#
# 		"""
# 		super(Grandson, self).__init__(name, age, gender)
# 		print('Grandson的init结束被调用')
#
#
# print(Grandson.__mro__)
#
# g = Grandson('grandson', 12, '男')
# print('姓名:', g.name)
# print('年龄:', g.age)
# print('性别:', g.gender)

# -----------------------单继承中的super---------------------------------->

# class Parent(object):
# 	def __init__(self, name):
# 		print('parent的init开始被调用')
# 		self.name = name
# 		print('parent的init结束被调用')
#
#
# class Son1(Parent):
# 	def __init__(self, name, age):
# 		print('Son1的init开始被调用')
# 		self.age = age
# 		super().__init__(name)  # 单继承不能提供全部参数
# 		print('Son1的init结束被调用')
#
#
# class Grandson(Son1):
# 	def __init__(self, name, age):
# 		print('Grandson的init开始被调用')
# 		super().__init__(name, age)  # 单继承不能提供全部参数
# 		print('Grandson的init结束被调用')
#
#
# gs = Grandson('grandson', 12)
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# # print('性别：', gs.gender)

"""
总结:
1.>MRO保证了多继承情况下,每个类只出现一次
2.>super().__init__相对于类名.__init__,在单继承上用法基本无差.
3.>但在多继承上有区别,super方法能保证每个父类的方法只会执行一次.而
使用类名的方法会导致方法被执行多次
4.>多继承时候,使用super方法,对父类的传参数,应该是是由于父类方法所需的参数,否则会报错.
5.>单继承时,使用super方法,则不能全部传递,只能传递父类方法所需的参数,否则会报错
6.>多继承时候,相对于使用类名.__init__方法,要把每个父类全部写一遍,而使用
super方法,只需写一句话便执行了全部父类的方法,这也是为何多继承需要全部传参的一个原因
"""


# -------------------property属性------------------------------------->

class Foo:
	def func(self):
		print('好吧,这个真的是实例方法')

	# 定义property属性
	@property
	def prop(self):
		print('妈的,这个不是方法啊')


foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop  # 调用property属性

"""
注意:property属性的定义和调用要注意:
1.>定义时候,在实例方法的基础上添加@property装饰器,并且仅有一个self参数
2.>调用时候,千万不能加()
"""