class Dog:
	"""定义了一个Dog类"""
	def eat(self):
		print('吃鸡')
		# print(self)  # 如果在eat()方法中不调用self参数,eat()会提示:警告eat()是可能是一个static静态方法.


dog1 = Dog()
dog1.eat()

a = 10  # 给一个变量赋值
print(a)  # 调用(输出)这个变量的值

# 格式:对象.属性 = 值  首次给属性赋值叫定义属性(创建属性)
dog1.name = 'xiaowang'  # 定义属性
dog1.name = 'xiaowang11'  # 修改属性的值,这两个是同一个属性,只是值不一样了
print(dog1.name)

dog1.age = 2
print(dog1.age)
