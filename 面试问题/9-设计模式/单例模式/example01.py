# -*- coding: utf-8 -*-
class Singleton(object):
    # 先赋值空
    _instance = None

    def __new__(cls, *args, **kwargs):
        """重写__new__方法"""

        # 判断:为空就创建一个实例对象
        if cls._instance is None:
            # 使用父类的__new__方法创建一个实例对象
            cls._instance = object.__new__(cls)
            # 返回实例
            return cls._instance
        else:
            # 返回实例
            return cls._instance


stu = Singleton(25, "shdudhsv")
print(stu)
print(id(stu))
stu1 = Singleton(26, "dfhufdvh")
print(stu1)
print(id(stu1))
stu2 = Singleton(27, "sjisv")
print(stu2)
print(id(stu2))