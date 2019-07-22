# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 09:47:20
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 10:49:05


def foo(numbers=[]):               # 这里的[]是可变的,这样的话每执行一次foo,numbers都会添加一个9,意思就是上一次的numbers列表中的9会保存到 下一次 执行函数的时候
        numbers.append(9)
        print(numbers)

foo()                              # first time, like before, [9]
foo()                              # second time, not like before, [9, 9]
foo()                              # third time, not like before too, [9, 9, 9]


# 改进,这样写之后每次foo执行都是添加一个9
def foo(numbers=None):
    if numbers is None:
        numbers = []
        numbers.append(9)
        print(numbers)
foo()
foo()
foo()


# 另外一个例子,参数的默认值是不可变的
def foo(count=0):           # 这里的0是数字,是不可变的
    count += 1
    print(count)

foo()               # 输出1
foo()               # 输出1
foo(5)              # 输出6
foo()               # 还是输出1



# format(value, format_spec)格式化的使用
# 注意:print 的圆括号要放到整个字符串表达式的外面  ()
print ("I am {name},I like {value}".format(name = "bng",value = "value"))
print ("I am {0},I like {1}".format("lbin",'money'))
#
# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#
#
class Person(object):
    def __init__(self):
        pass
    def giveRaise(self):
        print("一切好嗨")


# 子类扩展超类:尽量调用超类的方法
class Manager(Person):
    def giveRaise(self):
        # self.pay = int(self.pay*(1 + percent + bonus))     # 不好的方式 复制粘贴超类代码
        # Person.giveRaise(self)            # 好的方式 尽量调用超类方法
        # super(当前类的名称,self或者cls,就是一个位置参数).重写父类的方法名(方法名中的参数,注意这里的参数要把self或者cls去掉)
        super(Manager,self).giveRaise()    # 更常见的方式,是上面写法的等价  xxx.giveRaise() 就是调用giveRaise这个方法了,.前面的xxx就是giveRaise方法的一个位置参数了


m = Manager()
m.giveRaise()