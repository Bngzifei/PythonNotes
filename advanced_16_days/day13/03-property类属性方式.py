class Person:
    def __init__(self, age):
        """_age单下划线的age是代表不能直接访问的类属性<也叫保护属性/变量/方法>，需通过类提供的接口进行访问，不能用“from xxx import *”而导入"""
        # self._age = age
        # 双下划线__age需要使用obj._类__age来访问
        self.__age = age

    def get_age(self):
        """将装饰的方法 当成获取属性的方式   执行当前这个方法"""
        return self._age

    def set_age(self, age):
        """如果需要让用户  对象.属性 的方式修改property装饰的属性,  将当前方法改为属性名
        并且还需要使用 @属性名.setter对当前方法进行装饰"""
        if age > 255 or age < 0:
            print('哥们,输入的年龄暂时有点超前了')
        else:
            self._age = age

    def del_age(self):
        """如果需要让用户  对象.属性 的方式删除property装饰的属性,  将当前方法改为属性名
                并且还需要使用 @属性名.deleter对当前方法进行装饰"""
        print('正在删除...')

    # property 类属性的方式
    # 包装成的属性 = property(获取操作,设置操作,删除操作,'属性的描述文档')
    age = property(get_age, set_age, del_age, '这是一个神奇的属性,居然是方法')


person = Person(18)
print(person.__dict__)  # {'_Person__age': 18}
print(person._Person__age)  # 18
# print(person.age)
# person.age = 989
# print(person.age)
# person1 = Person(20)
# print(person1.age)
# print(person.age)
print(Person.age)  # <property object at 0x000001B7AD6A7908>
# del person.age
# print(help(person))
# print(dir(person))
# print(dir(person))
# print(person.__doc__)

"""
名字重整:
_Person__age这种方式去调__age属性
_age:
目的是:保护私有变量/私有属性
记得看视频校对一下
"""
