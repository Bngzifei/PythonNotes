print('----------------')
"""
由于GIL的存在,Python的多线程并不是真正的多线程,如果想要充分的使用多核cpu的资源,在Python中大部分情况需要使用多进程.
multiprocessing包是Python中的多进程管理包,和threading.Thread类似,它可以利用multiprocess.Process对象来创建一个进程,
该进程可以运行在python程序内部编写的函数,该Process对象与Thread对象的用法相同, 
也有start(),run(),join()的方法.此外multiprocess包中也有Lock/Event/Semaphore/Condition类<这些对象可以像多线程那样,
通过参数传递给各个进程>,用以同步进程,其用法与threading包中的同名类一致.所以,multiprocessing的很大一部分与threading
使用同一套API,只不过换到了多进程的情境.

"""
# from multiprocessing import Process
# import time
#
#
# def f(name):
# 	time.sleep(1)
# 	print('hello', name, time.ctime())
#
#
# if __name__ == '__main__':
# 	p_list = []
#
# 	for i in range(3):
# 		p = Process(target=f, args=('alex',))
# 		p_list.append(p)
# 		p.start()
#
# 	for i in p_list:
# 		i.join()
# 	print('end')

"""
hello alex Sat Sep 22 17:24:19 2018
hello alex Sat Sep 22 17:24:19 2018
hello alex Sat Sep 22 17:24:19 2018
end

理论上 输出的时间绝对是一样的,绝对的并行.实现了在同一时刻一起执行相应的任务

"""
# ---------------------调用方式2:重写一个类,然后继承----------------------->

# from multiprocessing import Process
# import time
#
#
# class MyProcess(Process):
# 	"""自定义进程类"""
#
# 	# def __init__(self):
# 	# 	"""调用重写的父类方法"""
# 	# 	super(MyProcess, self).__init__()
#
# 	def run(self):
# 		time.sleep(1)
# 		# self.name --->  MyProcess-2 指的是进程的名字
# 		print('hello', self.name, time.ctime())
#
#
# if __name__ == '__main__':
# 	p_list = []
#
# 	for i in range(3):
# 		p = MyProcess()  # 创建
# 		p.daemon=True
# 		p_list.append(p)
# 		p.start()  # 启动
#
# 	# for i in p_list:
# 	# 	i.join()  # 主进程等待子进程,直到子进程执行完
# 	print('end')

# --------------------------示例:------------------------------->
import os
from multiprocessing import Process
import time


def info(title):
	print('title:', title)
	print('parent process id:', os.getppid())  # 这个是pycharm这个软件的进程id,可以通过任务管理器进行验证,一旦开启了,这个id号就不会变化,除非关闭pycharm之后再重启.
	print('process id:', os.getpid())  # 解释器运行的进程,子进程,就是.py这个文件运行程序


def f(name):

	info('function f')
	print('hello', name)


if __name__ == '__main__':
	info('main process line')
	time.sleep(1)
	print('-----------')
	p = Process(target=info,args=('yuan',))
	p.start()
	p.join()

# 输出结果:
# title: main process line
# parent process id: 5440
# process id: 8092
# -----------
# ----------------
# title: yuan
# parent process id: 8092
# process id: 2792

# -------------------------------进程间通信:1.Queue 2.pipe 3.Managers-------->
"""
Queue和pipe只是实现了双方数据交互,并没有实现数据共享,即一个进程去更改另一个进程的数据.
"""
