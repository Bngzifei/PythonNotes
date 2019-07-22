"""
开很多进程-->资源消耗太大
不开-->时间消耗太大
所以选择了一个折中的方案
设置一个池子,里面放最大的进程数n:那么最大 并发数就是5

"""
from multiprocessing import Process, Pool

import time, os


def foo(i):
	time.sleep(1)
	print(i)
	print('son:', os.getpid())
	return 'hello %s' % i


def bar(arg):  # 就是接收return的值
	"""回调函数"""
	# logger()
	# print('hello')
	# print('bar:',os.getpid())
	# # print(os.getppid())
	print(arg)


if __name__ == '__main__':  # 注意:在进程中如果不加这个,会导致主进程不明显,直接报错

	pool = Pool(5)  # 开5个进程,最大是5.但是如果不写,默认是按照电脑的cpu核心数来执行,比如,我自己的电脑是4核心的,这里就会4个4个的执行.如果写了5,那么就是5个5个的执行.
	# 实际上写了5也是4颗cpu并行的执行4个任务,其中剩下的1个任务在切换,只不过是切换的很快,我们感觉不出来罢了.
	print('main:', os.getpid())
	print('------------')
	# bar(1)
	for i in range(100):  # 开10个任务
		# 每次出5个任务,相当于一次搬了5块
		# pool.apply_async(func=foo, args=(i,))  # 类似线程的target=func

		# 回调函数:就是某个动作执行成功之后,再去执行的函数就是回调函数
		# bar 是在主进程里面调用的
		pool.apply_async(func=foo, args=(i,), callback=bar)
	# 意思就是每次for执行结束之后就会去掉bar函数
	# 效果就是每次for执行完以后会跟一个bar的hello效果

	pool.close()  # 记住,进程池里面是先close后join.顺序是固定的
	pool.join()  # 一定先关闭入口,然后等已经进去的进程执行结束.
	print('end')

"""
回调函数好处:
为啥在主进程里面调用?
例子:数据库操作打印日志
不要让100个子进程一起都去打印日志操作<这个是共用的功能,都需要日志打印>
所以放在回调函数里面,让主进程去调用

"""
