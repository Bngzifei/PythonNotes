print('-----单例模式---------')


class Singleton(object):
	
	_instance = None  # 先赋值空
	
	def __new__(cls, *args, **kwargs):
		"""重写__new__方法"""
		if cls._instance is None:  # 判断:为空就创建一个实例对象
			cls._instance = object.__new__(cls)  # 使用父类的__new__方法创建一个实例对象
			return cls._instance  # 返回实例
		else:
			return cls._instance  # 返回实例


stu = Singleton(25,"shdudhsv")
print(stu)
stu1 = Singleton(26,"dfhufdvh")
print(stu1)
stu2 = Singleton(27,"sjisv")
print(stu2)

"""
可以看到创建的三个不同的实例对象的内存地址是一样的.说明符合单例模式

-----单例模式---------
<__main__.Singleton object at 0x0000013CCDC15240>
<__main__.Singleton object at 0x0000013CCDC15240>
<__main__.Singleton object at 0x0000013CCDC15240>

"""

