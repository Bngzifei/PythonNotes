import threading

g_number = 0


def func1(lock):
	"""线程1 对全局变量 + 11"""

	for i in range(10000):
		global g_number
		# 申请加锁  如果未锁定,就可以直接占有
		# 如果已经被锁定,那就会阻塞等待,知道别人解锁
		lock.acquire()  # 申请锁
		g_number += 1  # 内部使用外部,需要声明全局变量
		# 用完锁之后要释放<解锁>
		lock.release()
		print('线程1:', g_number)


def func2(lock):
	"""线程2  获取全局变量的值"""
	for i in range(10000):
		global g_number
		lock.acquire()  # 申请锁
		g_number += 1
		lock.release()  # 解锁
		print('线程2:', g_number)


if __name__ == '__main__':
	# 创建互斥锁  一般锁名叫 mutex,能够保证同一时间点只有一个线程占有锁
	lock1 = threading.Lock()

	thd1 = threading.Thread(target=func1, args=(lock1,))
	thd2 = threading.Thread(target=func2, args=(lock1,))
	thd1.start()  # 1和2几乎同时启动,时间差可以忽略不计
	thd2.start()
	# 加入等待线程结束的队列
	thd1.join()
	thd2.join()
	print('最后的结果是:%d' % g_number)


"""
好处:确保完整运行

坏处:降低了运行效率

"""
