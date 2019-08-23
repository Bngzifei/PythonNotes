# coding:utf-8

class Person:
    def __init__(self,age):
        self._age = age

    # @property   #  没有加@property 这个装饰器之前,
    # per.age只会输出<bound method Person.age of <__main__.Person object at 0x0000000001DD6908>>说明这只是实例的一个方法,
    # 如果想和属性一样获取值,就加@property装饰器
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if age > 255 or age < 0:
            print("哥们,输入的年龄暂时有点超前了")
        else:
            self._age = age

    @age.deleter
    def age(self):
        print("要删除self的age属性了...")
        del self._age




per = Person(13)
print(per.age)  # 返回值是一个实例方法的地址,并不会返回实例的age属性值,只有在调用这个方法的时候才会返回这个实例的age属性值,所以在这里
# 为了实现 per.age 方法也能在不调用的情况下拿到实例的_age属性,这里加@property实现
print("--------------------")
print(per._age)
per.age = 788
print(per.age)
print("--------------------")
print(per.age)
del per.age  # 在这一步删除掉per实例的age属性后,下面就没有办法获取到age属性了,所以就会报错:'Person' object has no attribute '_age'
# print(per.age)


