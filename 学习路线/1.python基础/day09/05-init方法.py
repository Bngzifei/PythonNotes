# 多个对象(由同一个类产生)的属性同名且值都一样,这时就需要使用init()方法.

# class 定义属性和方法,增加代码的复用性  init()方法

"""
双下划线开头,双下划线结尾的方法都具有特殊含义,并且此方法在特定情况下会自动调用.(调用就是使用,执行的意思)Python解释器会自动调用,内部已经写好了.

把定义属性的方法写在init()方法里面,当然,也可以自己定义.只是需要自己去写调用方法

称之为魔法方法.也叫运算符重载方法

在创建对象时就会自动调用.
init()方法叫初始化 ,功能: 定义属性


在其他的语言中也有init()方法,就是进行属性赋值操作

类似手机或电脑在开机启动的时候进行的加载操作.可以简单理解为是一个程序正式运行前的准备工作.


"""
print('xxx')


class Dog:
	def __init__(self, name):  # 这里的name称为自定义参数.不要写死了这里加形参进行传参操作.如果不想让属性的初始值写死,可以给init加形参,通过参数的方式传递给属性
		self.type = '狗'
		self.name = name  # 自定义属性的初始值


# 先造对象,再调用init()方法init的实参应该在创建对象的类名后面的小括号中传递
dog1 = Dog('小花')  # 在创建的时候就会执行init()方法,同时注意init()方法有一个位置参数(形参),不能调用的时候不能为空,所以这里一定要记得给init()传一个参数'小花'
print(id(dog1.name))  # 2778225245504
print(id(dog1.type))  # 2240461703328 虽然id地址一样,但是仍然不一样
print(dog1.name)  # 小花
print(dog1)  # <__main__.Dog object at 0x0000025674A58978>
# 都有属性type,值一样,但是 不是同一个属性.只是属性名字一样而已.创建的时候代码会走两遍,每次创建一个对象就会执行一遍
dog2 = Dog('小黑')  # 小黑
print(dog2.name)  # 2240461703328
print(id(dog2.name))  # 2778225246032
print(id(dog2.type))  # 2240461703328 虽然id地址一样,但是仍然不一样


# 类中写属性,只能在init()方法中写
# 这里记住:虽然打印输出的id值一样(地址值),但实际上dog1.type和dog2.type不一样,是独立的两个.只是在Python解释器中为了运行效率,将同一个type的值进行了缓存
print('xxx')
