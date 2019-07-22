print('面向对象进阶-反射...')
"""
反射(自省):程序可以访问,检测和修改它本身状态或行为的一种能力,也称之为自省.

Python中实现反射的四个函数:
	1.>hasattr(obj,name):判断一个对象object中有没有一个name字符串对应的属性<name是字符串形式,就是一个名字>
	2.>getattr(obj,name):
	3.>setattr(x,y,v):
	4.>delattr(x,y):
类和对象都适用	
	
为啥用反射?:
	可以事先定义好接口,接口只有在被完成后才会真正执行,这实现了即插即用,这其实是一种
	'后期绑定'. 什么意思? 即你可以事先把主要的逻辑写好(只定义接口),然后后面再去实现接口的功能.

反射/自省: 其实就是检查自己有没有对应的属性和方法.
"""


class BlackMedium:
	feature = 'Ugly'

	def __init__(self, name, addr):
		self.name = name
		self.addr = addr

	def sell_house(self):
		print('[%s] 正在卖房子,傻逼才买呢' % self.name)

	def rent_house(self):
		print('[%s] 正在租房子,傻逼才租呢' % self.name)


# Python里面一切皆对象.
print(hasattr(BlackMedium, 'feature'))  # True

# b1 = BlackMedium('万成置地', '天露园')
# print(b1)
# b1.name  --> b1.__dict__['name']
# print(b1.__dict__)  # {'name': '万成置地', 'addr': '天露园'}
#
#
# # b1.sell_house()  # [万成置地] 正在卖房子,傻逼才买呢
# # print(hasattr(b1, 'name'))  # True
# # # 就是检测b1是否能调用b1所拥有的属性,方法
# print(hasattr(b1, 'sell_house'))  # True,有的,就是True
# print(hasattr(b1, 'house'))  # False  ,没有的,输出False
#
#
# print(getattr(b1, 'name'))  # 万成置地
# print(getattr(b1, 'addr'))  # 天露园
# # 是一个方法的地址,只要加了(),这个方法就调用了
# print(getattr(b1, 'sell_house'))  # <bound method BlackMedium.sell_house of <__main__.BlackMedium object at 0x000001
# # 没有就会报错
# print(getattr(b1, 'rent_house'))  # <bound method BlackMedium.rent_house of <__main__.BlackMedium object at 0x000001
# print(getattr(b1, 'rent_house1111','没有这个属性'))  # 如果没有rent_house1111这个属性,可以输出指定内容  没有这个属性
# func = getattr(b1, 'sell_house')
# # 调用
# func()  # [万成置地] 正在卖房子,傻逼才买呢

# getattr(x,'y')  等价于 x.y


# b1.sb = True
# setattr(b1,'sb',True)  # 设置属性
# setattr(b1,'sb1', 123)
# setattr(b1,'name','SB1')
# 设置一个方法进去
# setattr(b1, 'func1', lambda x: x + 1)  # {'name': '万成置地', 'addr': '天露园', 'func1': <function <lambda> at 0x000002538
# setattr(b1, 'func2', lambda self: self.name + 'sss')
# print(b1.__dict__)  # {'name': 'SB1', 'addr': '天露园', 'sb': True, 'sb1': 123}
# print(b1.func1)  # <function <lambda> at 0x000002137E4FB9D8>
# print(b1.func1(10))  # 11
# print(b1.func2(b1))  # 万成置地sss


# del b1.sb
# print(b1.__dict__)  # {'name': 'SB1', 'addr': '天露园'} 删除了sb键
#
# delattr(b1,'sb')  # {'name': 'SB1', 'addr': '天露园'} 删除了sb键
# print(b1.__dict__)


"""为啥用反射?
最大的作用:就是在需要使用别人模块里面的方法属性的时候,不需要管别人是否已经实现,
自己可以使用反射预先判断,不受别人影响.自己可以直接往后继续进行开发,不用等.
"""


# A写的,功能还未实现
class Ftpclient:
	"""ftp客户端,但是还没有实现具体功能"""

	def __init__(self, addr):
		print('正在连接服务器%s' % addr)
		self.addr = addr


		# B写的,需要使用A写的
		# from module import Ftpclient  # 假设先得导入A写的模块
		# f1 = Ftpclient('192.168.6.166')
		# if hasattr(f1,'get'):
		# 	func_get = getattr(f1,'get')
		# 	func_get()
		# else:
		# 	print('---> 不存在此方法')
		# 	print('处理其他逻辑')
