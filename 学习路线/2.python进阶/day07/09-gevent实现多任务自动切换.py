from gevent import monkey  # gevent文档规定了这两行放到源代码的开始
monkey.patch_all()  # 打补丁
"""
# 将原来的阻塞打了补丁,去除了这个阻塞的问题,
# 默认会把阻塞的函数recv,accept,time.sleep变成非阻塞的,input(),raw_input()函数都不可以
# gevent官方要求: monkey.patch_all() 放在开头,和PEP8要求冲突.

"""
import gevent
import time

def worker1(n1, n2, **kwargs):
	"""协程函数"""
	print(n1, n2, kwargs)
	while True:
		print('in worker1')
		# gevent.sleep()  # 这么写 在没有猴子补丁(monkey.patch)的情况下,可以自动切换,但是不通用,所以使用猴子补丁
		time.sleep(0.5)  # 没有猴子补丁的情况下,程序会自动阻塞,不能自动切换

def worker2():
	while True:
		print('in worker2')
		# gevent.sleep(0.5)
		time.sleep(0.5)

def main():
	# 创建并且 启动 协程
	g1 = gevent.spawn(worker1, 1, 2, b=5)
	g2 = gevent.spawn(worker2)
	# 等待协程执行完成,因为协程依赖于主进程<主进程退出后协程也跟着退出了>
	# g1.join()
	# g2.join()
	# 如果没有join(),就不会执行协程
	# gevent.joinall([g1,g2])
	# 在所有协程执行完成之前,保持主进程的存活
	# 说明了join()和time.sleep(100)的作用一致
	time.sleep(100)
	# gevent.sleep(100)


if __name__ == '__main__':
	main()
