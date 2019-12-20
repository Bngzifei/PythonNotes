"""
要求：
1.在类内定义一个可以重新设置私有属性name的函数条件为字符串长度小于10,才可以修改.
"""
# class Name:
# 	def SetName(self,newname):
# 		if len(newname) < 10:
# 			self.__name = newname
# 		else:
# 			print('error:名字太长')


"""
创建一个动物类,并通过init方法接受参数(name),并打印init被调用.

"""

# class Animal:
# 	def __init__(self, str_name):
# 		self.name = str_name
#
# 	def __str__(self):
# 		return self.name
#
#
# a1 = Animal('骡子')
# print(a1)
"""
写出一个简单的多继承案例.

"""

# 定义一个父类

# class language:
# 	def printlanguage(self):
# 		print('---language---')
#
#
# # 定义第二个父类
#
# class Cpp:
# 	def printCpp(self):
# 		print('---C++---')
#
#
# # 定义一个子类
#
# class Python(language, Cpp):
# 	def printPython(self):
# 		print('---Python---')
#
#
# P1 = Python()
# P1.printCpp()
# P1.printlanguage()
# P1.printPython()

""" 
定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
将类中的姓名和年龄私有化.
提供获取用户信息的函数.
提供获取私有属性的方法.
提供可以设置私有属性的函数.
设置年龄的范围(0-100).

"""

#
# class BasePerson:
# 	def __init__(self, name_str, age):
# 		self.__name = name_str
# 		self.__age = age
#
# 	# def __str__(self):
# 	# 	return '%s,%d' % (self.__name, self.__age)
#
# 	def get_att(self):
# 		return '姓名:%s,年龄:%d' % (self.__name, self.__age)
#
# 	# 添加获取私有属性的方法
# 	def get_Name(self):
# 		return self.__name
#
# 	def get_Age(self):
# 		return self.__age
#
# 	# 添加设置姓名的函数
# 	def set_Name(self, name1):
# 		self.__name = name1
# 		return self.__name
#
# 	# 添加设置年龄
# 	def set_Age(self, age1):
# 		if 0 < age1 <= 100:
# 			self.__age = age1
# 			return str(self.__age)
# 		else:
# 			return '年龄有误!'



# p1 = BasePerson('老五', 56)
# print(p1.get_att())
# print(p1.get_Age())
# print(p1.get_Name())
# print(p1.set_Age(79))
# print(p1.set_Name('大道质检'))


# print(print('***'))  # ***  None 这样的结果是因为print()函数中继续调用print()函数了


"""
编写一段代码以完成继承和多态

要求：

创建一个动物的基类,其中有一个run方法
创建一个cat类继承于动物类
创建一个dog类继承于动物类
cat类中不仅有run方法还有eat方法
dog类中方法同上
编写测试程序已验证
"""

# class Animal:
# 	def run(self):
# 		print('running')
#
#
# class Cat(Animal):
# 	def eat(self):
# 		print('eating1')
#
#
# class Dog(Animal):
# 	def eat(self):
# 		print('eating2')
#
#
# c1 = Cat()
# c1.eat()
# c1.run()
#
# d1 = Dog()
# d1.eat()
# d1.run()
