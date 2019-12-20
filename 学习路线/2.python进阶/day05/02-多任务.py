import time
import threading  # 导入线程模块


def sing():
	for i in range(3):
		print('正在唱歌...%d' % i)
		time.sleep(1)


def dance():
	for i in range(3):
		print('正在跳舞...%d' % i)
		time.sleep(1)


# 主线程执行顺序默认从上往下,线程执行的时候相互之间不会受影响
if __name__ == '__main__':
	# sing()  # 这样就没有多任务了
	# 主线程代码
	# 1.创建一个新的线程  创建了一个计划.  target = dance不能加(),否则就是在主线程里面执行了,这样就逻辑错误了
	dance_thd = threading.Thread(target=dance)  # target:指定新(子)线程执行的函数名,因为dance不是我们自己调用的,是这个线程去调用执行,所以不要加().
	# 2.启动子线程的创建和执行
	dance_thd.start()  # 给主线程开个分支
	# 一个程序肯定是一个线程,默认的线程是sing(),称之为主线程,其余的称之为子线程
	sing()  # 主线程一定要在子线程执行的后面,否则就不是多任务了.
# 一旦创建子线程,不会出现主线程执行完成才会执行子线程的情况,因为这个时候子线程和主线程是同一起跑线,一起执行.子线程依赖于主线程,主的结束了,子的就不会再继续执行了.
# dance()


"""
group:线程组,Python官方目前还未实现该模块


"""
