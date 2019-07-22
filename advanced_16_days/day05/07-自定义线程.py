print('-' * 30)
"""
第二种创建线程的方式,继承threading.Thread()类,然后重写父类方法,实现自己需要的功能.

"""
import threading
import time


# threading模块里面的Thread类
class MyThread(threading.Thread):  # 继承自threading模块里面的Thread类
	def __init__(self, age, height):
		# 重写父类的init()方法 将接收的参数保存为属性  ,这样run方法才可以直接使用
		super().__init__()  # 记得调用父类的init()
		self.age = age  # 重写
		self.height = height  # 重写

	def run(self):  # 官方规定是run,写成其他不会被执行,无效
		"""run()方法是子线程运行的方法,子线程会从run开始运行"""

		print(self.age, self.height)
		for i in range(10):
			print('%s子线程正在运行' % threading.current_thread().name)
			time.sleep(1)


if __name__ == '__main__':
	# 创建出Thread对象
	mt = MyThread(98, 180)
	# start()先是创建子线程;然后运行子线程,并且会回去调用子线程的run()方法
	mt.start()  # 这里会自动去调用run()子线程运行的方法,但是记住这里不能直接换成run()
	print('%s主线程正在运行' % threading.current_thread().name)


"""
1.继承自thread.Thread()类及其子类
2.重写其中的run()方法,run存放的是子线程运行的代码
3.创建子线程  创建类的对象   对象.start()
4.如果子线程需要更多的参数,需要重写init()方法,在其中还要调用super()
ps:就是这里调用了父类被重写过的方法,所以需要使用super()
"""
