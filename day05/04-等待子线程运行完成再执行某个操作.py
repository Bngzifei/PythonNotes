import time
import threading  # 导入线程模块


def sing():
	for i in range(3):
		print('正在唱歌...%d' % i)
		time.sleep(1)
	print(threading.current_thread())


def dance():
	for i in range(3):
		print('正在跳舞...,年龄%d')
		time.sleep(1)
	print(threading.current_thread())


# 主线程执行顺序默认往下,线程执行的时候相互之间不会受影响
if __name__ == '__main__':
	dance_thd = threading.Thread(target=dance,name=dance)
	dance_thd.start()

	sing_thd = threading.Thread(target=sing,name=sing)
	sing_thd.start()

	# 需求:在子线程退出后再执行一步操作.(就是表演结束后欢呼...)
	# 查看当前程序中存活的线程列表
	# print(threading.enumerate())  # 3个
	# while True:
	# 	if len(threading.enumerate()) == 1:
	# 		print('所有子线程已退出,只剩主线程')
	# 		break
	# 	else:
	# 		time.sleep(1)

	print(sing_thd.is_alive())  # True,未结束<查看线程是否结束>
	print(dance_thd.is_alive())  # True
	# 阻塞等待唱歌子线程运行完成,才会继续往下完成.及时的执行
	sing_thd.join()  # Wait until the thread terminates 等待子线程结束
	dance_thd.join()

	print(sing_thd.is_alive())  # False,已结束
	print(dance_thd.is_alive())  # False
	print(threading.current_thread())
	print('太棒啦')




