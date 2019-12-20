"""str()就是可以自定义输出返回值,必须是str字符串"""


class Dog:
	def __init__(self, name):
		self.name = name

	def __str__(self):  # 把对象放在print()方法中输出时,就会自动调用str()方法
		return '呵呵呵%s' % self.name  # 只能返回字符串


# overrides method :覆盖方法  重写了
dog1 = Dog('来福')
print(dog1)  # 如果将str()方法注释掉,把对象放在print中输出时,默认输出的是对象的内存地址 <__main__.Dog object at 0x0000015BF223B320>
# dog1.__str__() 这一步是自动调用了,自定义返回值

# ss = type(dog1)
# print(ss)
