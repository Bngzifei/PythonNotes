"""
绝对不要使用两个前导下划线,这是很烦人的自私行为.

得益于Python数据类型,自定义类型的行为可以像内置类型那样自然.实现如此自然的行为,靠的不是继承,而是鸭子类型(duck typing):我们只需要按照预定行为实现对象所需的方法即可.


这一章则自己定义类,而且让类的行为跟真正的Python对象一样.


本章包含以下话题:
	
	支持用于生成其他表示形式的内置函数(如repr(),bytes(),等等)
	使用一个类方法实现备选构造方法
	扩展内置的format()函数和str.format()方法使用的格式微语言
	实现只读属性
	把对象变为可散列的,以便在集合中及作为dict的键使用
	利用__slots__节省内存


在实现这个类型的中间阶段,我们会讨论两个概念:

	如何以及何时使用@classmethod和@staticmethod装饰器
	Python的私有属性和受保护属性的用法,约定和局限

我们从对象表示形式函数开始.


对象表示形式:

	每门面向对象的语言至少都有一种获取对象的字符串表示形式的标准方式.
	Python提供了两种方式.

	repr():以便于开发者理解的方式返回对象的字符串表示形式.
	str():以便于用户理解的方式返回对象的字符串表示形式.

正如你所知,我们要实现__repr__和__str__特殊方法,为repr()和Str()提供支持.


为了给对象提供其他的表示形式,还会用到另外两个特殊方法:__bytes__和__format__.__bytes__方法与__str__方法类似:bytes()函数调用它获取对象的字节序列表示形式.而__format__方法会被内置的format()函数和str.format()方法调用,使用特殊的格式代码显示对象的字符串表示形式.我们将在下一个示例中讨论__bytes__方法,随后再讨论__format__方法.

	
	如果你是从Python2转过来的,记住,在Python3中,__repr__,__str__和__format__都必须返回Unicode字符串(str类型).只有__bytes__方法应该返回字节序列(bytes类型)

	
再谈向量类:
"""

from array import array
import math

class Vector2d:
	typecode = "d"  # 是类属性


	def __init__(self,x,y):
		self.x = float(x)  # 在__init__方法中把x和y转换成浮点数,尽早捕获错误,以防调用Vector2d函数时传入不当参数
		self.y = float(y)

	def __iter__(self):
		"""定义__iter__方法,把Vector2d实例变成可迭代的对象,这样才能拆包(例如,x,y = my_vector 这个方法的实现方式很简单,直接调用生成器表达式一个接一个产出分量"""
		return (i for i in (self.x,self.y))

	def __repr__(self):
		class_name = type(self).__name__
		# 使用{!r获取各个分量的表示形式,然后插值,构成一个字符串}
		return "{}({!r},{!r})".format(class_name,*self)

	def __str__(self):
		"""从可迭代的Vector2d实例中可以轻松地得到一个元组,显示为一个有序对"""
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))

	def __eq__(self,other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.hypot(self.x,self.y)

	def __bool__(self):
		return bool(abs(self))

"""
示例中的__eq__方法,在两个操作数都是Vector2d实例时可用,不过拿Vector2d实例与其他具有相同数值的可迭代对象相比,结果也是True.这个行为可以视作特性,也可以视作缺陷.


备选构造方法:
	
	我们可以把Vector2d实例转换成字节序列了,同理,也应该能从字节序列转换成Vector2d实例.在标准库中探索一番之后,我们发现array.array有个类方法.frombytes正好符合需求.
"""

