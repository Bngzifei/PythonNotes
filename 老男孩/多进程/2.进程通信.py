# ----------------方式1:进程队列multiprocessing.Queue()----------------------->
# import multiprocessing
# import time
#
#
# def foo(q):
# 	"""子进程执行放操作"""
# 	time.sleep(1)
# 	print('子进程id:',id(q))
# 	q.put(123)
# 	q.put('yuan')
#
#
# if __name__ == '__main__':
#
# 	# q = queue.Queue()  # 线程队列
# 	q = multiprocessing.Queue()  # 进程队列
# 	p = multiprocessing.Process(target=foo, args=(q,))
# 	p.start()
# 	# p.join()
# 	print('主进程id:',id(q))
# 	# 主进程执行取操作,因为一开始队列里面是空的,取不到值,所以要进行阻塞等待.
# 	print(q.get())
# 	print(q.get())

# --------------------方式2:进程管道pipe--------------------->
# from multiprocessing import Process
# from multiprocessing import Pipe
#
#
# def f(conn):
# 	conn.send([12, {'name': 'yuan'}, 'hello'])
# 	response = conn.recv()
# 	print('response:', response)  # response: 儿子你好
# 	conn.close()
# 	print('q_ID2:', id(conn))  # q_ID2: 1789790706040
#
#
# if __name__ == '__main__':
# 	parent_conn, child_conn = Pipe()  # 双向管道,既可以收数据,也可以发数据
#
# 	print('q_ID2:', id(parent_conn))  # q_ID2: 1838838772344
# 	print('q_ID1:', id(child_conn))  # q_ID1: 1838838772288
# 	p = Process(target=f, args=(child_conn,))
# 	p.start()
#
# 	print(parent_conn.recv())  # [12, {'name': 'yuan'}, 'hello']
# 	parent_conn.send('儿子你好')
# 	p.join()

"""
pipe和socket模式一样,但是原理不一样

关系:进程之间完成通信,就是把一个数据传给对方,对方也可以把数据传回来.但是没有完成数据共享的功能

manages:完成数据共享

Queue和pipe只是实现了数据交互,并没有实现数据共享,即一个进程去更改另一个进程的数据.


"""
# -------------------方式3:Manager------------------------>
from multiprocessing import Process, Manager


def f(d, l, n):

	d[n] = '1'  # {0:'1'}
	d['2'] = 2  # {1: '1', '2': 2, 3: '1', 6: '1', 0: '1', 4: '1', 5: '1', 7: '1', 2: '1', 9: '1', 8: '1'}

	l.append(n)  # [0, 1, 2, 3, 4, 1, 3, 6, 0, 4, 5, 7, 2, 9, 8]
	print('子进程:', id(d), id(l))


if __name__ == '__main__':
	# 上下文管理器 with
	with Manager() as manager:
		d = manager.dict()  # {}

		l = manager.list(range(5))  # [0,1,2,3,4]

		print('主进程:', id(d), id(l))

		p_list = []

		for i in range(10):
			p = Process(target=f, args=(d, l, i))
			p.start()
			p_list.append(p)

		for res in p_list:
			res.join()

		print(d)
		print(l)

"""
实现的功能:对不同的进程对同一个列表和字典进行操作,实现数据共享的效果.
不是独立的部分,某一个进程操作列表/字典,列表和字典会发生相应的变化,这种变化是累积在所有进程的操作上面的,这样就实现了数据共享功能.

操作一个共同的数据.支持dict/list/变量/lock/信号量对象/互斥锁对象/namespace/函数等等
"""