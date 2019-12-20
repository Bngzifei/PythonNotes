# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-09 16:41:46
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-09 20:29:12


class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __call__(self,friend):
        # 在这里的self就是当前初始化之后的那个对象
        print("我的名字是:%s" % self.name)
        print("朋友的名字是:%s" % friend)

# 初始化的时候给初始化的两个参数
p = Person("mc","male")
# 然后在使用 对象() 调用的时候,再传一个参数
p("Time")
p1 = Person("man","famel")
p1("你是个撒")


"""
__call__()方法模糊了函数和方法之间的概念

"""

print('-------分割线----------')

class A(object):
    def __new__(cls,*args,**kwargs):
        object = super(A,cls).__new__(cls)
        print("__new__方法被调用")
        return object

    def __init__(self,*args,**kwarg):
        print("__init__方法被调用")

    def __call__(self,func):
        # 这里的func参数的位置就是可以给下面的装饰器
        # 用法进行传参
        print("__call__方法被调用")
        return func


# 在初始化下面的实例对象的时候,就会去执行A类中的__new__方法和__init__方法

# 这样的话a就是一个实例化对象,这个实例化对象可以被调用 即可以 a()这么写
a = A()
print('-------分割线----------')
b = A()
print('-------分割线----------')
# @A()  # 这样的话就是一个装饰器的写法了
@a # 这样的话就是一个装饰器的写法了  就是等价于 <==> hello = a(hello)  这样的话就已经是调用装饰器函数了.就会输出 : __call__方法被调用
def hello():
    print("hello函数被调用")

print('-------分割线----------')

# 到这里的话只是调用hello函数了,和hello函数上面的装饰器没有关系
hello()

# 这么写的话还不会改变函数的__name__和__doc__属性
print(hello.__name__)
print('-------分割线----------')

# 到这里的话,我直接传一个字符串形式的  函数名 hello
# 这样就是调用了__call__方法,就会输出__call__方法中的内容
b('hello')


# 注意:类在生成实例的时候不会调用__call__()方法,但在作为装饰器使用的时候__call__()会被调用
#
# hasattr函数: 判断指定属性(或方法)是否存在,但是到底是属性还是方法,则需要进一步判断它是否可调用.程序可以通过判断该属性(或方法)是否包含__call__属性来确定它是否可调用
#
#

class User:
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def vaild(self):
        print("验证%s的登录" % self.name)
# 实例化一个对象
u = User('libin','123456')
# 判断u这个实例对象是否包含__call__方法
print(hasattr(u,'__call__'))  # False
# 判断u.name属性是否包含__call__方法
print(hasattr(u.name,'__call__'))  # False
# 判断u.passwd属性是否包含__call__方法,即判断是否可调用
print(hasattr(u.passwd,'__call__'))  # False
# 判断u.vaild方法是否包含__call__方法,即判断是否可调用
print(hasattr(u.vaild,'__call__'))  # True


# 分别判断User实例对象的name,passwd,属性 vaild方法是否包含__call__方法,如果包含该方法,则表明它是可调用的,否则就说明它是不可调用的.
#


# 实际上,一个函数(甚至对象)之所以能执行,关键在于__call__方法.实际上x(args1,args2,...)只是x.__call__(args1,args2,...)的快捷写法,因此我们甚至可以为自定义类添加__call__方法,从而使得该类的实例也变成可调用的.比如:

# 定义Role类
class Role:
    def __init__(self,name):
        self.name = name

    # 定义__call__方法
    def __call__(self):
        print("执行Role对象")

r = Role('管理员')

# 直接调用Role对象,就是调用该对象的__call__方法
r.__call__()
# 可以看到调用 r对象  r() 和调用 r 对象的__call__方法是一样的
r()


# 对于程序中的函数:同样可以使用函数的语法来调用它,也可以把函数当成对象,调用它的__call__方法.例如如下示例代码:

def func():
    print("--func函数被调用--")

# 下面示范了2种方式调用func()函数
func()
# 执行两种方式的调用,可以看到func()和func.__call__()的效果完全相同
func.__call__()


print("-----------------------------------")

def keyOnly(a, *b, c=0):
    print('c的位置参数在使用的时候就必须是 c=xx这种形式',a,b,c)


keyOnly(1,2,c=3)



print("-----------------------------------")

# 成员变量都进行相同操作之后存起来
print(list(map(lambda x:x+1,[1,2,3,4])))
# 筛选符合条件的成员变量
print(list(filter(lambda x:x+1==2,[1,2,3,4])))
# 把多个成员变量按照指定的函数规则合成一个变量
# 比如在下面的用法中就是对列表中的元素求乘积
from functools import reduce  # 这个在py3版本中放到了functools模块里面了
print(reduce(lambda x,y:x*y,[1,2,3,4]))

