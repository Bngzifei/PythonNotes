class Lazyproperty:  # 延迟property 实现延迟计算
	def __init__(self,func):
		self.func = func
	def __get__(self, instance, owner):
		# print('get')
		# print(instance)
		# print(owner)

		if instance is None:  # 因为类调用的时候会返回一个None,程序出错
			return self

		val = self.func(instance)
		return val


class Room:

	def __init__(self,name,width,length):
		self.name = name
		self.width = width
		self.length = length

	# @property  # area = propery(area)  这个@property 的作用就是把方法当成了属性使用了
	# area = Lazyproperty(area)
	@Lazyproperty
	def area(self):
		return self.width * self.length  # 传了一个None进去
	@property  # test = property(test)
	def area1(self):
		return self.width * self.length

r1 = Room('厕所',10,10)
# 实例调用
# print(r1.area)
# print(r1.area)
# print(r1.area)
print(r1.area1)
print(r1.area1)
print(r1.area1)
# print(r1.test)
# 类调用
# print(Room.area)
# 类调用
# print(Room.area1)