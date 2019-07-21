"""
sys模块下面的argv:系统参数的实参列表.
如果操作类属性,就使用类方法,类对象.

静态方法:不要实例和类对象的时候.

语法格式,干什么的,是什么.记住这几点,慢慢琢磨.

"""


class Dog:
	def __init__(self):  # 严格意义上来说只是继承了方法.
		self.type = '狗'


class XTQ(Dog):
	def __init__(self):  # 子类定义自己独有的属性
		self.type = '大狗'
		super().__init__()  # 继承父类Dog的属性type='狗'
		# 尽量写在自定义子类属性的前面,如果是后面,子类中和父类同名的属性值就会是父类的属性值.子类的属性值就不对了.当然,这个顺序也是要看实际开发中的需求了.不能统一规定死了
		self.color = '黑'


xtq = XTQ()
print(xtq.type)  # 输出的是XTQ父类Dog的type属性的值狗.    属性也会继承.严格意义的说是通过init()方法来继承的.
print(xtq.color)
