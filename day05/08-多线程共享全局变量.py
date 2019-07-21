"""
验证多线程是否共享全局变量
"""
import threading
import time

g_number = 100


def func1():
	"""线程1 对全局变量 + 11"""
	time.sleep(1)
	global g_number
	g_number += 11  # 内部使用外部,需要声明全局变量
	print('线程1:', g_number)


def func2():
	"""线程2  给全局变量 + 3"""
	for i in range(10):

		global g_number
		g_number += 3
		print('线程2:', g_number)
		time.sleep(1)


if __name__ == '__main__':
	threading.Thread(target=func1).start()
	threading.Thread(target=func2).start()

"""
结论:

同一个程序内部的多个线程 -----> 共享全局变量

线程是程序内部的一条执行线索<流程>

其中一个线程修改了全局变量,其余线程使用这个全局变量的时候会有影响 ----> 即这个全局变量的值会发生相应的改变

"""
