"""
Python内置了三个用于装饰方法的函数:property,classmethod和staticmethod

另一个常见的装饰器是functools.wraps,它的作用是协助构建行为良好的装饰器(就是可以让装饰器表现的更好).

标准库中最值得关注的两个装饰器是lru_cache和全新的singledispatch(Python3.4新增)
这两个装饰器在functools模块中定义.


使用functools.lru_cache做备忘

	fucntools.lru_cache是非常实用的装饰器,它实现了备忘录的功能.这是一项优化技术,它把耗时的函数的结果保存起来,
	避免传入相同的参数时重复计算.LRU三个字母是Least Recently Used 的缩写,表明缓存不会无限制增长.一段时间不用
	的缓存条目会被扔掉.

	生成第n个斐波那契数列这种慢速递归函数适合使用lru_cahce,如示例所示:

生成第n个斐波那契数列,递归方式非常耗时:
"""
from 修改后的装饰器 import clock


@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)


# if __name__ == '__main__':
	# print(fibonacci(6))


"""
除了最后一行，其余输出都是 clock 装饰器生成的.
输出:
[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00000000s]fibonacci(3) -> 2 
[0.00000000s]fibonacci(4) -> 3 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00097680s]fibonacci(3) -> 2 
[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00000000s]fibonacci(3) -> 2 
[0.00000000s]fibonacci(4) -> 3 
[0.00097680s]fibonacci(5) -> 5 
[0.00097680s]fibonacci(6) -> 8 
8


可以看到浪费时间的地方很明显:fibonacci(1)被调用了8次,fibonacci(2)调用了5次.
但是如果增加两行代码,使用lru_cache,性能会显著改善.




"""


# 使用缓存实现,速度更快
import functools

from 修改后的装饰器 import clock


@functools.lru_cache()
@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
	print(fibonacci(6))



"""
输出:

[0.00000000s]fibonacci(0) -> 0 
[0.00000000s]fibonacci(1) -> 1 
[0.00000000s]fibonacci(2) -> 1 
[0.00000000s]fibonacci(3) -> 2 
[0.00000000s]fibonacci(4) -> 3 
[0.00000000s]fibonacci(5) -> 5 
[0.00000000s]fibonacci(6) -> 8 
8


注意:必须像常规函数那样调用lru_cache.这一行中有一对括号:@functools.lru_cache().
这么做的原因是:lru_cache可以接受配置参数.

这样一来,执行时间减半了,而且n的每个值只调用一次函数.



除了优化递归算法之外,lru_cache在从Web中获取信息的应用中也能发挥巨大作用.

特别要注意:lru_cache可以使用两个可选的参数来配置,它的签名是:

functools.lru_cache(maxsize=128,typed=False)

maxsize参数指定存储多少个调用的结果.缓存满了之后,旧的结果会被扔掉,腾出空间.为了得到最佳性能,
maxsize应该设为2的幂.typed参数如果设为True,把不同参数类型得到的结果分开保存,即把通常认为相等的
浮点数和整数参数区分开.顺便是说一下,因为lru_cache使用字典存储结果.而且键根据调用时传入的定位参数和关键字
参数创建,所以被lru_cache装饰的函数,它的所有参数都必须是可散列的.
"""