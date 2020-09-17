# -*- coding: utf-8 -*-
def singleton(cls, *args, **kwargs):  # cls:可以传入一个类
    """实现单例模式的装饰器"""

    # 字典,保存单例对象
    instances = dict()

    def get_instance(*args, **kwargs):
        # 内层函数获得单例对象
        if cls not in instances:
            # 字典中没有这个单例对象就存进去
            instances[cls] = cls(*args, **kwargs)
        # 返回单例
        return instances[cls]

    # 本质就是返回产生的单例对象
    return get_instance


@singleton  # 本质就是: Student = singleton(Student).最后是返回get_instance()函数的引用
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("jiang", 25)
print(stu)
print(id(stu))

stu1 = Student("jiang1", 215)
print(stu1)
print(id(stu1))

stu2 = Student("jiang111", 15)
print(stu2)
print(id(stu2))
print(bool(stu is stu1))
print(bool(stu1 is stu))
print(bool(stu is stu2))
