# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-09 17:37:13
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-09 19:14:40

import functools
import six

def decorator(func):
    # @functools.wraps(func)
    # @six.wraps(func)
    def wrapper(*args,**kwargs):
        print("开始调用内部函数...")
        res = func(*args,**kwargs)
        return print(res)

    return wrapper

@decorator  # <==> what = decorator(what)
def what(name):
    # res = '接收到的名字是:%s' % name
    # print(res)
    return name



what('libin')
# print(what.__name__)

