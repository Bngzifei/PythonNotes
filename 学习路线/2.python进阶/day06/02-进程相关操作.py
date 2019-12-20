import multiprocessing
import time
import os


def func(age, height, love):
	"""子进程会执行 的函数"""
	print('身高:%d,年龄:%d,爱好是:%s' % (height, age, love))
	for i in range(10):
		# os.getpid() 获取当前进程的PID
		# os.getppid() 获取当前进程的父进程的PID  parent process id
		print('子进程的PID:%s,父进程的PID:%s' % (os.getpid(), os.getppid()))

		time.sleep(1)


# 默认的就是主进程
def main():
	# 这是主进程运行的范围

	pro = multiprocessing.Process(target=func, args=(18, 175), kwargs={'love': '抽烟喝酒'})
	# target里面的就是子进程运行的,kwargs是用来指定某个具体的项的值是多少.即相当于函数的参数的名字是固定的,不能更改的时候才考虑使用kwargs进行传参操作.

	# pid为None说明子进程没有被创建,也说明了start()方法的作用:创建并启动子进程.
	print('子进程pid', pro.pid)
	# 创建和启动子进程
	pro.start()

	# 子进程的pid
	print('子进程pid', pro.pid)
	# 查看子进程名称
	print('子进程名称:', pro.name)  # Process-1
	# 等待子进程退出,参数为等待的秒数,如果参数不写,表示一直等待
	pro.join(1)  # []内部参数是可选可不选
	# 查看子进程运行状态
	print('子进程状态', pro.is_alive())
	# 立即终止子进程
	pro.terminate()  # 终止之后不能立即退出,要使用join等一会儿,不能立即进行状态判断
	# time.sleep(0.6)
	print('kill -9 后...')
	pro.join()
	# 子进程状态
	print('子进程状态', pro.is_alive())  # 主进程发送kill 信号给os,os才会去执行杀死子进程的操作,但是什么时候去执行,不确定.
	print('当前进程的PID', multiprocessing.current_process().pid)
	# 查看当前进程的状态
	print('当前进程的状态:', multiprocessing.current_process().is_alive())  # 主进程
	print('子进程刚刚退出')


if __name__ == '__main__':
	main()

"""
start的作用:

创建和启动子进程

不执行start就不会有子进程,也不会有pid


"""
