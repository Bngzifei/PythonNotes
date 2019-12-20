import os
import multiprocessing
import time


def func():
	for i in range(100):
		print('第%d个的PID:%s' % (i, os.getpid()))
		print('*' * 30)
		time.sleep(1)


if __name__ == '__main__':
	# 创建并启动5个子进程
	for i in range(50):
		multiprocessing.Process(target=func).start()
	print('-' * 30)

"""
注意:虽然输出结果看起来各个进程之间的执行顺序是有序的,但是实际上无序的,只是因为我们电脑cpu核数的原因导致
这种无序执行的效果不明显,如果是多核且启动的子进程数目很多,这种现象就会非常明显.

结论:多进程的执行顺序是无序的(和cpu的核数有关,多核这个现象更明显)

"""
