"""
需求:参数传入0 希望时间用整数显示,参数传入1 用浮点数显示
"""
import time


def get_run_time(flag):
	"""装饰器工厂函数"""

	def get_time(func):
		"""装饰器函数:对函数运行时间进行统计"""
		print('in get_time')

		def inner(*args, **kwargs):
			t1 = time.time()
			res = func(*args, **kwargs)
			t2 = time.time()
			if flag == 0:
				print('运行了%d s' % (t2 - t1))
			else:
				print('运行了%f s' % (t2 - t1))
			return res

		return inner

	return get_time


# 装饰器工厂函数的作用:
# 1.>接收装饰器函数所需要但是又不能直接接受的参数---->接收参数
# 2.>生产装饰器对象---->产生装饰器函数

# 关联: 装饰器工厂内部是装饰器函数
# 真正执行过程:
# 1.> get_time = get_run_time(参数)
# 2.> @get_time 对func1函数进行装饰  func1 = get_time(func1)
@get_run_time(0)  # 这句话的返回值是get_time这个函数名
def func1(num, age=18):
	for i in range(3):
		time.sleep(1)
		print('in func', num, age)


# @get_run_time(1) 注意:这个要分开看    f1 = get_run_time(1) 这是一个整体,函数调用,然后返回一个值
# @f1 这才是真正的装饰器函数开始了

func1(89)

"""
问题:
1.>装饰器工厂函数是装饰器函数吗?
不是,工厂内部定义了装饰器函数,并且return装饰器函数的引用
2.>装饰器工厂函数和装饰器的关系?
工厂的返回值是装饰器函数的引用.它的作用就是创建一个装饰器函数的对象<或者叫地址引用更合适>
"""
