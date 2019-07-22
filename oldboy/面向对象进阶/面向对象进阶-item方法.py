class Foo:
	def __getitem__(self, item):  # get:查询
		print('getitem')
		return  self.__dict__[item]
	def __setitem__(self, key, value):  # 赋值
		print('setitem')
		self.__dict__[key] = value  # 定制属性

	def __delitem__(self, key):  # 删除
		print('delitem')
		self.__dict__.pop(key)


f1 = Foo()
# print(f1.__dict__)  # {}
# f1.name = 'egon'
# print(f1.__dict__)  # {'name': 'egon'}
# f1['name'] = '李斌'
f1['age'] = 18
# del f1.name
print(f1['age'])
# del f1['name']
# print(f1.__dict__)  # {'name': '李斌', 'age': 18}

"""
.的方式操作属性,就是和attr系列相关

[键] 的方式操作属性,就是和item系列相关


"""