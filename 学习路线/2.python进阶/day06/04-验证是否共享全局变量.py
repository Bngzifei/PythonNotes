import multiprocessing
import time

g_number = 0


def func():
	global g_number  # 函数内部需要使用外部变量值的时候,需要声明这个变量是全局变量,否则就是和外部变量名同名的一个局部变量.
	g_number += 100
	for i in range(3):
		print('子进程', g_number)
		time.sleep(1)


if __name__ == '__main__':
	# 资源分配的基本单位  ---> 进程间是独立的数据空间  ---> 多进程之间不共享全局资源
	multiprocessing.Process(target=func).start()
	for i in range(3):
		print('主进程', g_number)
		time.sleep(1)

"""

结论:主进程和子进程之间不共享全局资源

多进程  不共享全局资源

父子之间是独立的地址
主进程创建子进程:将主进程的资源(除了PID)直接拷贝了一份给子进程.

"""
