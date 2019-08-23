# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-07 20:20:29
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-07 20:49:17

# 定义一个装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        """这是装饰器内部的函数"""
        # 输出当前调用函数的名字 + "was called"
        print(func.__name__ + " was called")
        # 返回当前函数调用的结果
        return func(*args, **kwargs)
    # 返回内部函数的引用
    return with_logging


@logged  # <==> 等价于 : f = logged(f)
def f(x):
   """does some math"""
   return x + x * x

def f1(x):
    """does some math"""
    return x + x * x

# f = logged(f)

print(f(3))
print('---')
print(f.__name__)
print(f.__doc__)
print('---')
print(f1.__name__)
print(f1.__doc__)

# 在使用 装饰器 的过程中，难免会损失一些原本的功能信息,比如上面的  f1.__name__在没有使用装饰器的时候是  f1
# 使用了 装饰器 之后的 f.__name__ 就是装饰器函数的返回的内部函数引用的名字  with_logging
# 这样就是改变了原来函数的一些属性了.为了在使用装饰器的时候不改变这些属性值,引入 functools.wraps
#
# functools.wraps 则可以将原函数对象的指定属性复制给包装函数对象, 默认有  __module__、__name__、__doc__,或者通过参数选择。代码如下：


# from functools import wraps
import functools
def logg1ed(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logg1ed
def f2(x):
   """does some math"""
   return x + x * x

print(f2.__name__ ) # print 'f2'  输出的是对应函数的名称
print(f2.__doc__ )  # print 'does some math'   输出对应函数的注释说明文档


# 可以看到在使用了functools.wraps 之后就可以保持原来函数的__name__属性,__doc__属性不变,把使用装饰器对原来函数的影响去除了

