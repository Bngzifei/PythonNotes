# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 11:00:17
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 11:04:44

#-- 为类动态绑定属性或方法: MethodType方法
# 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
class Student(object):
    pass

s = Student()

s.name = 'Michael'                  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):             # 定义一个函数作为实例方法
    self.age = age
    return self.age

from types import MethodType
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法 类的其他实例不受此影响
print(hasattr(s,'set_age'))         # 使用hasattr函数判断s实例是否有set_age方法的属性
# print(s.set_age(25))                       # 调用实例方法

Student.set_age = MethodType(set_age, Student)    # 为类绑定一个方法 类的所有实例都拥有该方法

print(s.set_age(25))