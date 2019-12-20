print('*'*30)
"""

注意事项:线程执行顺序是无序的

多线程执行的顺序是无序的.


	# 结论:1.>多线程的执行顺序是无序的
	# 结论:2.>主线程会等待子线程退出后再退出
	
	
"""
import threading
import time


def func():
	for i in range(10):
		print('%s' % threading.current_thread().name)
		time.sleep(1)
		print(threading.enumerate())


# 主线程只负责创建启动子线程,子线程才是去执行func()指定的功能.
if __name__ == '__main__':
	for i in range(5):  # 创建并开启5个线程,主线程只会执行这个for(5),不会去走func(),子线程才会去执行func()
		thd = threading.Thread(target=func).start()
		print('-' * 30)

	# 结论:1.>多线程的执行顺序是无序的
	# 结论:2.>主线程会等待子线程退出后再退出
