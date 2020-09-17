# -*- coding: utf-8 -*-
import time


def get_time(func):  # 这里只能接收一个参数,即使写成了*args **kwargs的形式
    """对函数运行时间进行统计"""
    print('in get_time')

    def inner(*args, **kwargs):  # 传参数,打包  内部函数可以接收任意参数
        t1 = time.time()
        # 解包参数  如果函数有返回值,暂时先保存,执行结束再返回
        # 这里的* 和** 是解包的作用,将刚刚打包的参数进行解包
        res = func(*args, **kwargs)  # res 暂时先保存执行结果
        t2 = time.time()
        print('运行了%s s' % (t2 - t1))
        # 如果 这里是 func(*args, **kwargs) 那么就会把func又执行了一遍,多余.
        return res  # 返回执行结果

    return inner


@get_time  # 只要这样写,就把 装饰器执行了  func1 = get_time(func1)
def func1(num, age=18):
    for i in range(3):
        time.sleep(1)
        print('in func', num, age)


@get_time  # 灵魂代码, 一旦装饰就执行
def func2(num, height=180, **kwargs):
    time.sleep(2)
    print('in f2', num, height)
    print(kwargs)
    return 250


func1(222)
func2(999, minzgi=333)
