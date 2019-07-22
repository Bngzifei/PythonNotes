# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 11:26:50
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 17:29:12


#-- 动态创建类type()
# 一般创建类 需要在代码中提前定义
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
# h = Hello()
# h.hello()                             # Hello, world
# type(Hello)                           # Hello是一个type类型 返回<class 'type'>
# type(h)                               # h是一个Hello类型 返回<class 'Hello'>

# 动态类型语言中 类可以动态创建 type函数可用于创建新类型
def fn(self, name='world'):           # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn))    # 创建Hello类 type原型: type(name, bases, dict)
h = Hello()                           # 此时的h和上边的h一致
h.hello() # 这里的hello就是属性字典中你设置的key,对应的值是fn函数


