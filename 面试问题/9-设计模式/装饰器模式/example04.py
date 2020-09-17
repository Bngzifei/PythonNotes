# -*- coding: utf-8 -*-
import time


class MyClass:
    def __init__(self, func):
        """需要接收一个被装饰的函数引用  相当于装饰器函数中外层函数的作用,接收 函数名 参数"""
        self._func = func

    def __call__(self, *args, **kwargs):
        """可以让一个对象变成可调用的对象 就是可以 以 对象() 这样的形式执行  相当于装饰器函数中内层函数,调用函数"""
        # 类装饰器可以实现的功能,没有装饰器函数的强大
        print('call方法被调用了')
        res = self._func(*args, **kwargs)  # self._func() 这样也可以
        return res


# 如果@后面的名字不是函数名,而是类名,称为类装饰器
# func1 = MyClass(func1)  创建一个实例对象<这个对象可以接受一个参数>
@MyClass
def func2(age):
    time.sleep(2)
    print('in f2:', age)


# 判断一个对象是否可调用,如果:一个对象(),那么对象是可调用的
# 常见的可调用对象:类 函数 匿名函数 方法  实现了__call__()的对象 记住:普通的对象不可以
# 普通的实例对象不是可调用的
print(callable(func2))  # 写了__call__()方法就是可调用的
print(callable(MyClass))
func2(56)
# callable 可被调用

"""
问题:
1.>func1 = MyClass(func1)  里面 的 func1 是啥?  是一个类创建的实例对象  
2.>可调用对象的特点:
如何判断可调用 callable()/对象.()  
3.>实现了__call__方法的实例对象是 

"""
