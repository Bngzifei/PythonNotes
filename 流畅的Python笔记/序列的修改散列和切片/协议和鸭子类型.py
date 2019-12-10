"""
协议和鸭子类型:


在Python中创建功能完善的序列类型无需使用继承,只需实现符合序列协议的方法.
不过,这里说的协议是什么呢?

在面向对象编程中,协议是非正式接口,只在文档中定义,在代码中不定义.例如,Python的序列协议只需要__len__和__getitem__两个方法.任何类,只要使用标准的签名和语义实现了这两个方法,就能用在任何期待序列的地方.是不是哪个类的子类无关紧要,只要提供了所需的方法即可.


任何有经验的Python程序员只要看一眼就知道它是序列,即便它是object的子类也无妨.我们说它是序列,因为它的行为像序列,这才是重点.人们称之为鸭子类型.


协议是非正式的,没有强制性.因此如果你知道类的具体使用场景,通常只需要实现一个协议的部分.例如,为了支持迭代,只需实现__getitem__方法.没必要提供__len__方法.




如果能委托给对象中的序列属性(如self._compontents数组),支持序列协议特别简单.下述只有一行代码的__len__和__getitem__方法是个好的开始.


切片得到的都是各自类型的新实例,而不是其他类型.

为了把Vector实例的切片也变成Vector实例,我们不能简单地委托给数组切片.我们要分析传给__getitem__方法的参数,做适当的处理.

切片原理:

调用dir(slice)得到的结果中有个indices属性,这个方法有很大的作用,但是鲜为人知.
S.indices(len)  -> (start,stop,stride)

	给定长度为len的序列,计算S表示的扩展切片的起始(start)和结尾(stop)索引.以及步幅(stride).超出边界的索引会被截掉,这与常规切片的处理方式一样.

	换句话说,indices方法开放了内置序列实现的棘手逻辑,用于优雅地处理缺失索引和负数索引,以及长度超过目标序列的切片.这个方法会整顿元组,把start,stop和stride都变成非负数,而且都落在指定长度序列的边界内.

能处理切片的__getitem__方法:

为了创建符合Python风格的对象,我们要模仿Python内置的对象.

我们使用@property装饰器把x和y标记为只读特性.我们可以在Vector中编写这四个特性.但这样太麻烦了.特殊方法__getattr__提供了更好的方式.

属性查找失败后,解释器会调用__getattr__方法.简单来说,对my_obj.x表达式,Python会检查my_obj实例有没有名为x的属性;,如果没有到类(my_obj.__class__)中查找;如果还没有,顺着继承树继续查找.如果依旧找不到,调用my_obj所属类中定义的__getattr__方法,传入self和属性名称的字符串形式(如"x")



添加__getattr__方法:
"""

shortcut_names = "xyzt"

def __getattr__(self,name):
	cls = type(self)

	if len(name) == 1:
		pos = cls.shortcut_names.find(name)
		if 0 <= pos < len(self._compontents):
			return self._compontents[pos]

	msg = "{.__name__!r} object has no attribute {!r}"
	raise AttributeError(msg.format(cls,name))



"""
__getattr__运作方式:

	仅当对象没有指定名称的属性时,Python才会调用那个方法,这是一种后备机制.可是,像v.x = 10这样赋值之后,v对象有x属性了,因此使用v.x获取x属性的值时不会调用__getattr__方法了,解释器直接返回绑定到v.x上的值,即10.另一方面,__getattr__方法的实现没有考虑到self._components之外的实例属性,而是从这个属性中获取shortcut_names中所列的虚拟属性.


!r !s 就是%r 和 %s 的一样.  !r 是显示repr(obj)  !s 是显示str(obj)
"""

def __setattr__(self,name,value):
	cls = type(self)
	if len(name) == 1:
		if name in cls.shortcut_names:
			error = "readyonly attribute {attr_name!r}"
		elif name.islower():
			error = "cannt set attributes 'a' to 'z' in {cls_name!r} "
		else:
			error = ""

	if error:
		msg = error.format(cls_name=cls.__name__,attr_name=name)
		raise AttributeError(msg)

	# 在父类上调用__setattr__方法,提供标准行为
	super().__setattr__(name,value)

"""
super()函数用于动态访问超类的方法,对Python这样支持多重继承的动态语言来说,必须能这么做.程序员经常使用这个函数把子类方法的某些任务委托给超类中适当的方法.


我们知道,在类中声明的__slots__属性可以防止设置新实例属性;因此,你可能想使用这个功能,而不像这里所做的,实现__setattr__方法.可是,正如9.8.1节所指出的,不建议只为了避免创建实例属性而使用__slots__属性.__slots__属性只应该用于节省内存,而且仅当内存不足时才应该这么做.

虽然这个示例不支持为Vector分量赋值,但是有一个问题要特别注意:多数时候,如果实现了__getattr__方法,那么也要定义__setattr__方法,以防对象的行为不一致.

如果想允许修改分量,可以使用__setitem__方法,支持v[0] = 1.1 这样的赋值,以及实现__setattr__方法,支持v.x = 1.1 这样的赋值.不过,我们要保持Vector是不可变的.



再详细一点，hash函数相当于，把原空间的一个数据集映射到另外一个空间。

所以说理论上的完美无碰撞需要映射到的空间不小于原空间。但实践中是不会这么去做。

因为用hash函数的目的就是把原空间的数据映射到一个更小的空间，以方便处理。

"""


