# class Dog:
#     """定义狗类"""

#     def __init__(self,name):  # 初始化方法,就是给属性赋值
#         self.name = name  # self.name 就是一个变量,是属性.后面的name 才是形参,是给调用的时候的实参进行占位和传递数据的作用.
#         self.age = 14

#     def drink(self):
#         # print(self)

#         print('%s喝点酒' % (self.name))

# # dog1 = Dog()  # 创建一个对象
# # print(dog1)  # 就是一个地址
# # dog1.drink()  # 对象调用类的方法
# #
# # dog1.name = '老黄'  # 定义对象的属性
# # print(dog1)  # <__main__.Dog object at 0x000001BFC2856438>
# # dog1.age = 89
# # print(dog1.age)
# dog2 = Dog('小晓')  # 又一个新的对象2
# # dog2.name = '小黑'
# # dog2.drink()
# print(dog2.name)  # <__main__.Dog object at 0x000001BFC2856438>
# print(dog2.age)
# # 说明每次创建出来的对象内存地址都不一样,不是同一个对象
#
#
# 列表推导式:
# list1 = [x**2 for x in range(9)]
# print(list1)
#
# 集合推导式:
# set1 = {x for x in range(9)}
# print(set1)
#
# 字典推导式:
# dict2 = {'a':1,'b':2,'c':3}
# dict1 = {key:value for key,value in dict2.items()}
# print(dict1)
#
# import os

# print(os.sys.getsizeof('op'))
#
# 匿名函数:lambda  就是没有名字的函数  记得给实际参数

# f = lambda x : x + 2
# f1= f(3)
# print(f1)
#
#  实际起到的作用就是当作参数进行数据的传递了
# f = lambda a,b,c : a - b * c
# f1 = f(8,1,6)
# print(f1
#
# 递归函数:函数自己调用自己,千万要记得在函数调用的过程中能够给一个初始值
# 9 的阶乘:
#
# def jiecheng(num):
#     if num == 1:
#         return 1
#     else:
#         result = num * jiecheng(num - 1)
#         return result

# result = jiecheng(0)
# print(result)
#
# f = open('we.txt','r')

# f.write('159753')
# print(f.read())

# f.close()
#
# with open('we.txt','r+') as f:
#     while True:
#         c = f.readline()  # 单行输出
#         print(c,end='') # 删掉默认的换行符
#         if len(c) == 0:
#             break
#
# oldf = input('输入需要备份的文件:')

# index = oldf.rfind('.')  # 找到.所在的索引位置,目的是为了文件后缀的名字
# newf = oldf[:index] +'副本'+ oldf[index:]

# with open(oldf,'r') as f1:
#     with open(newf,'w') as f2:
#         file = f1.read()
#         f2.write(file)
#
# import os

# os.rename('we.txt','we1.txt')
# print(os.getcwd())

# os.mkdir('demo')
# os.rmdir('demo')
# os.chdir('张飒')
# print(os.getcwd())


# print(os.listdir())

# with open('we1.txt','r+') as f:
#     print(f.tell())
#     f.write('hello')
#     print(f.tell())

#     f.seek(3,0)
#     c = f.read()
#     print(c)
#
#
# 给列表元素排序,在不影响元素的位置前提下
# list1 = [2,5,3,1,4,5,6,78,89,9,9]
# list2 = []
# for ele in list1:
#     if ele not in list2:
#         list2.append(ele)

# print(list2)

# 列表推导式:

# list1 = ['555' for i in range (5)]  # 只是让一个字符串出现5次
# print(list1)
#
# list1 = [i for i in range(15) if i % 2 == 0]
# print(list1)

# def func2(*args,a=10):
#     print(args)
#     print(a)

# func2(1,2,3,a = 89)

# def func1(*args,a = 20,**kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# func1(12,'mk',a = 100,b = 'etree',a1 = 56)
# 100
# (12, 'mk')
# {'b': 'etree'}
#
# def func1(b,a):
#     print(b)
#     print(a)

# dict1 = {'m':56,'n':29}
# dict2 = {'a':59,'b':58}


# func1(*dict2)
# func1(**dict2)  # 加一个*是解包输出key的值,加两个*是输出key对应的value的值

# 现在先看到第六天的04-组包拆包了
#
# list1 = [1,2,3,4,5,5]
# set1 = set(list1)

# print(set1)
#
#
# 属性方法
#
#
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     @property
#     def eat(self):
#         print('%s is eating' % self.name)

# dog1 = Dog('大侠')
# print(dog1.name)

# dog1.eat()
# TypeError: 'NoneType' object is not callable.就是这个方法没法调用.因为eat此时已经变成一个静态属性了， 不是方法了， 想调用已经不需要加()号了，直接d.eat就可以了
#
"""

装饰器:装饰器是函数,只不过这个函数可以具有特殊的含义,装饰器用来装饰函数或类,使用装饰器可以在函数执行前和执行后添加相应操作.

"""
# def wrapper(func):
#     def result():
#         print('before')
#         func()
#         print('after')
#     return result
# @wrapper
#
# def foo():
#     print('foo')
#
# foo()

"""冒泡排序法:"""
# li = [13, 2, 6, 9, 11]
"""for拆分开:"""
# for m in range(4):  # 不能到5,需要保证有m+1 的存在
# 	if li[m] > li[m + 1]:
# 		temp = li[m + 1]
# 		li[m + 1] = li[m]
# 		li[m] = temp
# print(li)
# for m in range(3):
# 	if li[m] > li[m + 1]:
# 		temp = li[m + 1]
# 		li[m + 1] = li[m]
# 		li[m] = temp
# print(li)
# for m in range(2):
# 	if li[m] > li[m + 1]:
# 		temp = li[m + 1]
# 		li[m + 1] = li[m]
# 		li[m] = temp
# print(li)
# for循环嵌套,外面的控制 2-4,里面的控制比较大小
"""for嵌套:"""
# for i in range(4, 1, -1):
# 	print(i)
# 	for j in range(i):
# 		if li[j] > li[j + 1]:
# 			temp = li[j + 1]
# 			li[j + 1] = li[j]
# 			li[j] = temp
# print(li)

"""函数式:"""

# def caocong(name, gender, age, fight_num, cost=200):
# 	print('姓名:%s,性别:%s,年龄:%d,初始战斗力:%d,消耗:%d,剩余战斗力:%d' %
# 		  (name, gender, age, fight_num, cost,fight_num - cost))
#
#
# def xiulian(name, gender, age, fight_num, add=100):
# 	print('姓名:%s,性别:%s,年龄:%d,初始战斗力:%d,增加:%d,剩余战斗力:%d' %
# 		  (name, gender, age, fight_num, add,fight_num + add))
#
#
# def duoren(name, gender, age, fight_num, cost=500):
# 	print('姓名:%s,性别:%s,年龄:%d,初始战斗力:%d,消耗:%d,剩余战斗力:%d' %
# 		  (name, gender, age, fight_num, cost,fight_num - cost))
#

# caocong('苍井井', '女', 18, 1000)
# xiulian('苍井井', '女', 18, 1000)
# duoren('苍井井', '女', 18, 1000)
# print('-'*30)
# caocong('东尼木木', '男', 20, 1800)
# xiulian('东尼木木', '男', 20, 1800)
# duoren('东尼木木', '男', 20, 1800)
# print('-'*30)
# caocong('波多多', '女', 19, 2500)
# xiulian('波多多', '女', 19, 2500)
# duoren('波多多', '女', 19, 2500)

"""面向对象:"""

# class Role:
# 	"""角色类"""
#
# 	def __init__(self, name, gender, age, first_fight):
# 		self.name = name
# 		self.gender = gender
# 		self.age = age
# 		self.first_fight = first_fight
#
# 	def caocong(self):
# 		self.first_fight -= 200
# 		return self.first_fight
#
# 	def xiulian(self):
# 		self.first_fight += 100
# 		return self.first_fight
#
# 	def duoren(self):
# 		self.first_fight -= 500
# 		return self.first_fight
#
# 	def __str__(self):
# 		return '姓名:%s,性别:%s,年龄:%d,战斗力:%d' % (self.name, self.gender, self.age, self.first_fight)
#
#
# role1 = Role('苍井井', '女', 18, 1000)
# role2 = Role('东尼木木', '男', 20, 1800)
# role3 = Role('波多多', '女', 19, 2500)
#
# print(role1)
# print(role2)
# print(role3)
#
# print(role1.caocong())
# role2.caocong()
# role3.caocong()
#
# print(role1.xiulian())
# role2.xiulian()
# role3.xiulian()
#
# print(role1.duoren())
# role2.duoren()
# role3.duoren()
#
# print(role1)
# print(role2)
# print(role3)

"""__doc__:描述类的信息"""

# class Dog:
# 	"""这是一个狗类"""
#
# 	def __init__(self):
# 		print('你大爷,初始化了')
#
# 	def __call__(self):  # 对象后面加()才会触发执行
# 		print('-*-*-')
#
#
# # print(Dog.__doc__)  # 这是一个狗类
#
# dog2 = Dog()
# dog2()  # 对象后面加()才会触发执行__call__方法.
#
# print(Dog.__dict__)

# print(type(Dog))  # <class 'type'>,说明Dog类是由type类创建生成的.


"""类是由type类产生的.

类中有一个属性__metaclass__,其用来表示 这个类 是由 谁 来创建的,所以,我们可以为__metaclass__设置一个type的派生类(就是子类),从而查看 类 创建的过程.


"""

# class My_type(type):
# 	def __init__(self, what, bases=None, dict=None):
# 		super(My_type, self).__init__(what, bases, dict)
#
# 	def __call__(self, *args, **kwargs):
# 		obj = self.__new__(self, *args, **kwargs)
#
# 		self.__init__(obj)
#
#
# class Fun(object):
# 	__metaclass__ = My_type
#
# 	def __init__(self, name):
# 		self.name = name
#
# 	def __new__(cls, *args, **kwargs):
# 		return object.__new__(cls)
#
#
# obj = Fun('name')
# print(obj)
#
# 私有属性:
# class Dog:
#     def __init__(self):
#         self.__age = None

#     def set_age(self,age):
#         if age >= 0 and age <= 20:
#             self.__age = age
#             # return self.__age
#         else:
#             print('数据不满足')
#     def get_age(self):

#         return self.__age

#     def __info(self):  # 私有方法
#         print('这是一个私有方法,外部无法直接调用')

#     def drink(self):
#         self.__info() # 通过普通方法调用私有方法

# dog1 = Dog()  # 创建一个实例对象

# dog1.set_age(16)  # 设置私有属性 年龄

# print(dog1.get_age())  # 获取并打印输出设置的私有属性的年龄值

# # dog1.__info()  # 私有方法无法调用,报错AttributeError: 'Dog' object has no attribute '__info'

# dog1.drink()  # 通过普通方法来调用返回私有方法的值


# del方法:
#
#
# class Dog:
#     def __init__(self):
#         self.name = '大爷啊'

#     def __del__(self):
#         print('这个对象要死了啊!!!')


# dog1 = Dog()  # 创建一个实例对象dog1
# del dog1
# print(dog1.name) # 获取dog1的name属性
#
#
# 类的继承:
# class Dog:
#     def __init__(self):
#         self.name = '大华'
#         self.__name = '海康'
#         self.age = 89
#         self.__age = 56
#         self.gender = '男'
#     def drink(self):
#         print('喝水!!!')
#     def eat(self):
#         print('吃点肉!!')
#     def __eat(self):
#         print('私有的,不分享')
#     def get_eat(self):
#         return self.__eat()
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age


# class XTQ(Dog):  # 只要这么写就可以直接调用父类中的属性和方法.但是记住能被调用的只能是公有的属性和方法,私有的方法和属性除外.
#     pass

# xtq = XTQ()
# xtq.drink()
# xtq.eat()

# print(xtq.name)
# print(xtq.age)
# print(xtq.gender)

# print(xtq.get_name())  # 通过普通方法来访问父类私有属性
# print(xtq.get_age())  # 普通方法访问父类私有属性
# xtq.get_eat()  # 普通方法访问父类私有方法

# 重写父类方法:继承父类之后,某些同名属性的值需要自定义.
#
# class Dog:
#     def __init__(self):
#         self.name = '玩去吧'
#         self.age = 15

#     def drink(self):
#         print('喝点水')
#     def eat(self):
#         print('吃点肉!!!')
# class XTQ(Dog):
#     # 父类的方法这时候无法满足子类的需求了
#     # def __init__(self):
#     #     pass# self.age = 56
#     def eat(self):
#         print('吃点馒头')


# xtq = XTQ()
# # xtq.age = 89
# xtq.eat()  # 调用子类自定义的方法
# xtq.drink()  # 调用继承的父类方法
# print(xtq.name)  # 调用继承的父类属性
# print(xtq.age)
#
# 调用被重写的父类方法:
# 当父类的方法无法满足子类的需求,就在子类中重写父类的方法.但是,如果重写之后又需要调用父类没有重写之前的方法,就需要手动调用了.
#
# 方式1:父类名.重写方法(self)  注意需要手动传递self
# 方式2:super(当前类名,self).重写方法()
#
#
# class Dog:
#     def drink(self):
#         print('喝点白开水')
#     def eat(self):
#         print('吃肉啊啊')

# class XTQ(Dog):
#     def drink(self):
#         print('喝点酒吧!')

#         # 1.Dog.drink(self)  # 使用方式1调用被重写的方法,self手动传,这里是子类XTQ产生的实例对象xtq
#         # 2.super().drink() 方式2 调用

# xtq = XTQ()
# # xtq.super(XTQ,self).drink()  # 外部无法这么写,会报错
# Dog.drink(xtq)  # 类外部调用的时候这么写,需要手动指明self是谁,这里是xtq这个子类的实例对象

# 多继承:
# class Dog:
#     def eat(self):
#         print('吃肉')
#     def drink(self):
#         print('喝酒')

# class God:
#     def fly(self):
#         print('飞吧!!!')
#     def eat(self):
#         print('吃点仙丹')

# class XTQ(God,Dog):
#     def eat(self):
#         # print('到底要吃啥?')
#         # super(God,self).eat()  # 多继承的时候比较乱,不要这么写
#         # God.eat(self)
#         Dog.eat(self)  # 多继承的时候建议这么写,父类名 + 方法名 + 手动传的self.能够看清楚到底是调用了哪个父类的.


# xtq = XTQ()
# xtq.eat()
# xtq.drink()
# xtq.fly()
#
#
#
# __str__: 方法 返回字符串
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):  # 自定义返回值
#         return '%s' % self.name


# dog1 = Dog('小花')
# print(dog1)  # 如果将str()方法注释掉,把对象名放在print()中输出的时候,输出的是对象在内存中的地址.
#
#
# 大文件读取:需要一点一点的去读取,读取完就释放掉内存
# with open('csdn1.txt') as f:  # 不写打开模式,默认是只读方式
#     while True:
#         content = f.readline()  # 不加s的是一次只读一行,遇到\n换行符就停止
#         print(content,end='')  # 输出读取的内容

#         # 判断读取结束的位置,如果content没有内容了,停止读取
#         if len(content) == 0:
#             break
#
# 文件备份:  sublime报错:EOFError: EOF when reading a line
# old_file = input('输入需要备份的文件:')
# index = old_file.rfind('.')  # 找.分隔符索引位置
# new_file = old_file[:index] + '[副本]' + old_file[index:]

# with open(old_file,'r+') as of:
#     with open(new_file,'w') as nf:
#         file = of.read()
#         nf.write(file)
#
# 不影响原有的索引位置去重:
# list1 = [1,2,5,3,5,7,3,45,7]
# list2 = []
# for i in range(len(list1) -1 ):
#     if list1[i] not in list2:
#         list2.append(list1[i])
# print(list2)
#
# 参数混合使用:
# 形参:位置参数,默认参数,可变参数,字典类型的可变参数
# 实参:普通实参,关键字参数
# 定义的时候是形参,调用的时候是实参.记住.
# def func(a,*args):
#     print(a)  # 2
#     print(args)  # 输出一个元组(3, 4, 4, 5, 6, 89)

# func(2,3,4,4,5,6,89)


# 默认参数和可变参数混合使用,默认参数应该在可变参数的后面
# def func2(*args,a = 89):
#     print(args)  # (89, 4, 5, 6, 56, 9, 78)
#     print(a)  # 89
# func2(89,4,5,6,56,9,78)
#
# 字典类型的可变参数:
# 作用:字典类型可以接收任意数量的多余 关键字参数,并且把它包装成字典.
#
# def func1(*args,a = 20 ,**kwargs):
#     print(args)  # (1, 23, 3, 4.5)
#     print(a)  # 47
#     print(kwargs)  # {'b': 90, 'c': '0o', 'm': 8888}

# func1(1,23,3,4.5,a = 47,b = 90 ,c = '0o', m = 8888)
# 形参前面加*:组包成元组加**,组包成字典类型
#
#
# 实参前面加* 解包,加**解包成...
#
# list1 = [1,2,3,4]
# print(*list1)  # 1 2 3 4
# str1 = '565566'
# print(*str1)  # 5 6 5 5 6 6
# tuple1 = (1,2,3,4,5)
# print(*tuple1)  # 1 2 3 4 5
# set1 = {1,3,4,56,7,9}
# print(*set1)  # 1 3 4 7 9 56
# dict1 = {'1':111,'2':222,'3':333}
# print(*dict1)
# print(**dict1)
#
# def func2(**kwargs):
#     print(kwargs)
# def func3(**kwargs):
#     # print(kwargs)
#     func2(**kwargs)
# func3(**{'a':1,'b':2,'c':3})  #{'a': 1, 'b': 2, 'c': 3}

# 输出*:
# for i in range(1,6):
#     print('*'.center(i,(6-i)*' '))
#
#
# 多进程:
# from multiprocessing import Process
# import os
# from time import sleep
#
#
# # 子进程要执行的代码
# def run_proc(name, age, **kwargs):
# 	for i in range(10):
# 		print('子进程运行中,name = %s,age = %d, pid = %d...' % (name, age,os.getpid()))
# 		print(kwargs)
# 		sleep(0.5)
#
#
# # print(__name__)
#
# if __name__ == '__main__':
# 	print('父进程%d' % os.getpid())
# 	p = Process(target=run_proc, args=('test', 18), kwargs={'m': 20})
# 	print('子进程将要执行')
# 	p.start()
# 	sleep(1)
# 	p.terminate()
# 	p.join()
# 	print('子进程已经结束')

from multiprocessing import Process
import time
import os


# 两个子进程将会调用的两个方法
def worker_1(interval):
	print('worker_1,父进程(%d),当前进程(%s)' % (os.getppid(), os.getpid()))
	t_start = time.time()
	time.sleep(interval)  # 进程将会被挂起intervalmiao
	t_end = time.time()
	print('worker_1,执行时间为"%0.2f秒" ' % (t_end - t_start))


def worker_2(interval):
	print('worker_2,父进程(%d),当前进程(%s)' % (os.getppid(), os.getpid()))
	t_start = time.time()
	time.sleep(interval)  # 进程将会被挂起intervalmiao
	t_end = time.time()
	print('worker_1,执行时间为"%0.2f秒" ' % (t_end - t_start))


# 输出当前程序的ID
print('进程ID:%s' % os.getpid())

p1 = Process(target=worker_1, args=(2,))
p2 = Process(target=worker_2, name='dongGe', args=(1,))

p1.start()
p2.start()

print('p2.is alive = %s' % p2.is_alive())

# 输出p1和p2的进程别名和pid
print(' p1.name = %s' % p1.name)
print(' p1.pid = %s' % p1.pid)
print(' p2.name = %s' % p2.name)
print(' p2.pid = %s' % p2.pid)

p1.join()
print('p1.is_alive=%s' % p1.is_alive())