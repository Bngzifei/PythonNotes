"""
使用继承和派生的概念来修改标准工厂函数
定制化操作
根源是基于继承了一个标准类型,可以进行包装,然后定制自己需要的数据类型.(其实就只是在这个数据类型原来拥有的方法里面添加新的功能而已.)

包装:通常是对一个已经存在的类型进行一些定制,这种做法可以新建,修改,或者删除原有
产品的功能,其他的则保持原样.

注意:Python里面一切皆对象,所以以后所有的都可以称之为对象,操作对象的函数也不再称为函数,而是方法.
"""


class List(list):
	def append(self, object):  # self就是l这个对象,object就是添加操作的111对象
		# print('-->',object)
		if type(object) is str:
			# self.append()# 这样就递归了,出错了.
			# 所以调用父类的append方法,记得需要传入自己self,因为是self调用这个父类的append()方法
			# list.append(self,object)
			# 更好的方法是使用super(),不用传入self这个参数,super()就是在子类需要调用父类被重写的方法时候才用
			super().append(object)
		else:
			print('只能添加字符串类型')

	def show_middle(self):
		mid_index = int(len(self) / 2)  # 中间那个数的索引
		return self[mid_index]


# 这就是工厂函数 str(),list()等等模式的
# l2 = list('hello world')
# # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] <class 'list'>
# print(l2,type(l2))

l = List('helloworld')
# ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'] <class '__main__.List'> w
# print(l, type(l))  # <class '__main__.List'>
# print(l.show_middle())  # w 这样就可以取到中间值w了
# l.append(111)  # 可以加,但是自定义了append之后就可以修改这个功能了.
# print(l)  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 111]

l.append('SB')  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'SB']
print(l)
