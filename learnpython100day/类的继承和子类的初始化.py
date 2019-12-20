# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 11:07:29
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 11:24:21


#-- 类的继承和子类的初始化
# 1.子类定义了__init__方法时，若未显示调用基类__init__方法，python不会帮你调用。
# 2.子类未定义__init__方法时，python会自动帮你调用首个基类的__init__方法，注意是首个。
# 3.子类显示调用基类的初始化函数：
class FooParent(object):

    def __init__(self, a):
        self.parent = 'I\'m the Parent.'
        print('Parent:a=' + str(a))

    def bar(self, message):
        print(message + ' from Parent')

class FooChild(FooParent):

    def __init__(self, a):
        FooParent.__init__(self, a)
        print('Child:a=' + str(a))

    def bar(self, message):
        FooParent.bar(self, message)
        print(message + ' from Child')


fooChild = FooChild(10)
fooChild.bar('HelloWorld')

print("----------------------------------------------------")
# (4)__getattr__方法: 定制类的属性操作
class Student(object):

    def __getattr__(self, attr):          # 定义当获取类的属性时的返回值
        if attr=='age':
            return 25                     # 当获取age属性时返回25
    raise AttributeError('object has no attribute: %s' % attr)
    # 注意: 只有当属性不存在时 才会调用该方法 且该方法默认返回None 需要在函数最后引发异常
s = Student()
s.age                                     # s中age属性不存在 故调用__getattr__方法 返回25