class FibIter:
	def __init__(self, n):
		self.n = n
		self.num1 = 1
		self.num2 = 1
		self.count = 0

	def __iter__(self):
		"""iter(对象):取出对象的迭代器 作为本对象  通过__iter()__返回一个迭代器"""
		return self  # 类是迭代器,所以创建的对象就是可迭代对象

	def __next__(self):
		"""值 = next(迭代器)  作为本对象 通过__next__()反复返回下一个元素的值"""
		if self.count < self.n:
			ret = self.num1
			# 打包/拆包
			self.num1, self.num2 = self.num2, self.num1 + self.num2
			self.count += 1
			return ret
		else:
			raise StopIteration


# n提前不准备数据,只是需要使用的时候才会去计算所需要的那一个,延迟计算.  Python实现的延迟计算(也成为懒惰计算)
if __name__ == '__main__':
	# 1 1 2 3 5 8 13
	# 创建一个实例对象
	f = FibIter(10)

	# 如果能够遍历

	# 法1:
	# for i in f:
	# 	print(i)

	# 法2:
	it = iter(f)  # 每次都是取出第一个元素  实际上是去调用__iter__()方法 自动调用魔法方法.
	while True:
		# 通过迭代器取出下一个元素的值<返回值>
		try:
			# it = iter(data)  # 每次都是取出第一个元素,不能放在这里,否则就是死循环.
			i = next(it)  # 迭代器的返回值赋给i  自动调用__next__() 魔法方法.
		# 如果迭代完成,则抛出StopIteration异常
		except Exception as e:
			print(e)
			break
		else:
			print(i)


"""
总结:
1.> 迭代器: 记录迭代的位置信息的对象
	操作:
		迭代器= iter(可迭代对象)  --> 可迭代对象.__iter__()
		下一个元素的值= next(迭代器)  --> 迭代器.__next__() 
		
	判断:
		isinstance(对象,类型)  判断对象是否是xxx类型  返回值是True或者False
		isinstance(对象,迭代器类型)
		isinstance(对象,Iterator)  # 首先要导入 fron collections import Iterator
		
2.> 实现迭代器
		魔法方法: Python 预先自定义功能的方法.
		__iter__()方法  提供迭代器<返回self  毛遂自荐>
		__next__()方法  提供下一个元素


可迭代对象:
	可以被迭代的对象
	判断:for循环遍历(偶尔使用还行)
	from collections import Iterable
	isinstance(obj,Iterable)  # 判断一个对象是否是可迭代类型
	
	结论:迭代器一定是可迭代对象
	可迭代对象 不一定是迭代器  <只需要实现__iter__()方法提供迭代器>

面试:	
迭代器需要实现那些方法?  
	__iter__()  __next__()
	
可迭代对象需要实现那些方法?   __next__() 可以有,也可以没有
	__iter__()  -> 可迭代对象的标识    可迭代对象的范围更大<包含了迭代器>
	
	
迭代器和可迭代对象的区别  
	迭代器一定是可迭代对象/可迭代对象 不一定是迭代器
	
如何判断对象是否是可迭代对象/迭代器
	isinstance(obj,Iterable) ---> 可迭代对象
	isinstance(obj,Iterator) ---> 迭代器
	
示例:
from collections import Iterator
d = [1,2,3,4]
isinstance(d,Iterator)
Out[15]: False

d1 = iter(d)
isinstance(d1,Iterator)
Out[15]: True


from collections import Iterable
isinstance(d,Iterable)
Out[17]: True


"""