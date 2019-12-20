"""
迭代:可以使用for遍历(或者更直接一点,这个对象是否内部有__iter__()方法)

可迭代对象:使用for循环遍历取值的对象叫可迭代对象.<列表,元组,字典,集合,range,字符串,文件对象>

"""
"""
判断对象是否是可迭代对象


记住:res/ret都是result的简写,结果之意

"""

import collections

# result = isinstance((3, 5), collections.Iterable) # 是
# print(result)
# print(isinstance([3, 5], collections.Iterable))  # 是
# print(isinstance('yusdhsuc', collections.Iterable))  # 是
# print(isinstance({3, 4, 5, 6}, collections.Iterable))  # 是
# print(isinstance({'key': 'value', '1': 1}, collections.Iterable))  # 是
# print(isinstance(range(4), collections.Iterable))  # 是
# print(type(range(4)))  # <class 'range'>
# print(isinstance(3, collections.Iterable))  # 否
# print(isinstance(3.98, collections.Iterable))  # 否

# isinstance(): 判断某个对象是否是 某个类所创建的实例对象
# print(isinstance(5, int))  # True
#
#
# class Student(object):
# 	pass
#
#
# stu = Student()
# print(isinstance(stu, collections.Iterable))  # False
# print(isinstance(stu, Student))  # True


"""自定义可迭代对象:

在类里面定义__iter__()方法,由此类创建的对象就是可迭代对象(太拗口,,实际上就是类中有
__iter__()方法,那么这个类创建的对象就是可迭代对象.

"""
# import collections
#
#
# # 自定义 可迭代对象:类中加__iter__()即可
# class MyList(object):
# 	def __init__(self):
# 		self.my_list = list()
#
# 	def append_item(self, item):
# 		self.my_list.append(item)
#
#
# 	# 可迭代对象的本质:遍历可迭代对象的时候,其实获取的是可迭代对象的迭代器,
# 	# 通过迭代器来获取其中的数据
# 	def __iter__(self):
# 		pass
#
# 	def __next__(self):
# 		return self.my_list
#
#
# my_list = MyList()
# my_list.append_item(1)
# my_list.append_item(11)
# my_list.append_item(111)
# my_list.append_item(1111)
#
# # result = isinstance(my_list,MyList)  # True
# # print(result)
# # result1 = isinstance(my_list,collections.Iterable)  # True
# # print(result1)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
#
#
# # for value in my_list:
# # 	print(value)
# print(my_list)


"""注意:
1.>遍历可迭代对象依次获取数据需要迭代器
2.>在类里面提供一个__iter__()创建的对象是可迭代对象,可迭代对象是
需要迭代器完成数据迭代的.

"""

"""迭代器:"""

"""1.>自定义迭代器对象:

在类里面定义__iter__()和__next__()方法创建的对象就是迭代器对象.




"""

import collections

# 自定义可迭代对象:类中加__iter__()
# class MyList(object):
# 	def __init__(self):
# 		self.my_list = list()
#
# 	def append_item(self, item):
# 		self.my_list.append(item)
#
# 	def __iter__(self):
# 		# 可迭代对象本质:遍历的时候--->迭代器,通过迭代器去取对象中的数据
# 		my_iterator = MyIterator(self.my_list)
# 		return my_iterator
#
# class MyIterator:
# 	def __init__(self, my_list):
# 		self.my_list = my_list
#
# 		# 记录当前获取数据的下标
# 		self.current_index = 0
# 		# 判断当前对象是否是迭代器
# 		print(isinstance(self, collections.Iterable))
#
# 	def __iter__(self):
# 		return self
#
# 	# 获取迭代器中的下一个值
# 	def __next__(self):
# 		if self.current_index < len(self.my_list):
# 			self.current_index += 1
# 			return self.my_list[self.current_index - 1]  # 从第一个开始
# 		else:
# 			# 数据取完了,需要抛出一个停止迭代的异常.
# 			raise StopIteration
#
#
# my_list = MyList()
# my_list.append_item(1)
# my_list.append_item(11)
# my_list.append_item(111)
#
#
# for i in my_list:
# 	print(i)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))


# next(my_list)
# my_list.__next__()
# my_list.__next__()
# my_list.__next__()

"""iter()函数和next()函数"""
"""
iter():获取可迭代对象的迭代器,会调用其对象的__iter__()方法
next():获取迭代器中的下一个值,会调用其对象的__next__()方法


"""

# import collections
#
#
# # 自定义可迭代对象:类中加__iter__()
# class MyList:
# 	def __init__(self):
# 		self.my_list = list()
#
# 	def append_item(self, item):
# 		self.my_list.append(item)
#
# 	def __iter__(self):
# 		# 可迭代对象本质:遍历的时候--->迭代器,通过迭代器去取对象中的数据
# 		my_iterator = MyIterator(self.my_list)
# 		return my_iterator
#
#
# # 自定义迭代器对象:类中加了__iter__和__next__方法,创建出来的对象就是迭代器对象.
# # 迭代器是记录当前数据的位置,以便获取下一个位置的值
# class MyIterator():
# 	def __init__(self, my_list):
# 		self.my_list = my_list
#
# 		# 记录当前获取数据的下标
# 		self.current_index = 0
#
# 	def __iter__(self):
# 		return self
#
# 	# 获取迭代器中的下一个值
# 	def __next__(self):
# 		if self.current_index < len(self.my_list):
# 			self.current_index += 1
# 			return self.my_list[self.current_index - 1]  # 从第一个开始
# 		else:
# 			# 数据取完了,需要抛出一个停止迭代的异常.
# 			raise StopIteration
#
#
# # 创建了一个自定义的可迭代对象
# my_list = MyList()
# my_list.append_item(1)
# my_list.append_item(11)
# my_list.append_item(111)
# my_list.append_item(1111)
# my_list.append_item(11111)
# my_list.append_item(111111)
#
# # 获取可迭代对象的迭代器
# my_iterator = iter(my_list)
# print(my_iterator)
#
# # 获取迭代器中下一个值
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# 循环获取
# while True:
# 	try:
# 		print(next(my_iterator))
# 	except StopIteration as e:
# 		break  # 遇到异常就停止



"""for 循环的本质:
遍历的是可迭代对象:
for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器,
然后对获取的迭代器不断调用next()方法,来获取下一个值,并且将这个值赋给item,
当遇到StopIteration的异常后循环结束.

遍历的是迭代器:
	for item in Iterator 循环的迭代器,,不断调用next()方法来获取下一个值,并将其赋给item,,当遇到
	StopIteration的异常后结束循环.

"""

"""迭代器应用场景:
最核心的是通过next()函数调用,返回下一个数据.好处 --->节省内存空间


"""

"""例子:斐波那契数列"""

# class Fibonacci:  # 记着这里的()直接不写就行
# 	def __init__(self, num):
# 		self.num = num
# 		self.a = 0
# 		self.b = 1
# 		# 记录当前生成数字的索引
# 		self.current_index = 0
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.current_index < self.num:
# 			result = self.a
# 			self.a, self.b = self.b, self.a + self.b
# 			self.current_index += 1
# 			return result
# 		else:
# 			raise StopIteration
#
#
# fib = Fibonacci(15)
#
# for i in fib:
# 	print(i)

"""迭代器的作用就是记录当前数据的位置,以便获取下一个位置的值"""

"""生成器:
概念:特殊的迭代器,不再需要写__iter__()和__next__(),直接就是一个迭代器



"""

"""法1:列表生成式的[] ---> ()  ---> generator object """
"""法2:在def 函数里面出现yield 就是生成器 """

"""示例:斐波那契:"""

# def Fib(num):
# 	a = 0
# 	b = 1
# 	current_index = 0
# 	print('--11--')
# 	while current_index < num:
# 		res = a
# 		a, b = b, a + b
# 		current_index += 1
# 		print('--22--')
# 		yield res
# 		print('--33--')
#
#
# fib = Fib(8)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

"""总结: 在使用生成器实现的方式中,__next__()方法换成了 一个函数来实现,
将返回值得return换成了yield,那么,这个时候就不再是函数,是生成器

"""

"""生成器使用return关键字"""
# def Fib(num):
# 	a = 0
# 	b = 1
# 	current_index = 0
# 	print('--11--')
# 	while current_index < num:
# 		res = a
# 		a, b = b, a + b
# 		current_index += 1
# 		print('--22--')
#
# 		# 执行到yield会暂停,然后把结果返回,下次启动生成器会在暂停的位置继续往下执行
# 		yield res
# 		print('--33--')
# 		return '哈哈哈哈或或'
#
#
# fib = Fib(8)
# try:
# 	print(next(fib))
# except StopIteration as e:
# 	print(e.value)

# 提示:return有终止函数的功能,所以代码执行到return的时候会停止迭代,抛出异常
# 在py3中可以使用return关键字,py2中不支持.


"""使用send()方法启动生成器并且传递参数"""

# def gen():
# 	i = 0
# 	while i < 5:
# 		temp = yield i
# 		print(temp)
# 		i += 1
#
#
# f = gen()
# # 迷糊
# next(f)
# f.send('hhhhhh')
# next(f)
# next(f)
# next(f)

"""协程-yield:

单线程的情况下完成多任务.
多个任务按照一定的顺序交替执行
通俗的理解:只要在def里面看到一个yield就是协程

协程也是实现多任务的一种方式.

就是交替执行-->多任务

小结:协程之间执行任务按照一定顺序交替执行.
"""
# import time
#
#
# def work1():
# 	while True:
# 		print('---work1---')
# 		yield  # 记住这个位置,下次继续
# 		time.sleep(1)
#
#
# def work2():
# 	while True:
# 		print('---work2---')
# 		yield  # # 记住这个位置,下次继续
# 		time.sleep(1)
#
#
# def main():
# 	w1 = work1()
# 	w2 = work2()
# 	while True:
# 		next(w1)
# 		next(w2)
#
#
# if __name__ == '__main__':
# 	main()

"""
greenlet:模块,对其封装,从而使得切换任务变得更加简单.

绿色小鸟 模块
"""

# import greenlet  # 绿色小鸟
# import time
#
#
# def work1():
# 	for i in range(5):
# 		print('work1...')
# 		time.sleep(0.2)
# 		g2.switch()
#
#
# def work2():
# 	for i in range(5):
# 		print('work2...')
# 		time.sleep(0.2)
# 		g1.switch()
#
#
# if __name__ == '__main__':
# 	g1 = greenlet.greenlet(work1)
# 	g2 = greenlet.greenlet(work2)
# 	g1.switch()
# 1和2交替出现,就是多任务


"""gevent:

greenlet已经实现了协程,但是这个还需要人工切换,不方便.

升级版:第三方库 ---> gevent

内部封装的greenlet,原理是:当一个greenlet遇到IO操作时候,比如访问网络,就自动切换到其他的
greenlet,等到IO操作完成,再在适当的时候切换回来继续执行.

理解:就是IO操作比较耗时,这个时间可以腾出来去做其他的任务,不会浪费系统资源.

安装:pip3 install gevent

"""

# import gevent
#
#
# def work(n):
# 	for i in range(n):
# 		# 获取当前协程
# 		print(gevent.getcurrent(), i)
# 		# 用来模拟一个耗时操作,注意:不是time模块中的sleep
# 		gevent.sleep(1)
#
#
# g1 = gevent.spawn(work, 5)
# g2 = gevent.spawn(work, 5)
# g3 = gevent.spawn(work, 5)
# g4 = gevent.spawn(work, 5)
#
#
# g1.join()  # 等待greenlet结束
# g2.join()
# g3.join()
# g4.join()

# 顺序依次执行,不是交替执行
"""打补丁:"""
# import gevent
# from gevent import monkey
# import time
#
# # 打补丁,让gevent框架识别耗时操作.例如,网络请求延时等等
# monkey.patch_all()
#
#
# def work1(n):
# 	for i in range(n):
# 		# 获取当前协程
# 		print('work1...')
# 		time.sleep(0.2)
#
#
# def work2(n):
# 	for i in range(n):
# 		# 获取当前协程
# 		print('work2...')
# 		time.sleep(0.2)
#
#
# if __name__ == '__main__':
# 	# 创建协程指定对应的任务
# 	g1 = gevent.spawn(work1, 3)
# 	g2 = gevent.spawn(work2, 3)
#
# 	# # 等待
# 	# g1.join()
# 	# g2.join()
#
# # 当前程序是一个死循环并且还能有耗时操作，
# # 就不需要加上join方法了,因为程序需要一直运行不会退出
# 	while True:
# 		print('主线程中执行...')
# 		time.sleep(0.5)


"""进程/线程/协程 之间的关系:

1.>一个  进程  至少有一个  线程, 进程 里面可以有很多个  线程.
	一个  线程  里面可以有很多个  协程.

2.>进程/线程/协程 的对比

	1.进程是资源分配的单位
	2.线程是os调度的单位
	3.进程切换需要的资源最大,效率很低
	4.线程切换需要的资源一般,效率一般
	5.协程切换任务资源很小,效率高
	6.多进程/多线程 根据cpu核数的 不一样,有时候可能是并行的,但是协程在一个线程中
	,所以是并发的(轮流依次执行,只是看起来是一起执行的罢了)


小结:进程/线程/协程 都是可以完成多任务,根据需要选择使用
	 由于线程/协程需要的资源很少,所以使用线程和协程的几率最大
	 开辟协程需要的资源最少.
"""

"""案例:gevent多任务图片下载:"""

import gevent
import urllib.request  # 网络请求模块
from gevent import monkey

# 打补丁:使用网络请求的耗时操作的时候,让协程自动切换对应的下载任务
monkey.patch_all()


# 根据图片地址下载对应的图片
def download_img(img_url, img_name):
	try:
		print(img_url)
		response = urllib.request.urlopen(img_url)
		# 创建文件把数据写入到指定的文件夹里面
		with open(img_name, 'wb') as img_file:
			while True:
				# 读取网络图片
				img_data = response.read(1024)
				if img_data:
					img_file.write(img_data)
				else:
					break
	except Exception as e:
		print('图片下载异常:', e)
	else:
		print('图片下载成功:%s' % img_name)


if __name__ == '__main__':
	# 图片地址
	# img_url1 = 'https://imgsa.baidu.com/forum/w%3D580/sign=ce94fa44d91b0ef46ce89856edc551a1/0fa1678da9773912d94d370bf3198618377ae290.jpg'
	# img_url2 = 'https://imgsa.baidu.com/forum/w%3D580/sign=3aca5c706b59252da3171d0c049a032c/d68cad389b504fc236510e6feedde71191ef6df5.jpg'
	# img_url3 = 'http://img.mp.itc.cn/upload/20170516/357c730e78ba4e688163e3060a02a3df_th.jpg'
	img_url4 = 'http://isure.stream.qqmusic.qq.com/C400003M3Q8j47vepF.m4a?vkey=315519233C33188E5770CD9F768A3E26CC54A2B7381E9DCBABE4F02200CC946EA45E4D42309111B5CDC8802188FBB0301A404CD335CFA04C&guid=3082389512&uin=0&fromtag=66'
	# img_url5 = 'http://isure.stream.qqmusic.qq.com/C4000035GQtJ19dQ97.m4a?vkey=7BAFB998CCB99F1397FFF060A6E6087C933BEDA9A00E2147336379903528BE1B39C77A874860C6F60FCC2CFFCFA494BAB03F29E88F77FDB0&guid=3082389512&uin=0&fromtag=66'
	# img_url6 = 'http://isure.stream.qqmusic.qq.com/C400002Gt1mf3xRRQF.m4a?vkey=54ECE5EF08C6C1A7D714B7E5E1B7DA5F224D66EC4C156275EC7A6F905AAE586E1116C04C4D09E66D0D28A16AC98F77F5228A2169232FB1B2&guid=3082389512&uin=0&fromtag=66'
	img_url7 = 'http://isure.stream.qqmusic.qq.com/C400000Qhd4C3Hfn7t.m4a?vkey=B718C019BDDD359E1796263F7BB1179F453FE9A8C15CEF5202E02888F94C6DA0673D32F96CEAC1F33C4DD66B321CCF8D126E3ABE8094A5D4&guid=3082389512&uin=0&fromtag=66'
	# 创建协程分配对应的任务
	# g1 = gevent.spawn(download_img, img_url1, '11.jpg')
	# g2 = gevent.spawn(download_img, img_url2, '22.jpg')
	# g3 = gevent.spawn(download_img, img_url3, '33.jpg')
	g4 = gevent.spawn(download_img, img_url4, '蓝莲花.m4a')
	# g5 = gevent.spawn(download_img, img_url5, '像风一样自由.m4a')
	# g6 = gevent.spawn(download_img, img_url5, '漫步.m4a')
	g7 = gevent.spawn(download_img, img_url7, '旅行.m4a')

	# 主线程等待所有的协程执行完成以后程序再退出
	gevent.joinall([g4,g7])
