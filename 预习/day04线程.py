"""
多任务:在同一时间内执行多个任务,每个任务可以理解成现实生活中干的每个活.

并发:指的是任务数多于cpu核数,通过操作系统的各种任务调度算法,实现用多个任务一起执行(
实际上总有一些任务不在执行,因为切换任务的速度相当快,只是看上去一起执行而已)

并行:指的是任务数小于等于cpu核数,即任务真的是一起执行的.


线程:线程就是在程序运行过程中,执行程序代码的一个分支,每个运行的程序至少都有一个线程.
"""

"""单线程执行"""
#
# import time
#
#
# def sing():
# 	for i in range(3):
# 		print('正在唱歌...%d' % i)
# 		time.sleep(1)
#
#
# def dance():
# 	for i in range(3):
# 		print('正在跳舞...%d' % i)
# 		time.sleep(1)
#
#
# if __name__ == '__main__':
# 	sing()
# 	dance()

"""多线程执行:"""
# import threading  # 导入线程模块
# import time
#
#
# def sing():
# 	"""唱歌"""
# 	print('sing当前执行的线程为:',threading.current_thread())
# 	for i in range(3):
# 		print('正在唱歌...%d' % i)
# 		time.sleep(2)
#
#
# def dance():
# 	"""跳舞"""
# 	print('dance当前执行的线程为:', threading.current_thread())
# 	for i in range(3):
# 		print('正在 跳舞...%d' % i)
# 		time.sleep(1)
#
#
# if __name__ == '__main__':  # 实现了轮询的效果,即一会儿是跳舞,一会儿是唱歌,不是那种执行完唱歌再来执行跳舞
# 	# 创建唱歌,跳舞的线程
# 	sing_thread = threading.Thread(target=sing)
# 	dance_thread = threading.Thread(target=dance)
#
# 	# 开启线程,启动线程使用start()方法
# 	sing_thread.start()
# 	dance_thread.start()

"""多任务执行带有参数的任务:"""
# import threading
# import time
#
#
# def sing(num):
# 	for i in range(num):
# 		print('正在唱歌...%d' % i)
# 		time.sleep(1)
#
#
# def dance(num):
# 	for i in range(num):
# 		print('正在跳舞...%d' % i)
# 		time.sleep(1)
#
#
# if __name__ == '__main__':
# 	# target:线程执行的函数名
# 	# args:表示以元组的方式给函数传递参数
# 	# kwargs:表示以字典的方式给函数传递参数
#
#
# 	# 创建线程
# 	sing_thread = threading.Thread(target=sing, args=(3,))
# 	dance_thread = threading.Thread(target=dance, kwargs={'num': 3})
#
# 	# 开启线程
# 	sing_thread.start()
# 	dance_thread.start()

"""查看获取线程列表:"""
# import threading
# import time
#
#
# def sing(num):
# 	print('sing:', threading.current_thread())
# 	for i in range(num):
# 		print('正在唱歌...%d' % i)
# 		time.sleep(1)
#
#
# def dance(num):
# 	print('dance:', threading.current_thread())
# 	for i in range(num):
# 		print('正在跳舞...%d' % i)
# 		time.sleep(1)
#
#
# if __name__ == '__main__':
# 	# target:线程执行的函数名
# 	# args:表示以元组的方式给函数传递参数
# 	# kwargs:表示以字典的方式给函数传递参数
#
# 	# 获取当前执行代码的线程
# 	print('main', threading.current_thread())
#
# 	# 获取当前程序活动线程的列表
# 	thread_list = threading.enumerate()
# 	print('111:', thread_list, len(thread_list))
#
# 	# 创建线程,表示创建的子线程执行唱歌任务
# 	sing_thread = threading.Thread(target=sing, args=(3,))
# 	# 执行跳舞任务
# 	dance_thread = threading.Thread(target=dance, kwargs={'num': 3})
#
# 	# 启动线程
# 	sing_thread.start()
# 	dance_thread.start()
#
# 	# 只有线程启动了,才能加入到活动线程列表中
# 	thread_list = threading.enumerate()
# 	print('333:', thread_list, len(thread_list))

"""
总结:1.>使用多线程可以完成多任务
	 2.>只有线程启动,线程才会加入到活动线程列表

"""
"""线程注意点:
1.线程之间执行是无序的.
2.主线程会等待所有的子线程结束后才结束
3.守护主线程


"""

"""1.线程之间执行是无序的"""

# import threading
# import time
#
#
# def task():
# 	time.sleep(1)
# 	print('当前线程:', threading.current_thread().name)
#
#
# if __name__ == '__main__':
# 	for _ in range(5):
# 		# 创建
# 		sub_thread = threading.Thread(target=task)
# 		# 启动
# 		sub_thread.start()


"""2.主线程会等待所有的子线程结束后才结束"""

# import threading
# import time
#
#
# def show_info():
# 	for i in range(5):
# 		print('test:', i)
# 		time.sleep(0.5)
#
#
# if __name__ == '__main__':
# 	sub_thread = threading.Thread(target=show_info)
# 	sub_thread.start()
# 	time.sleep(1)
# 	print('over')

"""守护主线程"""

# import threading
# import time
#
#
# def show_info():
# 	for i in range(5):
# 		print('test:', i)
# 		time.sleep(0.5)
#
#
# if __name__ == '__main__':
# 	# 创建子线程守护主线程
# 	# daemon = True守护主线程
# 	sub_thread = threading.Thread(target=show_info, daemon=True)
# 	# 设置成为守护主线程,主线程退出后子线程直接销毁不再执行子线程的代码
# 	# 守护主线程方式2
# 	# sub_thread.setDaemon(True)
# 	sub_thread.start()
# 	# 主线程延时1秒
# 	time.sleep(1)
# 	print('over')

"""
总结:1.>线程之间执行时是无序的,
	2.>主线程会等待所有的子线程结束后才结束,如果需要可以设置守护主线程

"""

"""自定义线程代码:"""

# import threading
#
#
# class MyThread(threading.Thread):
# 	# 通过构造方法去接收任务的参数
# 	def __init__(self, info1, info2):
# 		# 调用父类重写方法
# 		super(MyThread, self).__init__()
# 		self.info1 = info1
# 		self.info2 = info2
#
# 	# 定义 自定义线程相关的任务
# 	def test1(self):
# 		print(self.info1)
#
# 	def test2(self):
# 		print(self.info2)
#
# 	# 通过run方法执行相关任务
# 	def run(self):
# 		self.test1()
# 		self.test2()
#
#
# # 创建自定义线程
# my_thread = MyThread('测试1', '测试2')
# my_thread.start()

"""
小结:1.>自定义线程不能指定target,因为自定义线程里面的任务都统一在run方法里面执行
	2.> 启动线程统一调用start()方法,不要直接调用run方法,因为这样不是使用子线程去执行任务.
"""

"""多线程:共享全局变量"""
# import threading
# import time
#
# # 定义全局变量
#
# my_list = list()
#
#
# # 写入数据任务
# def write_data():
# 	for i in range(5):
# 		my_list.append(i)
# 		time.sleep(0.1)
# 	print('write_data', my_list)
#
#
# # 读取数据任务
# def read_data():
# 	print('read_data', my_list)
#
#
# if __name__ == '__main__':
# 	# 创建写入数据的线程
# 	write_thread = threading.Thread(target=write_data)
# 	# 创建读取数据的线程
# 	read_thread = threading.Thread(target=read_data)
#
# 	write_thread.start()
#
# 	# 主线程 等待写入线程执行完成以后代码在继续往下执行
# 	write_thread.join()
# 	print('开始读取数据啦')
# 	read_thread.start()

"""总结:多线程共享全局变量,很方便在多个线程之间共享数据"""

"""多线程-共享全局变量问题"""

"""1.多线程同时对全局变量进行操作"""

# import threading
#
# # 定义全局变量
#
# g_num = 0
#
#
# # 循环一次给全局变量加1
# def sum_num1():
# 	for i in range(1000000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum1:', g_num)
#
#
# # 循环一次给全局变量加1
# def sum_num2():
# 	for i in range(1000000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum2:', g_num)
#
#
# if __name__ == '__main__':
# 	# 创建两个线程
# 	first_thread = threading.Thread(target=sum_num1)
# 	second_thread = threading.Thread(target=sum_num2)
#
# 	# 启动线程
# 	first_thread.start()
# 	second_thread.start()

"""注意:多线程同时对全局变量操作数据发生了错误"""
"""
多线程同时操作全局变量导致数据可能出现错误的原因分析
两个线程都要对全局变量g_num进行加一运算,但是由于是多线程同时操作,有可能出现
下面情况:

"""

"""全局变量数据错误的解决办法"""
"""
线程同步:保证同一时刻只能有一个线程去操作全局变量同步:就是协同步调,按预定的先后次序进行运行.如:你说完,我再说,好比现实生活中的对讲机

线程同步的方式:1.>线程等待(join)2.>互斥锁



"""
# 线程等待的代码


# import threading
#
# # 定义全局变量
# g_num = 0
#
#
# # 循环10000000次每次给全局变量加1
# def sum_num1():
# 	for i in range(10000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum1:', g_num)
#
#
# # 循环10000000次每次给全局变量加1
# def sum_num2():
# 	for i in range(10000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum2:', g_num)
#
#
# if __name__ == '__main__':
# 	# 创建两个线程
# 	first_thread = threading.Thread(target=sum_num1)
# 	second_thread = threading.Thread(target=sum_num2)
#
# 	# 启动线程
# 	first_thread.start()
# 	# 主线程等待第一个线程执行完成以后代码再继续执行,让其执行第二个线程
# 	# 线程同步,一个任务执行完成以后另外一个任务才能执行,同一个时刻只有一个任务在执行
# 	first_thread.join()
# 	second_thread.start()
"""
结论:多个线程同时对同一个全局变量进行操作,会有可能出现资源竞争数据错误的问题
线程同步方式可以解决资源竞争数据错误问题,但是这样由多任务变成了单任务.
"""

"""互斥锁:

1.>对共享数据进行锁定,保证同一时刻只能有一个线程去操作
注意:抢到锁的线程先执行,没有抢到锁的线程需要等待,等锁用完后需要释放,然后其他等待的线程再去抢这个锁
,哪个线程抢到哪个线程再执行
2.>具体哪个线程抢到这个锁我们决定不了,是由cpu调度决定的.

线程同步能够保证多个线程安全访问竞争资源,最简单的同步机制是引入互斥锁.

互斥锁为资源引入一个状态:锁定/非锁定

互斥锁保证了每次只有一个线程进行写入操作,从而保证了多线程情况下数据的正确性.

threading模块中定义了Lock变量,这个变量本质上是一个函数,可以方便的处理锁定.


"""

# import threading
# # 创建锁
# mutex = threading.Lock()
#
# # 锁定
# mutex.acquire()
#
# # 释放
# mutex.release()


"""
注意:1.>如果这个锁之前是没有上锁的,那么acquire不会堵塞
2.>如果在调用acquire对这个锁上锁之前 ,它 已经被其他线程上了锁,那么此时axquire会堵塞,
直到这个锁被解锁为止.


"""

"""示例:使用互斥锁完成2个线程对同一个全局变量各加100万次的操作"""

# import threading
#
# # 定义全局变量
# g_num = 0
#
# # 创建互斥锁
# lock = threading.Lock()
#
#
# # 循环一次给全局变量加1
# def sum_num1():
# 	# 上锁
# 	lock.acquire()
# 	for i in range(1000000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum1:', g_num)
#
# 	# 释放锁
# 	lock.release()
#
#
# # 循环一次给全局变量加1
# def sum_num2():
# 	# 上锁
# 	lock.acquire()
# 	for i in range(1000000):
# 		global g_num
# 		g_num += 1
#
# 	print('sum2:', g_num)
#
# 	# 释放锁
# 	lock.release()
#
#
# if __name__ == '__main__':
# 	# 创建两个线程
# 	first_thread = threading.Thread(target=sum_num1)
# 	second_thread = threading.Thread(target=sum_num2)
#
# 	# 启动线程
# 	first_thread.start()
# 	second_thread.start()

"""
提示:加上互斥锁,哪个线程抢到这个锁我们决定不了,哪个线程抢到就哪个执行,没抢到的要等待

加上互斥锁多任务瞬间变成单任务,性能会下降,也就是说同一时刻只能有一个线程去执行.


使用互斥锁的目的 :能够保证多个线程访问共享数据不会出现资源竞争及数据错误

上锁.解锁过程:
当一个线程调用锁的accquire()方法获得锁时,锁就进入'locked'状态.

每次只有一个线程可以获得锁,如果此时另一个线程试图获得这个锁,该线程就会变为'blocked'
状态,成为阻塞,直到拥有锁的线程调用锁的release()方法释放锁之后,锁进入unblocked状态.

线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁,并使得该线程进入运行状态.

总结:

锁的好处:确保了某段关键代码只能由一个线程从头到尾完整地执行

锁的坏处:多线程执行变成了包含所得某段代码实际上只能以单线程模式执行,效率就大大降低了.
锁使用不好就容易出现死锁情况.

"""

"""死锁:

就是一直等待对方释放锁的情景

"""

"""死锁示例:"""

# import threading
# import time
#
# # 创建互斥锁
# lock = threading.Lock()
#
#
# # 根据下标去取值,保证同一时刻只能有一个线程去取值
# def get_value(index):
# 	# 上锁
# 	lock.acquire()
# 	print(threading.current_thread())
# 	my_list = [3, 6, 8, 1]
# 	# 判断下标释放越界
# 	if index >= len(my_list):
# 		print('下标越界:', index)
# 		return
# 	value = my_list[index]
# 	print(value)
# 	time.sleep(0.2)
# 	lock.release()
#
#
# if __name__ == '__main__':
# 	# 模拟大量线程去执行取值操作
# 	for i in range(30):
# 		sub_thread = threading.Thread(target=get_value, args=(i,))
# 		sub_thread.start()


"""避免死锁:在合适的地方释放锁"""

# import threading
# import time
#
# # 创建互斥锁
# lock = threading.Lock()
#
#
# # 根据下标去取值,保证同一时刻只能有一个线程去取值
# def get_value(index):
# 	# 上锁
# 	lock.acquire()
# 	print(threading.current_thread())
# 	my_list = [3, 6, 8, 1]
# 	# 判断下标释放越界
# 	if index >= len(my_list):
# 		print('下标越界:', index)
# 		# 当下标越界需要释放锁,让后面的线程还可以取值
# 		lock.release()
# 		return
# 	value = my_list[index]
# 	print(value)
# 	time.sleep(0.2)
# 	lock.release()
#
#
# if __name__ == '__main__':
# 	# 模拟大量线程去执行取值操作
# 	for i in range(30):
# 		sub_thread = threading.Thread(target=get_value, args=(i,))
# 		sub_thread.start()

