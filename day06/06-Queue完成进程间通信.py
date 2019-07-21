import multiprocessing
import time


def func(queue):
	"""取数据"""
	while True:
		print(queue.get())
		time.sleep(1)


def main():
	"""放数据,一个放,一个取,说明通信的问题"""
	# 创建队列
	q = multiprocessing.Queue(5)  # 5条数据的长度,表示队列的长度为5
	# 创建一个子进程,获取队列的数据,并打印
	p = multiprocessing.Process(target=func, args=(q,))
	p.start()

	# 主进程-->放数据   子进程里面不要输入数据
	while True:
		data = input('>>>')
		if q.full():
			print('满了')
		else:
			q.put(data)


if __name__ == '__main__':
	main()
