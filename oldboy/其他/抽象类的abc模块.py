# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-07 20:53:38
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-07 21:04:35

# 1.什么是抽象类 ?
#
#  与java一样，python也有抽象类的概念但是同样需要借助模块实现，抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化


# 2.为什么要有抽象类?
# 如果说类是从一堆对象中抽取相同的内容而来的，那么抽象类就是从一堆类中抽取相同的内容而来的，内容包括数据属性和函数属性。

#   比如我们有香蕉的类，有苹果的类，有桃子的类，从这些类抽取相同的内容就是水果这个抽象的类，你吃水果时，要么是吃一个具体的香蕉，要么是吃一个具体的桃子。。。。。。你永远无法吃到一个叫做水果的东西。

#   从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的。

#　 从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法。这一点与接口有点类似，但其实是不同的，即将揭晓答案



# 一切皆文件
import abc  # 利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):

    all_type='file'

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

# 这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)


print("---------------------")


import abc

class A(metaclass=abc.ABCMeta):  # 指定元类,A是一个抽象类

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def abstract_method(self):
        """子类必须定义该方法"""
        pass

# class B(A):
#     pass

# b=B()  # TypeError: Can't instantiate abstract class Txt with abstract methods

class B(A):  # 子类继承抽象类，必须定义抽象方法
    def abstract_method(self):
        print('抽象方法')

b = B()
b.abstract_method() # 抽象方法