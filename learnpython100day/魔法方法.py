# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-29 11:27:43
# @Last Modified by:   Marte
# @Last Modified time: 2019-06-05 09:11:50

# 定义一个能够自动比较大小的People类
class People(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        return

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self,other):
        return self.name < other.name if self.name != other.name else self.age < other.age


print("\t".join([str(item) for item in sorted([People("abc", 18), People("abe", 19), People("abe", 12), People("abc", 17)])]))

# Python实现任意深度的赋值 例如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'


class MyDict(dict):

    def __setitem__(self,key,value):        #  该函数不做任何改动,这里只是为了输出
        print("setitem:",key,value,self)
        super().__setitem__(key,value)
        return

    def __getitem__(self,item):     # 主要技巧在该函数
        print("getitem:",item,self)

        # 基本思路: a[1][2]赋值时,需要先取出a[1],然后给a[1]的[2]赋值
        if item not in self:
            temp = MyDict()
            super

class A(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = A("qi",9)
a.name = "qi"
a.age  = 9

# 返回对象的变量名,变量值的字典(字典,哈希,映射,map等等就是有一个对应关系的概念,
# 这样的统统就是python中的字典类型)
print(vars(a))          # {'name':'qi', 'age':9}

