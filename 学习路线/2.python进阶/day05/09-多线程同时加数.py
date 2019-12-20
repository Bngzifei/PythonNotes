"""
验证多线程是否共享全局变量
"""
import threading
import time

g_number = 0


def func1():
	"""线程1 对全局变量 + 11"""
	for i in range(10000):
		global g_number
		g_number += 1  # 内部使用外部,需要声明全局变量
		print('线程1:', g_number)


def func2():
	"""线程2  获取群居变量的值"""
	for i in range(10000):
		global g_number
		g_number += 1
		print('线程2:', g_number)


if __name__ == '__main__':
	thd1 = threading.Thread(target=func1)
	thd2 = threading.Thread(target=func2)
	thd1.start()  # 1和2几乎同时启动
	thd2.start()

	thd1.join()
	thd2.join()
	print('最后的结果是%d' % g_number)
"""
线程独立运行,同时去修改一个全局变量,彼此不知道对方对这个变量修改了啥,
所以会产生数据竞争的现象.


相互之间没沟通,所以会在公共资源上产生竞争,错误

资源竞争/数据竞争:原因:多个线程同时修改一个共享的全局资源.




同步:保持秩序 --->称之为多线程同步 手段:互斥锁  类比厕所的问题,有人/没人等等


给访问的公共资源加锁,别人就不能访问,用完了再去解锁.

锁定的资源--->称之为临界区资源

对共享的数据进行锁定,保证同一时刻只能有一个线程使用.
互斥锁状态:锁定/未锁定


"""