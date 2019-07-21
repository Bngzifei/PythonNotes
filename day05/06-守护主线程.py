"""
守护线程:设置所有的子线程为守护线程,当主线程退出的时候子线程也随之退出.避免了孤儿线程的问题
"""

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
	dance_thd = threading.Thread(target=dance, name=dance)
	# 将子线程设置为守护线程
	dance_thd.setDaemon(True)
	dance_thd.start()
	sing_thd = threading.Thread(target=sing, name=sing)
	# 将子线程设置为守护线程
	sing_thd.setDaemon(True)
	sing_thd.start()
	time.sleep(3)  # 让主线程休眠9秒,不是死了,是睡着了的意思.说明主线程还活着,子线程还会执行
	print('主线程挂了')

	# 一般讲所有的子线程设置为守护线程,跟随主线程一起退出

	# 守护意义:当前程序中所有的守护线程会随着最后一个非守护线程的退出而退出
