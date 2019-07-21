# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 09:30:56
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 09:45:27


#-- 本地变量是静态检测的
X = 22                             # 全局变量X的声明和定义,全局变量必须是大写
def test():
    print(X)                       # 如果没有下一语句 则该句合法 打印全局变量X
    X = 88                         # 这一语句使得上一语句非法 因为它使得X变成了本地变量 上一句变成了打印一个未定义的本地变量(局部变量)
    if False:                      # 即使这样的语句 也会把print语句视为非法语句 因为:
        X = 88                     # Python会无视if语句而仍然声明了局部变量X
def test1():                       # 改进
    global X                       # 声明变量X为全局变量
    print(X)                       # 打印全局变量X
    X = 88                         # 改变全局变量X



# test()
test1()