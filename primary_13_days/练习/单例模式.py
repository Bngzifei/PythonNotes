"""
new:创建并返回,静态方法

init:初始化


"""


class UserInfo:
	case = None  # 类属性 例子初始值为空
	isinit = False  # 类属性 默认没有初始化
	
	# 判断创建次数
	def __new__(cls, *args, **kwargs):
		if cls.case is None:
			cls.case = object.__new__(cls)
		return cls.case
	
	def __init__(self):
		if UserInfo.isinit is False:
			self.name = '李大爷'
			UserInfo.isinit = True


user0 = UserInfo()  # 创建对象0
user1 = UserInfo()  # 创建对象1
user2 = UserInfo()  # 创建对象2

print(user0)
print(user1)
print(user2)

user0.name = '白崇禧'
print(user0.name)
print(user1.name)
print(user2.name)
