print('面向对象:')

"""面向对象编程:
面向对象的概念:
OOP:Object Oriented Programming:意为将具有相互关系的数据/操作封装成对象,以对象的角度去处理问题,让对象来完成相应处理

面向对象 和 面向过程:

按照业务逻辑 从上到下 设计程序的方式,叫做面向过程编程(POP)Procedure Oriented Programming .POP 面向过程程序设计.

面向对象\编程的优点:
	将数据和业务抽象为 对象,有利于程序整体结构的分析和设计,使设计思路更加清晰
	业务以对象为单位,对象各自完成工作,减少了代码耦合度,有助于业务升级 和 代码重构
	方便工作划分,有利于提高团队开发的效率

"""

"""类和对象:
对象:是承载数据,执行操作的一个具体"事物",比如具体某一个人,具体某一只狗

组成部分:1.属性:用于记录与对象相关的数据,比如姓名,年龄,身高,肤色等等
2.方法:用于实现与对象相关的操作,比如吃饭睡觉,飞行,歌唱等等

类:很多事物存在相同的操作行为,比如人都进行吃饭,睡觉,狗都会叫等等

描述共同行为的集合,称之为类(class)

类是总结事物特征的抽象概念,而对象是具体存在的某个实物

类和对象的关系:

在编程中,类就是创建对象的模板 或者 说制造手册,用来定义 对象 公共的行为(大家都有的)

类总结了对象的共同特征,有利于复用代码创建拥有相同特征的对象

每个对象必须有一个对应的类

"""

"""
定义类:
class 类名:
	方法列表(就是面向对象中的函数)

类名 的命名规则按照大驼峰命名法进行
"""

"""定义方法:

类是定义对象的共同行为的,也就是说在类中定义对象的方法.

定义方法:
	class 类名:
		def 方法名(self):
			...
注意: 方法的格式和函数类似,也可以设置参数和返回值,但是,需要设置第一个参数为self
注意:定义方法需要在类的缩进中(范围之内)

"""

"""定义一个Cat类"""

# 定义类
# class Cat:
# 	def eat(self):
# 		print('猫在吃鱼...')
#
# 	def drink(self):
# 		print('猫在和可乐...')


"""创建对象:

引用对象的变量名 = 类名()

"""

# # 定义一个类
# class Cat:
# 	def eat(self):
# 		print('猫在吃鱼...')
#
# 	def drink(self):
# 		print('猫在喝可乐...')
#
#
# # 根据类,创建一个对象
# tom = Cat()
# print(type(print))
"""调用方法:
创建对象的格式为:
引用对象的变量名.方法名()

注意:虽然定义方法时设置第一个参数 self ,但是 调用方法时不要传递对应self 的参数

"""
# class Cat:
# 	# 属性
# 	# 方法
# 	def eat(self):
# 		print('猫在吃鱼...')
#
# 	def drink(self):
# 		print('猫在喝可乐...')


# # 根据类,创建一个对象
# tom = Cat()
# # 调用对象的eat方法
# tom.eat()
# tom.drink()


"""定义/使用属性
定义/设置属性 格式:
引用对象的变量名.属性名 = 数据(所有数据类型均可以)

"""
# 属性和变量类似,首次赋值时会定义属性

# 创建对象
# tom = Cat()
#
# # 首次赋值属性,会定义属性
# tom.age = 3
#
# # 定义属性后,再赋值属性,会修改属性保存的数据
# tom.age = 1

# 获取属性值并打印
# print(tom.age)

"""创建多个对象:

类作为对象的模具,根据类可以创建多个对象

Python语法要求  方法必须定义在类中,如果某个行为只有一个对象拥有,也需要为该对象单独设计一个类

"""
# 创建了一个对象
# tom = Cat()
# tom.name = '桐木'
# tom.age = 30
# tom.eat()
#
# # 创建了另外一个对象
# lan_mao = Cat()
# lan_mao.name = '蓝猫'
# lan_mao.age = 20
# lan_mao.eat()


"""self关键字:

self主要用于对象方法中,表示调用该方法的对象

在方法中使用self,可以获取到调用当前方法的对象.进而获取到该对象的属性和方法

某个对象调用其方法时,python解释器会把  这个对象 作为  第一个参数  传递给  方法
所以开发者只需要在定义方法时"预留" 第一个参数为self 即可


"""

# class Cat:
# 	# 方法
# 	def introduce(self):
# 		print('名字是%s,年龄是%d' % (self.name,self.age))
#
# # 创建一个对象
# tom = Cat()
#
# # 给tom对象添加了一个属性,叫name,里面的值是'汤姆'
# tom.name = '汤姆'
#
# tom.age = 5
# tom.introduce() # 打印结果:name是汤姆,age是5
#
# # 创建另外一个对象
# lan_mao = Cat()
# lan_mao.name = '蓝猫'
# lan_mao.age = 20
# lan_mao.introduce()  # 打印结果:名字是蓝猫,年龄是20

"""方法中定义属性:
使用self操作属性 和对象的变量名操作属性效果上相同,如果属性在赋值时还没有定义,则会自动定义属性并赋值


"""
# class Cat:
# 	# 方法
# 	def introduce(self):
# 		self.type = '小型动物'
#
# # 创建了一个对象
# tom = Cat()
# # 调用对象的方法
# tom.introduce()
# # 获取对象的属性
# print(tom.type)
#
# # 创建另一个对象
# lanmao = Cat()
# # 获取对象的属性
# print(tom.type)
# # 调用对象的方法
# tom.introduce()


"""__init__()方法:

记住:带 函数名() 这种格式的不是函数就是方法

__init__()方法:叫做对象的初始化方法,在 创建一个对象后默认会被调用,不需要手动调用

可以实现这个方法,并在该方法中定义属性并设置初始值

"""

# class Cat:
# 	# 初始化方法
# 	def __init__(self):
# 		# 设置对象的默认属性及初始值
# 		self.type = '小型动物'
#
#
# # 创建了一个对象
# tom = Cat()
# # 获取对象的属性
# print(tom.type)

"""__init__()自定义参数:
__init__(self)除了默认参数self ,还可以设置任意个数的自定义参数,例如

__init__(self,x,y,z)
init方法  设置的自定义参数必须和创建对象时候传递的参数保持一致,例如 tom = Cat(x,y,z)

开发者可以 设置 自定义参数,为对象的 默认属性 提供不同的 初始值

开发中,一般会在__init__()中定义 对象 的 属性


"""

# class Cat:
# 	# 方法
# 	def __init__(self,new_name,new_age):
# 		"""在创建完对象之后 会自动调用,它完成对象的初始化的功能(就是工厂造人一样.批量生产)"""
# 		self.name = new_name
# 		self.age = new_age
#
# 	def introduce(self):
# 		print('名字是:%s,年龄是:%d' % (self.name,self.age))


# 创建了一个对象

# tom = Cat('汤姆',30)
# print(tom)  # <__main__.Cat object at 0x0000022F5742B940> 对象在内存中的地址
# print(tom.name)
# print(tom.age)
# tom.introduce()
#
# print('=' * 30 )
#
# lan_mao = Cat('蓝猫',20)
# lan_mao.introduce()
# print(lan_mao.name)
# print(lan_mao.age)


"""__str__()方法:
如果直接print打印对象,会看到创建出来的对象在内存中的地址

当使用print(xx)输出对象的时候,只要 对象 定义 了__str__(self)
方法,就 会 打印 该方法 return 的信息描述


在Python中方法如果是__xxx__()的,name就有特殊的功能,因此叫做"魔法"方法

"""

# class Cat:
# 	"""定义一个猫类"""
#
# 	def __init__(self, new_name, new_age):
# 		"""在创建完对象之后, 会自动调用,它完成对象的初始化的功能 """
#
# 		self.name = new_name
# 		self.age = new_age  # 它是一个对象中的属性,在对象中存储.即只要这个对象还存在,那么这个变量就可以使用
#
# 	# num = 100 #  它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量
# 	def __str__(self):
# 		"""返回一个对象的描述信息"""
# 		return ('他的名字是:%s,年龄是:%d' % (self.name, self.age))
#
# 	def eat(self):
# 		print('%s在吃鱼...' % self.name)
#
# 	def drink(self):
# 		print('%s在喝可乐...' % self.name)
#
# 	def introduce(self):
# 		print('名字是:%s,年龄是:%d' % (self.name, self.age))
#
#
# tom = Cat('汤姆', 30)
# print(tom)  # 输出:他的名字是:汤姆,年龄是:30.这里不是introduce()方法


"""应用一:烤地瓜
类,属性,方法

方法中使用self可以获取和修改属性


"""

# 创建地瓜类,定义__init__()方法,定义__str__()方法

# class SweetPotato:
# 	"""地瓜类"""
#
# 	def __init__(self):
# 		self.cookied_state = '生的'  # 地瓜初始状态
# 		self.cookied_time = 0  # 烧烤时间
# 		self.condiments = []  # 佐料列表,添加多个佐料
#
# 	def __str__(self):
# 		return '地瓜状态:%s,烧烤总时间:%d,包含的佐料:%s' % (self.cookied_state, self.cookied_time, self.condiments)
#
# 	# 定义烤地瓜方法
# 	def cook(self, time):
# 		"""烧烤"""
# 		# 本次烧烤时间累加到 烧烤总时间中
# 		self.cookied_time += time
# 		# 根据烧烤总时间 改变地瓜的状态
# 		if 0 <= self.cookied_time < 3:
# 			self.cookied_state = '生的'
# 		elif 3 <= self.cookied_time < 6:
# 			self.cookied_state = '半生不熟'
# 		elif 6 <= self.cookied_time < 8:
# 			self.cookied_state = '熟了'
# 		else:
# 			self.cookied_state = '烤糊了'
#
# 	def add_condiments(self, condiment):
# 		"""添加佐料"""
# 		self.condiments.append(condiment)  # self.condiments:这个是地瓜属性,是个列表
#
#
# # 创建对象
# digua1 = SweetPotato()
# digua1.cook(1)
# print(digua1)
# print('-'*30)
#
# digua1 = SweetPotato()
# digua1.cook(5)
# digua1.add_condiments('醋')
# digua1.add_condiments('盐')
# digua1.add_condiments('味精')
# print(digua1)
# print('-'*30)
#
# digua1 = SweetPotato()
# digua1.cook(8)
# digua1.add_condiments('盐')
# print(digua1)
# print('-'*30)
#
# digua1 = SweetPotato()
# digua1.cook(9)
# digua1.add_condiments('孜然')
# digua1.add_condiments('辣椒酱')
# print(digua1)

"""应用2:搬家具
类创建的对象,可以作为参数被传递
传递对象相比传递属性的优点

家具的两个属性:
	1.家具类型type:字符串
	2.家具面积area:整数

房子类:
	1.地址address:字符串
	2.房子面积area:整数
	3.房子剩余面积free_area:整数
	4.家具列表items:列表


主程序逻辑:

1.创建家具对象,输出 家具信息

2.创建房子对象,输出 房子信息

3.房子添加家具,输出 房子信息
"""

# 定义家具类Item
# class Item:
# 	"""家具类"""
#
# 	def __init__(self, type, area):
# 		self.type = type  # 家具类型
# 		self.area = area  # 家具占用的面积
#
# 	def __str__(self):
# 		return '家具为%s,占用面积:%d' % (self.type, self.area)
#
#
# class Home:
# 	"""房子类"""
#
# 	def __init__(self, address, area):
# 		self.address = address  # 房子地址
# 		self.area = area  # 房子面积
# 		self.free_area = area  # 房子的剩余面积
# 		self.items = []  # 家具列表, 保存该房子中的家具(家具对象)
#
# 	def __str__(self):  # 输出房子时,显示包含的所有家具类型
#
# 		# 房子在xx,面积为xx,包含的家具有:双人床,冰箱
# 		res_str = '房子在:%s,面积为:%d,剩余面积为:%d' % (self.address, self.area, self.free_area)
#
# 		# 判断是否包含家具
# 		if len(self.items) > 0:  # 有家具
# 			res_str += ',包含的家具有:'
# 			# 遍历家具列表,取出每一个家具(对象),然后拼接家具的type属性
# 			for item in self.items:
# 				res_str += item.type + ','
# 			res_str = res_str.rstrip(',')  # 去掉最后一个家具后面的,号
# 		return res_str
#
# 	def add_items(self, item):
# 		"""添加家具"""
# 		# 先判断房子是否能够容纳该家具
# 		result_area = self.free_area - item.area
# 		if result_area >= 0:  # 可以容纳
# 			print('%s 添加成功' % item.type)
# 			self.items.append(item)
# 			self.free_area -= item.area
# 		else:
# 			print('房子面积不足,%s 添加失败' % item.type)
#
#
# # 创建家具对象
# item1 = Item('双人床', 4)
# print(item1)
#
# # 创建房子
# Home1 = Home('北京天通苑', 200)
# print(Home1)
#
# # 添加家具
# Home1.add_items(item1)
# print(Home1)
#
# # 再添加一个家具
# item2 = Item('冰箱', 2)
# print(item2)
#
# Home1.add_items(item2)
# print(Home1)
#
# item3 = Item('篮球场', 420)
# print(item3)
#
# Home1.add_items(item3)
# print(Home1)

"""面向对象二"""

"""私有属性:

目的:为了避免属性被设置为脏数据,更好的保护属性安全,一般的处理方式为:
	1.添加一个方法,在方法内部先判断数据的有效性,再赋值属性
	2.将属性定义为私有属性,避免对象在外部直接操作属性

如果在属性名前面加了2个下划线'__' ,则表明该属性是私有属性,否则为公有属性

私有属性只能在类的内部访问

"""

# class People(object):
# 	def __init__(self, name):
# 		self.__name = name
#
# 	def getName(self):
# 		return self.__name
#
# 	def setName(self, newname):
# 		if len(newname) >= 5:
# 			self.__name = newname
# 		else:
# 			print('error:名字长度需要大于或者等于5')
#
#
# xiaoming = People('dongge')
# print(xiaoming.__name)  # 这样的就不行,这里就写死了,不允许直接对它进行修改,只能通过setName方法来修改名字
# print(xiaoming.getName())  # 必须通过getName方法来获取名字
#
# xiaoming.setName('wanger')
# print(xiaoming.getName())
#
# xiaoming.setName('lisi111')
# print(xiaoming.getName())

"""私有方法:
在方法名前面加2个'__' ,则表明该方法是私有方法

私有方法只能在类 内部使用

私有方法和私有属性的设计目的主要有两个:
	1.保护数据或操作的安全性
	2.向使用者隐藏核心开发细节


"""

# class People:
# 	def __init__(self):
# 		self.money = 0  # 账户余额
#
# 	def send_msg(self):
# 		if self.money >= 1:
# 			self.__send_msg()
# 		else:
# 			print('余额不足,请充值')
#
# 	def __send_msg(self):
# 		print('发送短信')
#
#
# xiaoming = People()
# xiaoming.send_msg()
# xiaoming.money = 100
# xiaoming.send_msg()


"""__del__方法:

创建对象之后,Python解释器默认调用__init__()方法

__del__(): 当 删除 一个对象时,Python解释器 默认调用的 一个方法


当使用del删除变量时,只有当变量指向的对象的所有引用都被删除后,也就是引用计数为0时,才会真正
删除该对象(释放内存空间),这是才会触发__del__()方法

"""
# import time
#
#
# class Animal:
# 	# 初始化方法
# 	# 创建完对象后会自动被调用
# 	def __init__(self, name):
# 		print('__init__方法被调用')
# 		self.__name = name
#
# 	# 解构方法
# 	# 当对象被删除时,会自动被调用
# 	def __del__(self):
# 		print('__del__方法被调用')
# 		print('%s对象马上被干掉了...' % self.__name)
#
#
# # 创建对象
# dog = Animal('癞皮狗')
#
# # 删除对象
# del dog
#
#
# cat = Animal('波斯猫')
# cat2 = cat
# cat3 = cat
#
#
# print('---马上删除cat的对象引用')
# del cat
# print('---马上删除cat2的对象引用')
# del cat2
# print('---马上删除cat3的对象引用')
# del cat3
#
# print('程序2秒钟后结束')
# time.sleep(2)

"""继承:

面向对象三大特征:1.封装 2.继承 3.多态
继承:某个类直接具备另外一个类的能力(属性和方法)
格式:
class 子类名(父类名):
"""

# class Animal:
# 	def eat(self):
# 		print('-----吃-----')
#
# 	def drink(self):
# 		print('-----喝-----')
#
#
# class Dog(Animal):
# 	pass
#
#
# class Cat(Animal):
# 	pass
#
#
# wang_cai = Cat()
# wang_cai.eat()
# wang_cai.drink()

"""子类添加新功能:"""

# class Animal:
# 	def eat(self):
# 		print('-----吃-----')
#
# 	def drink(self):
# 		print('-----喝-----')
#
#
# class Dog(Animal):
# 	def bark(self):
# 		print('-----汪汪叫-----')
#
#
# class Cat(Animal):
# 	def catch(self):
# 		print('----捉老鼠-----')
#
#
# wang_cai = Dog()
# wang_cai.eat()
# wang_cai.drink()
# wang_cai.bark()
#
# jia_fei = Cat()
# jia_fei.eat()
# jia_fei.drink()
# jia_fei.catch()


"""多层继承"""

# class Animal:
# 	def eat(self):
# 		print('-----吃-----')
#
# 	def drink(self):
# 		print('-----喝-----')
#
#
# class Dog(Animal):
# 	def bark(self):
# 		print('-----汪汪叫-----')
#
#
# class Cat(Animal):
# 	def catch(self):
# 		print('----捉老鼠-----')
#
#
# class XTQ(Dog):
# 	"""定义了一个哮天犬类"""
# 	pass
#
# xtq = XTQ()
# xtq.eat()
# xtq.drink()
# xtq.bark()

# wang_cai = Dog()
# wang_cai.eat()
# wang_cai.drink()
# wang_cai.bark()
#
# jia_fei = Cat()
# jia_fei.eat()
# jia_fei.drink()
# jia_fei.catch()

"""重写父类方法:
重写父类方法: 当子类实现一个和父类同名的方法

子类重写了父类方法,子类再调用该方法将不会执行父类的处理



"""

# class Animal:
# 	def eat(self):
# 		print('-----吃-----')
#
# 	def drink(self):
# 		print('-----喝-----')
#
#
# class Dog(Animal):
# 	def bark(self):
# 		print('-----汪汪叫-----')
#
#
# class Cat(Animal):
# 	def catch(self):
# 		print('----捉老鼠-----')
#
#
# class XTQ(Dog):
# 	"""定义了一个哮天犬类"""
# 	def bark(self):
# 		print('----嗷嗷叫-----')
#
# xtq = XTQ()
# xtq.eat()
# xtq.bark()


"""调用被重写的父类方法:"""

# class Animal(object):
# 	def eat(self):
# 		print('------吃------')
#
# 	def drink(self):
# 		print('------喝------')
#
#
# class Dog(Animal):
# 	def bark(self):
# 		print('---汪汪叫---')
# 		print('---汪汪叫---')
# 		print('---汪汪叫---')
# 		print('---汪汪叫---')
# 		print('---汪汪叫---')
# 		print('---汪汪叫---')
#
#
# class XTQ(Dog):
# 	"""定义了一个哮天犬类"""
#
# 	def bark(self):
# 		super(XTQ, self).bark()  # 调用已经被重写的方法2
# 		# super().bark()  # 调用已经被重写的方法3
# 		print('---嗷嗷叫---')
#
#
# xtq = XTQ()
# # xtq.eat()
# xtq.bark()


# class People:
# 	def __init__(self):
# 		self.name = '人'
#
#
# class Student(People):
# 	def __init__(self):  #重写了父类的init方法
# 		super().__init__()  # 不调用父类的init,父类的name属性就不会被定义
# 		self.age = 10
# 		# self.name = '学生'
#
# 	def stu_info(self):
# 		print('%s:%d' % (self.name,self.age))
#
#
# xiaoming = Student()
# xiaoming.stu_info()  # 打印结果

"""私有方法.属性.继承的问题:

父类中的私有方法,属性,不会被子类继承
可以通过调用继承的父类的共有方法,间接的访问父类的私有方法,属性

"""

# class Aniamal:
# 	def __init__(self):
# 		self.num1 = 1
# 		self.__num2 = 2  # 私有属性
#
# 	def __run(self):  # 私有方法
# 		print('---跑---')
#
# 	def eat(self):
# 		print('---吃---')
#
# 	def drink(self):
# 		print('---喝---')
#
# 	def test(self):
# 		print(self.__num2)
# 		self.__run()  # 私有属性
#
#
# class Dog(Aniamal):
# 	def bark(self):
# 		print('---汪汪汪汪---')
# 		# self.__run()  # 父类中调用私有方法,没有被子类继承
# 		print(self.num1)
# 		# print(self.__num2)  # 父类中的私有属性,没有被子类继承
#
#
# wang_cai = Dog()
# wang_cai.bark()
# wang_cai.test()  # 通过其他方法来调用获取父类的私有属性


"""多继承:

多继承:子类有多个父类并且具有它们的特征

格式:

# 定义一个父类
class A:
	def printA(self):
		print('---A---')


# 定义一个父类
class B:
	def printB(self):
		print('---B---')


# 定义一个父类,继承自A.B(就是从A和B继承来)
class C(A,B):
	def printC(self):
		print('---C---')


obj_C = C()  # 创建一个对象
obj_C.printA()  # 调用父类A的方法
obj_C.printB()  #调用父类B的方法



说明:1.python中是可以多继承的 2.父类中的方法,属性,子类会继承




"""

# class base(object):
# 	def test(self):
# 		print('---base test---')
#
#
# class A(base):
# 	def test(self):
# 		print('---A test---')
#
#
# # 定义一个父类
# class B(base):
# 	def test(self):
# 		print('---B test---')
#
#
# # 定义一个父类,继承自A.B(就是从A和B继承来)
# class C(A, B):
# 	pass
#
#
# obj_C = C()  # 创建一个对象
# obj_C.test()
#
# print(C.mro())  # 可以查看C类对象搜索方法时的先后顺序


"""多态:

多态:应用于Java 和C#这一类强类型语言中,而Python崇尚 '鸭子类型'

多态:定义时的类型和运行时的类型不一样,此时就成为多态




"""

# class F1():
# 	def show(self):
# 		print('F1.show')
#
#
# class S1(F1):
# 	def show(self):
# 		print('S1.show')
#
#
# class S2(F1):
# 	def show(self):
# 		print('S2.show')
#
#
# def Func(F1):
# 	"""Func函数需要接收一个F1类型或者F1子类的类型"""
#
# 	print(F1.show())
#
#
# s1_obj = S1()
# Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj,执行S1的show方法,结果:S1.show
#
# s2_obj = S2()
# Func(s2_obj)  # 在Func函数中传入S2类的对象 s2_obj,执行S2的show方法,结果:S2.show
# 输出结果:
# S1.show
# None
# S2.show
# None



"""Python '鸭子类型'

鸭子类型语言中,函数/方法可以接受一个任意类型的对象作为参数/返回值,只要该对象实现了代码后续用到定位属性和方法就不会报错




"""

# class F1():
# 	def show(self):
# 		print('F1.show')
#
#
# class S1(F1):
# 	def show(self):
# 		print('S1.show')
#
#
# class S2(F1):
# 	def show(self):
# 		print('S2.show')
#
#
# def Func(F1):
# 	"""Func函数需要接收一个F1类型或者F1子类的类型"""
#
# 	print(F1.show())
#
#
# s1_obj = S1()
# Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj,执行S1的show方法,结果:S1.show
#
# s2_obj = S2()
# Func(s2_obj)  # 在Func函数中传入S2类的对象 s2_obj,执行S2的show方法,结果:S2.show



"""实例属性.类属性
实例属性:通过类创建的对象 又称为 实例对象,对象属性 又称为 实例属性 ,记录对象各自的数据,不同对象的同名实例属性,记录的数据可能各不相同

类属性:
	1.类属性就是类对象所拥有的属性,它被该类的所有实例对象 所共有
	2.类属性可以使用 类对象 或 实例对象访问

在Python 中'万物皆对象',类本身也是一个对象,执行class语句时候会被创建,称为 类对象

使用场景:
	1.类的实例 记录的某项数据 始终保持一致时,则定义类属性
	2.实例属性 要求 每个对象 为其单独开辟一份内存空间来记录数据,而类属性为全类所共有,仅占用一份内存,更加节省内存空间

注意点:
1>尽量避免类属性和对象属性同名.如果有同名对象属性,实例对象会优先访问对象属性

2>类属性只能通过类对象修改,不能通过实例对象修改

3>类属性 也可以设置为私有,前边添加两个__下划线.

"""

# class Dog:
# 	type = '狗'  # 类属性
#
#
# dog1 = Dog()
# dog1.name = '旺财'
#
# dog2 = Dog()
# dog2.name = '来福'
#
# # 类属性 取值
# print(Dog.type)  # 结果:狗
# print(dog1.type)  # 结果:狗
# print(dog2.type)  # 结果:狗


# class Dog(object):
# 	type = '狗'  # 类属性
#
# 	def __init__(self):
# 		self.type = 'dog'  # 对象属性
#
#
# # 创建对象
# dog1 = Dog()
#
# print(Dog.type)  # 狗 使用类对象访问类属性
# print(dog1.type)  # dog 类属性和对象属性同名, 使用实例对象 访问的是对象属性


# class Dog(object):
# 	type = '狗'  # 类属性
#
# 	def __init__(self):
# 		self.type = 'dog'  # 对象属性
#
#
# # 创建对象
# dog1 = Dog()
# Dog.type = 'Dog'  # 使用类对象 修改类属性
# dog1.type = 'dog'  # 使用实例对象 创建了对象属性type
# print(Dog.type)  # Dog 使用类对象访问类属性
# print(dog1.type)  # dog 类属性和对象属性同名, 使用实例对象 访问的是对象属性
#

# class Dog(object):
# 	count = 100  # 公有的类属性
# 	__type = '狗'  # 私有的类属性
#
#
# print(Dog.count)
# print(Dog.__type)  # 私有,无法访问 报错: AttributeError: type object 'Dog' has no attribute '__type'

"""类方法.静态方法
1.类方法:类对象所拥有的方法
需要使用装饰器@classmethod 来来标识其为类方法,对于类方法,第一个参数必须是类对象
,一般以cls作为第一个参数

使用场景:
	1.当类方法中 需要使用类对象(如访问私有类属性等)时,定义类方法
	2.类方法一般和类属性配合使用


"""
# class Dog(object):
# 	__type = '狗'  # 私有属性
#
# 	# 类方法,用classmethod来进行修饰
# 	@classmethod
# 	def get_type(cls):
# 		return cls.__type
#
# print(Dog.get_type())


"""静态方法:

需要通过装饰器@staticmethod 来进行修饰,静态方法既不需要传递类对象也不需要传递实例对象(形参没有self/cls)

静态方法 也能够通过 实例对象和 类对象 去访问

使用场景:当方法中 既不需要使用实例对象(如实例对象,实例属性),也不需要使用类对象
(如类属性,类方法,创建实例等)时,定义静态方法

取消不需要的参数传递,有利于 减少不必要的内存占用和性能消耗

注意点: 类再定义了同名的对象方法,类方法,静态方法时,调用方法会 优先执行 最后定义的 方法

"""

# class Dog(object):
# 	type = '狗'
#
# 	def __init__(self):
# 		name = None
#
# 	# 静态方法
# 	@staticmethod
# 	def introduce():  # 静态方法不会自动传递实例对象和类对象
# 		print('犬科哺乳动物,属于食肉目...')
#
#
# dog1 = Dog()
# Dog.introduce()  # 可以用 类对象 来调用静态方法
# dog1.introduce()  # 可以用 实例对象 来调用静态方法

# class Dog:
# 	def demo_method(self):
# 		print('对象方法')

# 	@classmethod
# 	def demo_method(cls):
# 		print('类方法')

# 	@staticmethod
# 	def demo_method():  # 被最后定义,调用时优先执行
# 		print('静态方法')

# dog1 = Dog()
# Dog.demo_method()  # 类对象 结果:静态方法
# dog1.demo_method()  # 实例对象 结果:静态方法


"""__new__方法

创建对象时,系统会自动调用new方法
开发者可以实现new方法来 自定义对象的创建过程

"""

# class Cat:
# 	def __new__(cls, name):
# 		print('创建对象')
# 		return object.__new__(cls)
#
# 	def __init__(self, name):
# 		print('对象初始化')
# 		self.name = name
#
# 	def __str__(self):
# 		return "%s" % self.name
#
#
# lanmao = Cat('蓝猫')
# lanmao.age = 20
# print(lanmao)

"""单例模式:

1.确保某一个类只会创建出一个实例,这个类称为单例类,单例模式是一种对象创建型
模式

2.创建单例-保证只有一个对象

3.创建单例时,只执行1次__init__方法



"""

# 实例化 一个 单例
# class Singleton:
# 	__instance = None  # 保存创建者首次创建的对象
#
# 	def __new__(cls):
# 		if cls.__instance is None:
# 			print('创建对象')
# 			cls.__instance = super().__new__(cls)
#
# 		return cls.__instance
#
#
# s1 = Singleton()
# print(s1)
# s2 = Singleton()
# print(s2)
# 输出:
# <__main__.Singleton object at 0x000002297D70A128>
# <__main__.Singleton object at 0x000002297D70A128>


# class Singleton:
# 	__instance = None  # 保存创建者首次创建的对象
# 	__has_init = False  # 记录是否已经初始化
#
# 	def __new__(cls):
# 		if cls.__instance is None:
# 			print('创建对象')
# 			cls.__instance = super().__new__(cls)
#
# 		return cls.__instance
#
# 	def __init__(self):
# 		if not self.__has_init:
# 			print('对象初始化')
# 			self.type = '猫'
# 			self.__has_init = True
#
#
# s1 = Singleton()
# s1.type = '动漫人物'
# print(s1.type)
# s2 = Singleton()
# print(s2.type)


"""模块导入:

Python 中的模块:模块就好比是工具包,要想使用这个工具包(就好比是函数),就需要导入这个模块

import:当解释器在遇到import语句,如果模块在当前的搜索路径就会被导入

在调用math模块中的函数时,就必须这样引用:
模块名.函数名


想一想:

为什么必须加上模块名调用呢？

答:

因为可能存在这样一种情况：在多个模块中含有相同名称的函数，此时如果只是通过函数名来调用，解释器无法知道到底要调用哪个函数。所以如果像上述这样引入模块的时候，调用函数必须加上模块名


from ... import:

有时候我们只需要用到模块中的某个函数,只需要引入该函数即可.此时可以用下面方法实现:
		from modname import name1[, name2[, ... nameN]]

例如 ,需要导入 模块fib的fibonacci函数,使用如下语句:
		from fib import fibonacci


不仅可以引入函数,还可以引入一些全局变量,类等
这种方式引入时,直接使用函数名调用,但是当两个模块中含有相同名称函数的时候,后面一次引入会覆盖前面一次引入

如果想一次性引入math中所有的东西,还可以通过from math import * 来实现

模块中的__all__:在文件中设置__all__变量,可以限定通过 from xxx import * 导入时的内容


定位模块:
当你导入一个模块,Python解释器对模块位置的搜索顺序是:
	1>当前目录
	2>如果不在当前目录,Python则搜索在shell变量PYTHONPATH下的每个目录.
	3>如果都找不到,Python会察看默认路径UNIX下,默认路径一般为/usr/local/python/
	4>模块搜索路径存储在system模块的sys.path变量中.变量里包含当前目录,
	PYTHONPATH 和 由安装过程决定的 默认目录.

"""

"""模块制作:

在Python中,每个python文件都可以作为一个模块,模块的名字就是文件的名字.比如有这样一个文件test.py,在test.py中定义了函数add


2>调用自己定义的模块
	那么在其他文件中就可以先import test,然后通过test.add(a,b) 来调用了,当然也可以通过from test import add来引入

3>测试模块:在实际开发中,当一个开发人员编写完一个模块后,为了让模块能够在项目中达到想要的效果,这个开发人员会自行在py文件中添加一些测试信息,例如:


总结:可以根据__name__变量的结果能够判断出,是直接执行的,Python脚本还是被引入执行的,从而能够有选择性的执行测试代码


"""

"""Python中的包:

有2个模块功能有些联系,可以将其放到同一个文件夹下

要组成包,还需要在该文件夹中创建init.py文件

总结:包将有联系的模块组织在一起,即放到同一个文件夹下,并且在这个文件夹创建一个名字为init.py文件,那么这个文件夹就称之为包

有效避免模块名称冲突问题,让应用组织结构更加清晰.


"""

"""异常:

<1>异常简介:当Python检测到一个错误时,解释器就无法继续执行了,反而出现了一些错误的提示,这,就是所谓的'异常'.

捕获异常:

说明:此程序看不到任何错误,因为用except捕获到了IOError异常,并添加了处理的方法

pass表示实现了相应的实现,但什么也不管,如果把pass改为print语句,那么就会输出其他信息


<2>except捕获多个异常:

注意:当捕获多个异常时,可以把要捕获的异常的名字,放到except后,并使用元组的方式仅进行存储
"""
# try:
# 	print('---test--1----')
# 	open('123.txt', 'r')
# 	print('---test--2---')
# except IOError:
# 	print('错误')


# try:
# 	print(num)
# except NameError:
# 	print('产生错误了')

# try:
# 	print('---test--1----')
# 	open('123.txt','r')  #如果123.txt文件不存在,那么产生IOError异常
# 	print('---test--2----')
# 	print(num)  # 如果num变量没有定义,那么会产生NameError异常
#
# # 如果想通过一次except捕获到多个异常可以用一个元组的方式
# except(IOError,NameError):
# 	pass

"""result:存储异常的基本信息

NameError:要捕获的异常
"""
# try:
# 	print(a)
# except NameError as result:
# 	print(result)


# 获取异常的信息描述
# try:
# 	open('123.txt')
# except (NameError,IOError) as result:
# 	print('哈哈,捕获到了异常')
# 	print('异常的基本信息是:',result)

# 捕获所有异常,没有存储异常的基本信息
# try:
# 	open('a.txt')
# except:
# 	print('产生了一个异常')


# 捕获所有异常,并且存储异常的基本信息
# try:
# 	open('a.txt')
# except Exception as result:
# 	print('捕获到了异常')
# 	print(result)

"""else:

try...except...:如果没有捕获到异常,那么就执行else中的事情

try...finally...:在程序中,如果一个段代码必须要执行,即无论异常是否产生都要执行,那么此时就需要使用finally.比如文件关闭,释放锁,把数据库连接返还给连接池等

"""
# try:
# 	num = 10
# 	print(num)
# except NameError as errorMsg:
# 	print('产生错误了:%s' % errorMsg)
# else:
# 	print('没有捕获到异常,真高兴')
# import time
#
# try:
# 	f = open('tree.txt')
# 	try:
# 		while True:
# 			content = f.readline()
# 			if len(content) == 0:
# 				break
# 			time.sleep(2)
# 			print(content)
# 	except:
# 		# 如果在读取文件的过程中,产生了异常,那么就会捕捉到
# 		# 比如按下了ctrl + c
# 		pass
# 	finally:
# 		f.close()
# 		print('关闭文件')
# except:
# 	print('没有这个文件')

"""异常的传递:

1>.try嵌套:try嵌套时,如果里面的try没有捕获到这个异常,那么外面的try会接收到这个异常,然后进行处理,如果外边的try依然没有捕捉到,那么再进行传递

2>.函数嵌套调用中

"""

# import time
#
# try:
# 	f = open('test.txt')
# 	try:
# 		while True:
# 			content = f.readline()
# 			if len(content) == 0:
# 				break
# 			time.sleep(2)
# 			print(content)
# 	finally:
# 		f.close()
# 		print('关闭文件')
#
# except:
# 	print('没有这个文件')


# def test1():
# 	print('--test1-1---')
# 	print(num)
# 	print('--test1-2---')
#
#
# def test2():
# 	try:
# 		print('---test2-1----')
# 		test1()
# 		print('---test2-2-----')
# 	except:
# 		print('test2出现异常')
#
# 	print('---test2-3----')
#
# test2()
# print('------华丽的分割线--------')
"""总结:
如果try异常,那么如果里面的try没有捕获到这个异常那么外面的 try 会接收到这个异常,然后进行处理.如果外边的try依然没有捕获到,那么再进行传递.

如果一个异常是在一个函数中产生的,例如 函数A-->函数B--->函数C,而异常是在函数C中产生的,那么如果函数C中没有对这个异常进行处理,那么这个异常会传递到函数B中,如果函数B也没有处理,那么这个异常会继续传递,以此列推...,如果所有的函数都没有处理,那么此时就会进行异常的默认处理,即通常见到的那样报错.

注意观察上图中,当调用test2函数时,在test1函数内部产生了异常,此异常被传递到test2函数中完成了异常处理,而当异常处理完毕后,并没有返回到函数test1中进行执行,
而是在函数test2中继续执行


"""

"""抛出自定义异常:


可以用raise语句来引发一个异常.异常/错误对象必须有一个名字,且它们应是Error或Exception类的子类.



"""

# class ShortInputException(Exception):
# 	"""自定义的异常类"""

# 	def __init__(self, length, atleast):
# 		self.length = length
# 		self.atleast = atleast


# def main():
# 	try:
# 		s = input('请输入:')
# 		if len(s) < 3:
# 			raise ShortInputException(len(s), 3) # raise引发一个自己定义的异常

# 	except ShortInputException as result:  # 这个变量被绑定到了错误的实例

# 		print('ShortInputException:输入的长度是 %d,长度至少应该是:%d' % (result.length, result.atleast))
# 	else:
# 		print('没有异常发生')


# main()


"""闭包:函数引用

内部函数对外部函数作用域里变量的引用(非全局变量),则称内部函数为闭包



"""

# def test1():
# 	print('----- in test1 func------')
# # 调用函数
# test1()


# #引用函数
# ret = test1

# print(id(ret))
# print(id(test1))

# #通过引用调用函数
# ret()


# 定义一个函数
# def test(number):
# 	#在函数内部再定义一个函数,并且这个函数用到了外边函数的变量,那么将这个
# 	def test_in(number_in):
# 		print('in test_in函数,number_in is %d' % number_in)
# 		return number + number_in
# 	return test_in

# # 给test 函数赋值,
# ret = test(20)
# # print(ret)
# print(ret(200))
#
# def counter(start = 0):
# 	count = [start]
# 	def incr():
# 		count[0] += 1
# 		return count[0]
# 	return incr

# from tkinter import *
# from StillClock import StillClock
#
# class DisplayClock(object):
# 	"""docstring for DisplayClock"""
# 	def __init__(self):
# 		window = Tk()
# 		window.title('Change Clock Time')
#
# 		self.clock = StillClock(window)
# 		self.clock.pack()
#
# 		frame = Frame(window)
# 		frame.pack()
#
# 		Label(frame,text = 'Hour:').pack(side = LEFT)
# 		self.hour = IntVar()
# 		self.hour.set(self.clock.getHour())
#
# 		Entry(frame,textvariable = self.hour,width = 2).pack(side=LEFT)
#
# 		Label(frame,text = 'Minute:').pack(side = LEFT)
# 		self.minute = IntVar()
# 		self.minute.set(self.clock.getMinute())
#
# 		Entry(frame,textvariable = self.minute,width = 2).pack(side=LEFT)
#
# 		Label(frame,text = 'Second:').pack(side = LEFT)
# 		self.second = IntVar()
# 		self.second.set(self.clock.getSecond())
#
# 		Entry(frame,textvariable = self.second,width = 2).pack(side=LEFT)
#
# 		Button(frame,text = 'Set New Time',command = self.setNewTime).pack(side = LEFT)
#
# 		window.mainloop()
#
#
# 	def setNewTime(self):
# 		self.clock.setHour(self.hour.get())
# 		self.clock.setMinute(self.minute.get())
# 		self.clock.setSecond(self.second.get())
#
# DisplayClock()


"""反恐精英:"""


class Gun:
	"""枪类"""

	def __init__(self, model, damage):
		self.model = model  # 型号
		self.damage = damage  # 伤害
		self.bullet_count = 20  # 子弹数量

	def add_bullet(self, count):
		"""添加子弹"""
		self.bullet_count += count

	def shoot(self, enemy):
		"""射击"""
		if self.bullet_count == 0:
			print('子弹为0,无法射击')
		else:
			self.bullet_count -= 1
		# TODO 让敌人受伤
		enemy.hurt(self)

	def __str__(self):
		return '型号:%s,伤害:%d,子弹数量:%d' % (self.model, self.damage, self.bullet_count)


# ak47 = Gun('ak47',40)
# print(ak47)
#
# ak47.add_bullet(89)
# print(ak47)
#
# ak47.shoot(14)
# print(ak47)

# class Player:
# 	"""玩家类"""
#
# 	def __init__(self, name):
# 		self.name = name  # 角色
# 		self.hp = 100  # 血量
# 		self.gun = None  # 枪
# 		self.state = '生'  # 人的状态
#
# 	def fire(self, enemy):
# 		"""开火"""
# 		if self.gun is None:  # 没有枪提示
# 			print('没有枪,用眼神交流')
# 		elif self.gun.bullet_count > 0:  # 如果有子弹就射击
# 			self.gun.shoot(enemy)
# 		else:  # 如果没有子弹就自动添加子弹
# 			self.gun.add_bullet(20)
#
# 	def hurt(self, enemy_gun):
# 		"""受害"""
# 		# 自己受的伤害就是对方枪的伤害
# 		self.hp -= enemy_gun.damage
# 		if self.hp > 0:
# 			print('%s受伤了,当前血量为%d' % (self.name, self.hp))
# 		else:
# 			self.state = '死亡'
# 			self.hp = 0
# 			print('%s 已经死亡' % self.name)
#
# 	def __str__(self):
# 		return '%s角色,当前状态:%s,当前血量[%d],枪支信息:{%s}' % (self.name, self.state, self.hp, self.hp)
#
#
# ak47 = Gun('ak47', 40)
# policeman = Player('警察')
# print(policeman)
# policeman.gun = ak47
# print(policeman)
#
# m1 = Gun('m1', 20)
# badman = Player('匪徒')
# badman.gun = m1
#
# print(badman)
# print('***')
#
# for _ in range(3):
# 	policeman.fire(badman)
# 	badman.fire(policeman)
# 	print(policeman)
# 	print(badman)

"""fork()"""

# import os
#
# pid = os.fork()
# if pid == 0:
# 	print('121')
# else:
# 	print('565')

"""multiprocessing"""

# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
# 	print('子进程运行中,name = %s,pid = %d...') % (name, os.getpid())
#
#
# if __name__ == '__main__':
# 	print('父进程%d' % os.getpid())
# 	p = Process(target=run_proc, args=('test',))
# 	print('子进程将要执行')
# 	p.start()
# 	p.join()
# 	print('子进程已结束')
