# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-09 16:17:08
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-09 16:41:00


class Person(object):
    """Silly for Person"""

    def __new__(cls,name,age):
        print("__new__方法被调用")
        return super(Person,cls).__new__(cls)  # python3这里__new__方法的参数只需要一个cls对象就行

    def __init__(self,name,age):
        print("__init__方法被调用")
        self.name = name
        self.age = age

    def __str__(self):
        return "Person: %s-%d" % (self.name,self.age)


if __name__ == "__main__":
    pig = Person("lb",27)
    print(pig)
    print(Person.__mro__)
    print(type(Person.__mro__))
    print(Person.mro())
    print(type(Person.mro()))
