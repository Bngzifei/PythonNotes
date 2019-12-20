import greenlet
import time


def worker1():
	"""生成器函数"""
	while True:
		print('in worker1')
		g2.switch()
		time.sleep(0.5)


def worker2():
	while True:
		print('in worker2')
		g1.switch()
		time.sleep(0.5)


# 如果是这样g1,g2就是局部变量,work1和work2函数就识别不出来了,程序就无法执行了
# def main():
# 	g1 = greenlet.greenlet(run=worker1)
# 	g2 = greenlet.greenlet(run=worker2)


if __name__ == '__main__':
	# 这样写是g1,g2是全局变量
	g1 = greenlet.greenlet(run=worker1)
	g2 = greenlet.greenlet(run=worker2)
	# 切换到指定任务执行
	g1.switch()
