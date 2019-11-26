# import clockdeco_demo

# print(clockdeco_demo.factorial.__name__)  # clocked

"""
所以现在factorial保存的是clocked函数的引用.自此之后,每次调用factorial(n)
执行的都是clocked(n).cloked大致做了下面几件事.


1.>记录初始时间t0

2.>调用原来的factorial函数,保存结果

3.>计算经过的时间.

4.>格式化收集的数据,然后打印出来

5.>返回第2步保存的结果.


这是装饰器的典型行为:把被装饰的函数替换成新函数,二者接受相同的参数,而且通常返回被装饰
函数本该返回的值,同时还会做些额外操作.

装饰器模式概述:
	
	动态地给一个对象添加一些额外的职责.


示例中实现的clock装饰器有几个缺点:不支持关键字参数,而且遮盖了被装饰函数的__name__和
__doc__属性.使用functools.wraps装饰器把相关的属性从func复制到clocked中,此外,这个新
版还能正确处理关键字参数.


改进后的clock装饰器
"""

import time
import functools

def clock(func):
	@functools.wraps(func)
	def clocked(*args,**kwargs):
		t0 = time.time()
		result = func(*args,**kwargs)
		elapsed = time.time() - t0
		name = func.__name__
		arg_lst = []
		if args:
			arg_lst.append(",".join(repr(arg) for arg in args))
		if kwargs:
			pairs = ["%s=%r"%(k,v) for k,v in sorted(kwargs.items())]
			arg_lst.append(",".join(pairs))

		arg_str = ",".join(arg_lst)
		print("[%0.8fs]%s(%s) -> %r " %(elapsed,name,arg_str,result))
		return result
	return clocked



"""
functools.wraps只是标准库中拿来即用的装饰器之一.

下面将介绍functools模块中最让人印象深刻的两个装饰器:lru_cache和
singledispatch

"""