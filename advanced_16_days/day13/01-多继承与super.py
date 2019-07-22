"""
多继承和super的关系
"""


class Person:
	def __init__(self, name, age):
		print('Person类开始构造')
		self.name = name
		self.age = age

		print('Person类end构造')

	def love1(self):
		print('混吃等饿...')


class Man(Person):
	def __init__(self, love, *args, **kwargs, ):
		self.love = love
		print('Man类开始构造')
		super(Man, self).__init__(*args, **kwargs)
		print('Man类end构造')

	def love1(self):
		"""重写父类方法, 子类有新的实现"""
		print('%s,%d,爱好是%s' % (self.name, self.age, self.love))


class WoMan(Person):
	def __init__(self, *args, **kwargs):
		print('WoMan类开始构造')
		super(WoMan, self).__init__(*args, **kwargs)
		# self.__love = love
		print('WoMan类end构造')

	def love1(self):
		print('我爱好购物 剁手')

	# print('%s,%d,爱好是%s' % (self.name, self.age, self.__love))


class Son(Man, WoMan):
	"""多继承:一个子类有多个父类 java没有多继承,c++有"""

	def __init__(self, *args, **kwargs):
		print('Son类开始构造')
		# 当前类的下一个类 -->Man  super(Son, self).__init__()==Son.__init__()
		super(Son, self).__init__(*args, **kwargs)
		print('Son类end构造')

	def love1(self):
		print('%s,%d,爱好是%s' % (self.name, self.age, self.love))


if __name__ == '__main__':
	# p = Man('王二麻子', 50, '抽烟喝酒')
	# p.love()
	# w = WoMan('如花',18,'搓麻将')
	# w.love()
	datou = Son(name='大头', age=10,love='上学')
	datou.love1()
	# print(Son.mro())
	# print(Son.__mro__)

# <__main__.Person object at 0x0000026F4622A7F0>  <>代表一个对象
# -----------------------------单继承------------------------->
"""
1.>单继承:
因为子类需要使用父类提供的属性 必须要调用父类__init__()构造父类的属性

2.>多继承<菱形继承也叫钻石继承>:
父类.__init__(self,参数)构造父类的属性,导致父类的属性被构造多次,造成语义的二义性
super关键字作用: 为了解决这个问题

3.>MRO方法解析:
特点:在这个顺序上,保证所有的类只初始化一次
作用:使用这个顺序将所有的类的__init__()方法全部调用一次,
解决了父类.__init__方式的问题
super关键字的本质:就是使用了MRO顺序

4.>查看MRO:
	类.mro()   -->[] 类方法返回 列表类型
	类.__mro__ -->() 魔法方法返回元组类型
	
MRO顺序的特点:子类一定在父类的前面,同一级的兄弟类和子类的继承顺序有关系.

5.>super
	super关键字的本质 ---> 使用了MRO顺序
	super(参数1,参数2)在py3中两个参数可以省略,在py2两个参数不可以省略
	参数1:是继承的类的对象
	参数2:一般是self,当前类的实例对象,一般只能是self
py3中默认所有的类都是新式类<继承自object>
py2中如果没有写父类,该类是经典类,如果写了父类,该类就是新式类.<父类就是object>
super只能使用于新式类,经典类中不能使用super关键字
super不一定调的是父类哦,因为mro算法顺序的具体不一定.有可能是父类,也有可能是兄弟类

新式类:object的子类
禁止:将 类.__init__()和super().__init__()方法混用
"""
# def super(cls,self):
# 	return cls.mro[cls.find(cls) + 1]
# # super取出了当前类在mro顺序中的下一个类

"""
工作中:出现很多类的时候,使用UML 统一建模语言
类图,对象图,活动图,协作图

类属性可以被实例对象调用,反之则不行.类对象不可以调用实例属性.


"""
