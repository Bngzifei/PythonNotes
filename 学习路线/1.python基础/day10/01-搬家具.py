"""搬家具:"""
# del:主要是用来测试使用的

"""
类图:

1.class Item:
属性: type(类型),area(面积)

方法:str(),


2.class Home
属性:address area = 200 free_area = 200
	

方法: add_item(self,item_area)



"""


class Item:
	"""家具类"""

	def __init__(self, type_str, area):
		self.type = type_str  # 类型
		self.area = area  # 面积

	def __str__(self):
		return "%s家具,占地面积:%d" % (self.type, self.area)


bed = Item('床', 4)
print(bed)


class Home:
	"""房子类"""

	def __init__(self, address):
		self.address = address
		self.area = 200
		self.free_area = 200

	# def add_item(self, item_area, item_type):  # 通过一个一个的参数传递属性的值  1,2 个就使用这个
	def add_item(self, item):  # Python参数非常灵活.优化代码,多的时候需要使用这个方法.直接传一个对象过来,使用 对象.属性 的方式就可以了
		"""装家具"""
		if self.free_area >= item.area:
			print('添加%s家具成功' % item.type)
			self.free_area -= item.area  # 修改剩余面积
		else:
			print('添加失败')

	def __str__(self):
		return '我家在%s,面积%d,可用面积%d' % (self.address, self.area, self.free_area)


h1 = Home('天安门广场')
h1.add_item(bed)  # 家具.面积  引用的传递
print(h1)
