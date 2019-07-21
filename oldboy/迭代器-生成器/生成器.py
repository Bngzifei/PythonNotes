"""
什么是生成器?
答:可以理解为一种数据类型,这种数据类型自动实现了迭代器协议(其他的数据类型需要调用自己内置的__iter__()方法),
所以生成器就是可迭代对象.(意思就是不再需要去调用__iter__()方法了)

生成器分类及在Python中的表现形式:(Python中有两种不同的方式提供生成器)
1.>生成器函数:常规函数定义,但是,使用yield语句而不是return语句返回结果.yield语句一次返回一个结果,
在每个结果中间,挂起函数的状态,以便下次从它离开的地方继续执行.
2.>生成器表达式:类似于列表推导式,但是,生成器返回按需产生结果的一个对象,而不是一次构建一个结果列表


为何使用生成器之生成器的优点?
Python使用生成器对延迟操作提供了支持,所谓延迟操作,是指在需要的时候才产生结果,而不是立即产生结果.
这也是生成器的主要好处.

生成器小结:
1.是可迭代对象
2.实现了延迟计算,省内存
3.生成器本质和其他数据类型一样,都是实现了迭代器协议,只不过生成器附加了一个延迟计算省内存的好处,其余
的可迭代对象可没有这点好处.切记切记!



总结:
1.> 把列表解析的[]换成()得到的就是生成器表达式
2.> 列表解析与生成器表达式都是一种便利的编程方式,只不过生成器表达式更省内存.
3.> Python不但使用迭代器协议让for循环变得更加通用.此外,大部分内置函数,也是使用迭代器协议访问对象的.例如,
sum(),max(),filter(),map(),reduce(),min()
函数是Python的内置函数,该函数使用迭代器协议访问对象,而生成器实现了迭代器协议,所以,我们可以这样直接计算一系列值
的和:

sum(x ** 2 for x in xrangge(4))

"""


# l = [x ** 2 for x in range(4)]
# print(l)
# print(sum(l))

# print(sum([x ** 2 for x in range(4)]))  # 耗内存
#
# print(sum(x ** 2 for x in range(4)))  # 更省内存

# 验证:
# print(sum(list(range(100000000))))
# print(sum(list(range(1000000000000))))  #  实际是一个列表,特别占内存,一下子就卡死了

# l = list(range(1000000000))
# print(l)
# print(sum(l))


# 生成器模式,虽然也很慢,但是并不卡,说明不占内存
# print(sum(i for i in range(110000000000)))  # 实际就是一个生成器表达式

# sum()计算的慢是因为和cpu有关,和内存无关











# 函数中是yield() 生成器表达式是(列表解析式)
# 只要函数(方法中)出现的是yield 而不是return,那么这个函数就是生成器
def test():
	yield 1
	yield 11
	yield 111  # 也就是说yield代替了return,但是可以实现多次return的效果 (而return在一个函数中只能执行一次)


g = test()  # <generator object test at 0x00000213E0970F10>
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


"""三元表达式:"""

# # name = 'alex'
# name = 'linhaifneg'
# # if后面的条件成立的情况下,将if前面的值赋给res,如果if后面的条件不成立,,就把else后面的值赋给res
# res = 'SB' if name == 'alex' else '帅哥'
# print(res)

"""列表解析"""

# egg_list = []
# for i in range(10):
# 	egg_list.append('鸡蛋%s' % i)
# print(egg_list)
# 列表解析1  生成的是列表,占用内存大
# l = ['鸡蛋%s' % i for i in range(10)]
# print(l)
# 列表解析2  实际上是三元表达式
# l = ['鸡蛋%s' % i for i in range(10) if i > 5]
# print(l)

# 下面就是四元表达式了,但是Python中没有四元这种
# l = ['鸡蛋%s' % i for i in range(10) if i > 5 else i]
# print(l)

# 下面就是四元表达式了,但是Python中没有四元这种
# l = ['鸡蛋%s' % i for i in range(10) if i > 5 else i]
# print(l)


# 不要列表了,我要一个生成器
# laomuji = ('鸡蛋%s' % i for i in range(10))  # 生成器表达式,省内存,直接就是一个迭代器
# print(laomuji)  # <generator object <genexpr> at 0x000001B5E0530F10>
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(laomuji.__next__())  # 内部的__next__()方法
# print(next(laomuji))  # next()内置函数
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
