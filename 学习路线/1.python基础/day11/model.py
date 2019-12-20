"""单例要写几遍"""


class UserInfo:
	__instance = None  # 此属性来保存创建好的实例对象.__不让外部修改
	__has_init = False  # 默认还未初始化

	def __new__(cls, *args, **kwargs):
		# print(cls)  # <class '__main__.UserInfo'>  隐藏了这个过程# UserInfo.__new__(UserInfo)  # 当前类
		# obj = object.__new__(UserInfo)  # 创建的是UserInfo对象,所以设置成了静态方法,让我们自己去手动控制传递的类对象.默认是调用的自己的.父类被重写了

		if cls.__instance is None:
			cls.__instance = object.__new__(cls)  # 保证只会创建一次

		# 创建的是UserInfo对象,所以设置成了静态方法,让我们自己去手动控制传递的类对象.默认是调用的自己的.父类被重写了

		return cls.__instance  # 这样就只会创建一次.这里不能缩进到if里面,否则第2个就是None

	def __init__(self):  # 2次

		# if UserInfo.__has_init is False:
		# 	self.name = '超哥'
		# 	UserInfo.__has_init = True  # 已经初始化


		if self.__has_init is False:  # 如果是这样self的,就意味着类属性__has_init和实例属性和同名了,虽然这里的代码运行结果没有错误,但是实际代表的意思已经发生改变了.
			self.name = '超哥'
			self.__has_init = True  # 已经初始化  表示实例对象也拥有了一个和类属性同名的实例属性 __has_init


user1 = UserInfo()
user1.name = '小1111111超'
user2 = UserInfo()
# user2.name = '小超超'
