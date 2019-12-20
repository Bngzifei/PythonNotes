"""
进程:通俗理解为一个运行的程序或者软件,进程是操作系统资源分配的基本单位
线程:是同一个程序里面的一部分

现实生活中的公司可以理解为一个进程(很多公司),公司提供办公资源(电脑,办公桌椅等)
真正干活的是员工,员工就是一个一个的线程.属于进程中的一部分.

"""

"""
注意:一个程序至少有一个进程,一个进程至少有一个线程.多线程可以完成多任务.



进程的状态:

工作中,任务数往往大于cpu的核数,即一定有一些任务正在执行,而另外一些任务在等待cpu进行执行,
因此导致有了不同的状态.


就绪:运行的条件都已满足,正在等待cpu执行.
执行:cpu正在执行某功能
等待态:等待某些条件满足,比如一个程序sleep了,此时就处于等待态.


进程与线程的关系:
一个进程默认有一个线程,进程里面可以创建线程,
线程是依附在进程里面的,没有进程就没有线程.


"""

"""进程的使用:

Process进程类的语法结构:
Process([group [,target[,name[,])

group:指定进程组,目前只能使用None
target:执行的目标任务名
name:进程名字
args:以元组方式给执行任务传参数
kwargs:以字典方式给执行任务传参数

Process创建实例对象的常用方法:
start():启动子进程实例(创建子进程)
join([timeout]):是否等待子进程执行结束,或等待多少秒
terminate():不管任务是否完成,立即终止子进程

Process创建的实例对象的常用属性:
name:当前进程的别名,默认为Process-N,N为从1开始递增的整数.
pid:当前进程的pid(进程号)

"""

"""多进程完成多任务代码:"""
# import multiprocessing  # 导入进程模块
# import time
#
#
# def run_proc():
# 	"""子进程要执行的代码"""
# 	while True:
# 		print('---2---')
# 		time.sleep(1)
#
#
# if __name__ == '__main__':
# 	# 创建子进程
# 	sub_process = multiprocessing.Process(target=run_proc)
# 	# 启动子进程
# 	sub_process.start()
# 	while True:
# 		print('---1---')
# 		time.sleep(11)

"""获取进程pid"""
# import multiprocessing
# import time
# import os
#
#
# def work():
# 	# 查看当前进程
# 	current_process = multiprocessing.current_process()
# 	print('work:', current_process)
# 	# 获取当前进程的编号
# 	print('work进程编号:', current_process.pid,os.getpid())  # 当前进程编号
# 	# 获取父进程的编号
# 	print('work父进程的编号:', os.getppid())  # ppid:parent pid:父进程pid
# 	for i in range(10):
# 		print('工作中')
# 		time.sleep(0.2)
# 		# 根据进程编号杀死对应的进程
# 		os.kill(os.getpid(), 9)
#
#
# if __name__ == '__main__':
# 	# 查看当前进程
# 	current_process = multiprocessing.current_process()
# 	print('main:', current_process)
# 	# 获取当前进程的编号
# 	print('main进程编号:', current_process.pid)
#
# 	# 创建子进程
# 	sub_process = multiprocessing.Process(target=work)
# 	# 启动进程
# 	sub_process.start()
#
# 	# 主进程执行打印信息操作
# 	for i in range(20):
# 		print('我在主进程中执行...')
# 		time.sleep(0.2)

"""给子进程指定的函数传递参数:"""

# import multiprocessing
#
#
# # 显示人员信息
# def show_info(name, age):
# 	print(name, age)
#
#
# if __name__ == '__main__':
# 	# 创建子进程
# 	sub_process = multiprocessing.Process(target=show_info, args=('古力娜扎', 18))  # 启动进程
# 	# 启动进程
# 	sub_process.start()
#
# 	# 创建子进程
# 	sub_process = multiprocessing.Process(target=show_info, args=('貂蝉', 28))  # 启动进程
# 	# 启动进程
# 	sub_process.start()

"""进程注意点:1.>进程之间不共享全局变量"""
# import multiprocessing
# import time
#
# # 定义全局变量
# my_list = list()  # [] 是一个空列表
# print(my_list)
#
#
# # 写入数据
# def write_data():
# 	for i in range(5):
# 		my_list.append(i)
# 		time.sleep(0.2)
# 	print('write_data:', my_list)
#
#
# # 读取数据
# def read_data():
# 	print('read_data:',my_list)
#
#
# if __name__ == '__main__':
# 	# 创建写入数据的进程
# 	write_process = multiprocessing.Process(target=write_data)
# 	read_process = multiprocessing.Process(target=read_data)
#
# 	write_process.start()
# 	# 主进程等待写入进程执行完成以后 再继续往下执行
# 	write_process.join()
# 	read_process.start()

"""注意:
创建子进程其实是对主进程进行拷贝,进程之间相互独立,访问的全局变量不是同一个,所以进程之间不共享全局变量

"""
"""主进程会等待所有的子进程执行完成后再退出"""
# import multiprocessing
# import time
#
#
# # 测试子进程是否执行完成以后主进程才能退出
# def work():
# 	for i in range(10):
# 		print('工作中...')
# 		time.sleep(0.2)
#
#
# if __name__ == '__main__':
# 	# 创建子进程
# 	work_process = multiprocessing.Process(target=work)
# 	work_process.start()
#
# 	# 让主进程等待1秒钟
# 	time.sleep(1)
# 	print('主进程执行完成了')
"""总结:主进程会等待所有的子进程执行完成后,程序再退出"""

"""销毁子进程:"""
# import multiprocessing
# import time
#
#
# # 测试子进程是否执行完成以后主进程 才能退出
# def work():
# 	for i in range(10):
# 		print('工作中...')
# 		time.sleep(0.2)
#
#
# if __name__ == '__main__':
# 	# 创建子进程
# 	work_process = multiprocessing.Process(target=work)
# 	# 设置守护主进程,主进程退出后子进程直接销毁,不再执行子进程的代码
# 	work_process.start()
# 	# 让主进程等待1秒钟
# 	time.sleep(1)
# 	print('主进程执行完成了啦!')
# 	# 让子进程直接销毁,表示终止执行,主进程退出之前,把所有的子进程直接销毁就可以了
#
# 	work_process.terminate()
# 总结: 主进程会等待所有的子进程执行完成以后,程序再退出

"""小结:
1.>进程之间不会共享全局变量

2.>主进程会等待所有的子进程执行完成后,程序再退出.
"""

"""进程间通信-Queue
1.Queue的使用:
可以使用multiprocessing模块的Queue实现多进程之间的数据传递,Queue本身是一个消息队列程序



"""
# import multiprocessing
# import time
#
# if __name__ == '__main__':
# 	# 创建消息队列,3:表示队列中最大的消息个数
# 	queue = multiprocessing.Queue(3)
# 	# 放入数据
# 	queue.put(1)
# 	queue.put('hello')
# 	queue.put([3, 5])
# 	# 总结:队列可以放入任意数据类型
# 	# 提示:如果队列满了,需要等待队列有空闲位置才能放入数据,否则一直等待
# 	queue.put((5,6))
# 	# 提示:如果队列满了,不等待队列有空闲位置,如果放入不成功直接奔溃
# 	# queue.put_nowait((5,6))
# 	# 建议:向队列放入数据统一使用put
#
# 	# 查看队列是否满了
# 	# print(queue.full())
# 	# 注意点:使用queue.empty()来判断队列是否空了不可靠
# 	# print(queue.empty())
#
# 	# 解决办法:1.加延时操作  2. 判断队列的个数,不使用empty
#
# 	if queue.qsize() == 0:
# 		print('队列为空')
# 	else:
# 		print('队列不为空')
#
#
# 	# 获取队列的个数
# 	size = queue.qsize()
# 	print(size)
#
# 	# 获取数据
# 	value = queue.get()
# 	print(value)
#
# 	# 获取队列的个数
# 	size = queue.qsize()
# 	print(size)
#
# 	# 获取数据
# 	value = queue.get()
# 	print(value)
#
# 	# 获取队列的个数
# 	size = queue.qsize()
# 	print(size)
#
# 	# 获取数据
# 	value = queue.get()
# 	print(value)
"""说明:初始化Queue()对象时(例如:q = Queue(),若括号中没有指定最大可接收的消息数量,或数量为负值,那么就代表可接受的消息数量没有上限
(直到内存的尽头)
	
	Queue.qsize():返回当前队列包含的消息数量
	Queue.empty():如果队列为空,返回True,反之False,注意这个操作时不可靠的.
	Queue.full():如果队列满了,返回True,反之False.
	Queue.get([block[,timeout]]):获取队列中的一条消息,然后将其从队列中移除,block
	默认值为True.

1.>如果block使用默认值,且没有设置timeout(单位秒),消息队列如果为空,此时程序将被阻塞(停在读取状态),直到从
消息队列读到消息为止,如果设置了timeout,则会等待timeout秒,若还没有读取到任何消息,则抛出
'Queue.Empty'异常.
2.>如果block值为False,消息队列如果为空,则会立刻抛出'Queue.Empty'异常.
Queue.get_nowait():相当于Queue.get(False)
Queue.put(item,[block[,timeout]]):将item消息写入队列,block默认值为True;

1.>如果block使用默认值,且没有设置timeout(单位秒),消息队列如果没有空间可写入,此时程序将被阻塞(停在写入状态),直到从消息
队列腾出空间为止,如果设置了timeout,则会等待timeout秒,若还没有空间,则抛出'Queue.Full'异常.

2.>如果block值为False,消息队列如果没有空间可写入,则会立刻抛出'Queue.Full'异常
	Queue.put_nowait(item):相当于Queue.put(item,False);

"""

"""消息队列Queue完成进程间通信:"""

# import multiprocessing
# import time
#
#
# # 写入数据
# def write_data(queue):
# 	for i in range(10):
# 		if queue.full():
# 			print('队列满了')
# 			break
# 		queue.put(i)
# 		time.sleep(0.2)
# 		print(i)
#
#
# # 读取数据
# def read_data(queue):
# 	while True:
# 		# 加入数据从队列取完了,那么跳出循环
# 		if queue.qsize() == 0:
# 			print('队列空了')
# 			break
# 		value = queue.get()
# 		print(value)
#
#
# if __name__ == '__main__':
# 	# 创建消息队列
# 	queue = multiprocessing.Queue(5)
# 	# 创建写入数据的进程
# 	write_process = multiprocessing.Process(target=write_data, args=(queue,))
# 	# 创建读取数据的进程
# 	read_process = multiprocessing.Process(target=read_data, args=(queue,))
#
# 	# 启动进程
# 	write_process.start()
# 	# 主进程等待写入进程执行完成以后代码再继续往下执行
# 	write_process.join()
# 	read_process.start()

"""小结:从队列取值使用get()方法,向队列放入值使用put方法

消息队列判断队列是否为空不可靠,可以使用延时个根据个数进行判断.

"""

"""

xrange()

注意:Python3中没有xrange()这个了,Py2中这个东西和range()一样,只是返回值是一个生成器类型.range返回的是一个数组.
"""
# y = (x for x in range(10))
# print(y)

# y= range(100)
# print(type(y))


"""
进程池Pool:池子里面放的是进程,进程池会根据任务执行情况自动创建进程,而且尽量少创建进程,合理
利用进程池中的进程完成多任务.

当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态生成多个进程,
但如果是上百个甚至上千个目标,手动的去创建进程的工作量巨大,此时就可以用multiprocess模块
提供的Pool方法.

初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没有满,那么就会创建一个
新的进程用来执行该请求,但如果池中的进程数已经达到指定的最大值,那么该请求就会等待,直到池中有进程结束,
才会用之前的进程来执行新的任务.


进程池同步执行任务:表示进程池中的进程在执行任务的时候,一个执行完成另外一个才能执行,如果没有执行完成
会等待上一个进程执行.


"""
"""进程池同步执行任务:"""

# import multiprocessing
# import time
#
#
# def work():
# 	print('复制中...', multiprocessing.current_process().pid)
# 	time.sleep(0.5)
#
#
# if __name__ == '__main__':
# 	# 创建进程池
# 	pool = multiprocessing.Pool(3)  # 设置进程池中进程的最大个数
# 	# 模拟大批量任务,让进程池去执行
# 	for i in range(5):
# 		# 循环让进程池执行对应的work任务
# 		# 同步执行任务,一个任务执行完成后另外一个任务才能执行
# 		pool.apply(work)

"""进程池异步执行任务
表示进程池中的进程同时执行任务,进程之间不会等待


"""

# 进程池:池子里面放有进程,进程池会根据执行情况自动创建进程,
# 而且尽量少的创建进程.合理利用进程池中的进程完成多任务
# import multiprocessing
# import time
#
#
# def work():
# 	print('复制中...', multiprocessing.current_process().pid)
# 	# 获取当前进程的守护状态
# 	# print(multiprocessing.current_process().daemon)
# 	time.sleep(0.5)
#
#
# if __name__ == '__main__':
# 	# 创建进程池
# 	pool = multiprocessing.Pool(3)
#
# 	for i in range(5):
# 		# pool.apply(work)  # 这是同步
# 		pool.apply_async(work)  # 这是异步
#
# 	# 关闭进程池 ,意思是告诉主进程以后不会有新的任务添加进来
# 	pool.close()
# 	# 主进程等待进程池执行完成以后程序再退出
# 	pool.join()  # 等待结束

"""小结:
apply:阻塞调用函数
apply_async:非阻塞调用函数

close():关闭Pool,使其不再接受新的任务
terminate:不管任务是否完成,立即终止
join:主进程阻塞,等待子进程的退出,必须在close和terminate之后使用







"""

"""进程和线程的对比:

1.>功能对比:
	进程:能够完成多任务,比如,一台机器上面能够同时运行多个qq
	线程:能够完成多任务,比如,一个qq上面的多个聊天窗口
2.>定义对比:
	进程是系统进行资源分配的基本单位,每启动一个进程操作系统都需要为其分配运行资源.
	线程是运行程序中的一个分支,是cpu的调度单位
	
	总结:进程 ----> os的资源分配单位
		 线程 ----> cpu调度的基本单位
		 
3.>关系对比:
	线程是依附在进程里面的,没有进程就没有线程.
	一个进程默认提供一条线程,进程可以创建多个线程.
4.>区别:
	进程之间不共享全局变量
	线程之间共享全局变量,但是要注意资源竞争的问题,解决方法:-->互斥锁或者线程同步
	创建进程的资源开销要比创建线程的资源开销要大.
	进程是操作系统os资源分配的基本单位,线程是cpu调度的基本单位
	线程不能够独立运行,必须依存在进程中.
	多进程开发比单进程多线程开发稳定性要强.
	
5.>优缺点:
	多进程:
		优点:可以使用多核
		缺点:资源开销大
	
	多线程:
		优点:资源开销小
		缺点:不能使用多核


"""

"""文件夹拷贝器:-多任务

要求:使用进程池完成文件夹拷贝器,文件夹里面的文件能够实现多个文件一起拷贝

"""

# import multiprocessing
# import os
# import shutil
#
#
# def copy_work(src_dir, dst_dir, file_name):
# 	# 查看进程对象
# 	pid = multiprocessing.current_process().pid
# 	print(pid)
#
# 	# 拼接源文件的路径
# 	src_file_path = src_dir + '/' + file_name
# 	# 拼接目标文件的路径
# 	dst_file_path = dst_dir + '/' + file_name
#
# 	# 打开目标文件,来存读取到的文件数据
# 	with open(dst_file_path, 'wb') as dst_file:
# 		# 打开源文件读取文件中的数据
# 		with open(src_file_path, 'rb') as src_file:
# 			while True:
# 				# 读取数据
# 				src_file_date = src_file.read(1024)
#
# 				if src_file_date:  # 如果读到的数据不为空
# 					# 写入到目标文件里面
# 					dst_file.write(src_file_date)
# 				else:
# 					break
#
#
# if __name__ == '__main__':
# 	# 源目录
# 	src_dir = 'test'
# 	# 目标目录
# 	dst_dir = 'F:/黑马Python20期就业班/预习/目标文件/'
#
# 	# 判断文件夹是否存在
# 	if os.path.exists(dst_dir):
# 		# 存在则删除文件夹及文件夹里面的所有文件
# 		shutil.rmtree(dst_dir)
#
# 	# 创建目标文件夹
# 	os.mkdir(dst_dir)
# 	# 获取源目录里面的文件列表
# 	file_name_list = os.listdir(src_dir)
# 	# 创建进程池
# 	pool = multiprocessing.Pool(3)
# 	# 遍历文件夹里面的文件名
# 	for file_name in file_name_list:
# 		# 使用进程池执行拷贝任务
# 		pool.apply_async(copy_work, (src_dir, dst_dir, file_name))
#
# 	# 关闭进程池
# 	pool.close()
# 	# 主进程等待进程池执行完成以后程序再退出
# 	pool.join()
"""
小结:进程池在执行任务的时候会尽量少创建进程,合理利用现有进程完成多任务,这样可以减少资源开销


"""