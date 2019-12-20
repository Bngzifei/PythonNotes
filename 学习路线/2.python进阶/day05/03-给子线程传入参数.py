import time
import threading  # 导入线程模块


def sing():
	for i in range(3):
		print('正在唱歌...%d' % i)
		time.sleep(1)


def dance(age, name, height):
	for i in range(3):
		print('我的海拔是%d' % height)
		print('%s在跳舞...,年龄%d' % (name, age))
		time.sleep(1)
	# 查看当前线程的标识  <Thread(Thread-1, started 1744)>
	print(threading.current_thread())


# 主线程执行顺序默认往下,线程执行的时候相互之间不会受影响
if __name__ == '__main__':
	# args 元组<位置参数>
	# kwargs 字典<关键字参数>
	dance_thd = threading.Thread(target=dance, args=(100, 'Jerry'), kwargs={'height': 178})
	dance_thd.start()
	sing()
	print(threading.current_thread())  # <_MainThread(MainThread, started 2696)>

"""
group:线程组,python官方目前还未实现该模块
args: 元组形式的传参数,位置参数,
kwargs:字典形式的传参数,关键字参数,就是指定某一项值为多少,例如,指定 身高=185

"""
