"""
得益于operator和functools等包的支持,函数式编程风格也可以信手拈来.


operator模块:

	在函数式编程中,经常需要把算术运算符当作函数使用.例如,不使用递归
	计算阶乘.求和可以使用sum函数.但是求积则没有这样的函数.我们可以
	使用reduce函数,但是需要一个函数计算序列中两个元素之积.

	
	operator模块为多个算术运算符提供了对应的函数,从而避免编写lambda
	这种平凡的匿名函数.使用算术运算符函数,可以改写成下面的...
	
	
"""

# 使用reduce函数和一个匿名函数计算阶乘
from functools import reduce
def fact(n):
	return reduce(lambda a,b:a*b,range(1,n+1))

print(fact(9))


from functools import reduce
from operator import mul
def fact1(n):
	return reduce(mul,range(1,n+1))


"""
operator模块中还有一类函数能替代从序列中取出元素或读取对象属性的lambda表达式:
metro_data = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
 ]

 attrgetter与itemgetter作用类似,它创建的函数根据名称提取对象的属性.如果把多个属性名
 传给attrgetter,它也会返回提取的值构成的元组.此外,如果参数名中包含.,attrgetter会深入
 嵌套对象,获取指定的属性.

"""