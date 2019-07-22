print('匿名函数:')
# 也是从JS语言中借鉴过来的

"""就是没有名字的函数

匿名函数以表达式的方式来定义一个函数,只有一行,所以它只能做一些简单处理

格式:lambda 参数:返回值(就是一个表达式.)

应用场景:1.可以把匿名函数当成参数传递到函数内部去执行 2.自定义排序


"""


def func1(a, b):
	return a + b


# re = func1(2,3)
# print(re)
"""匿名函数使用1:"""

# fn = lambda a, b: a + b  # 此时fn就相当于匿名函数的名字
# re = fn(2, 5)
# print(re)  # 7
# re1 = fn(3, 5)
# print(re1)  # 8
#
#
# print(re1)
# print(func1)  # <function func1 at 0x0000025CEB342E18>
# print(fn)  # <function <lambda> at 0x0000025CED01B8C8>

# 函数当做参数传递-->闭包

"""匿名函数使用2:"""
re = (lambda a, b, c: a + b + c)(10, 30, 56)  # 一次性的函数  记住,:号前面的,lambda后面的是参数,:号后面的是表达式,也就是返回值部分.
re1 = (lambda a, b: a + b)(100, 30)

print(re)
print(re1)

"""当做参数传递"""


"""当自定义排序时候,lambda后面的值只能有一个,因为比较大小时是一个一个的进行比较"""

# sort(key=)
# 其中key用来指定比较大小的规则,只会影响排序规则
# 字符串比较大小是按照第一个字母的顺序
