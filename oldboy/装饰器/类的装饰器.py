# def deco(func):
# 	print('-----------')
# 	return func
#
# # @deco
# # def test():
# # 	print('test 函数运行')
# #
# #
# # test()
#
# @deco  #Foo = deco(Foo)
# class Foo:
# 	pass
#
#
# f1 = Foo()
# print(f1)

# --------------------给类增加内置属性--------------------------------->
# 类和函数都是一个对象
# def deco(obj):
# 	print('-----------:',obj)
# 	obj.x = 1  # 这样就给类增加了属性
# 	obj.y = 2
# 	obj.z = 3
# 	return obj   # 提示中p开头的是参数
#
# @deco  #Foo = deco(Foo)
# class Foo:
# 	pass
#
#
# print(Foo.__dict__)  # 属性字典里面多了'x': 1, 'y': 2, 'z': 3

# ---------------验证:一切皆对象--------------------------->
# def deco(obj):
# 	print('-----------:',obj)
# 	obj.x = 1  # 这样就给类增加了属性
# 	obj.y = 2
# 	obj.z = 3
# 	return obj   # 提示中p开头的是参数
#
# @deco  #test = deco(test)
# def test():
# 	print('test函数')
#
# # test.r = 333  # {'r': 333} 外部直接定义属性值
# print(test.__dict__)  # {'x': 1, 'y': 2, 'z': 3}

# ----------------------类的装饰器修订版------------------------->
# def typed(**kwargs):
# 	def deco(obj):
# 		print('**', kwargs)  # 2
# 		print('类名', obj)  # 3
# 		for key,val in kwargs.items():
# 			# obj.key = val
# 			setattr(obj,key,val)
# 		return obj
#
# 	print('-->', kwargs)  # 1
# 	return deco
#
#
# # 这样就执行了 1.typed(x=1,y=2,z=3) 返回值就是deco 2.@deco ---> Foo=deco(Foo)
# @typed(x=1, y=2, z=3)  # Foo = deco(Foo)
# class Foo:
# 	pass
#
# @typed(name='alex')  # @deco -----> Bar = deco(Bar)
# class Bar:
# 	pass
#
#
# print(Bar.name)  # alex
#
# print(Foo.__dict__)

# ----------------------------------类的装饰器的作用--------------------->

