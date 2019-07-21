# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-10 17:46:27
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-10 17:51:51


# 嵌套函数举例:工厂函数

def maker(N):
    def action(X):
        return X ** N
    return action
f = maker(2)  # N = 2
f(3)  # X = 3

# 实际结果就是 3**2 = 9
print(f(3))



