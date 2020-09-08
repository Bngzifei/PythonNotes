print('---------单例模式---------------')
"""
单例模式定义:具有该模式的类只能生成一个实例对象.


在python中认为一切皆对象(元类除外).类,函数都可以看做一个对象.
既然是对象就可以作为参数在函数中传递.


"""


def singleton(cls, *args, **kwargs):  # cls:可以传入一个类
	"""实现单例模式的装饰器"""
	instances = {}  # 字典,保存单例对象
	
	def get_instance(*args, **kwargs):  # 内层函数获得单例对象
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)  # 字典中没有这个单例对象就存进去
		return instances[cls]  # 返回单例
	
	return get_instance  # 本质就是返回产生的单例对象


@singleton  # 本质就是: Student = singleton(Student).最后是返回get_instance()函数的引用
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age


# 创建实例对象 stu   实质就是 stu = get_instance('jiang',25)
"""
此时可以看做Student = get_instance,创建实例对象时就是:
stu = get_instance("jiang",25),调用get_instance函数,先判断实例对象是否在
instances字典中,如果在,直接从字典中获取并返回.
如果不在执行instances[cls] = Student("jiang":25)
然后返回该实例对象,并赋值给stu变量.即stu = instances[cls]
下面创建三个不同的实例对象,可以看出其内存地址是一样的,
说明符合单例模式
"""
stu = Student("jiang", 25)
print(stu)

stu1 = Student("jiang1", 215)
print(stu)

stu2 = Student("jiang111", 15)
print(stu)

"""
可以看到:三个实例对象的地址都是一样的.
---------单例模式---------------
<__main__.Student object at 0x0000019FE05D5DD8>
<__main__.Student object at 0x0000019FE05D5DD8>
<__main__.Student object at 0x0000019FE05D5DD8>

"""
