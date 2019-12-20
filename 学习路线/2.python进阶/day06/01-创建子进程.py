"""
进程:程序一旦运行,就有进程<主进程>默认存在的进程叫主进程.
线程是进程的一部分.

调度:是否可以给一个cpu执行
线程是os进行资源调度的基本单位.  ---> 使用资源  个体,执行实体
进程是os进程资源分配的基本单位.  ---> 分配资源  分配不等于使用  统筹规划,只管安排分配

线程是轻量级的进程.
实际开发过程中线程使用多于进程.

进程使用的时候资源开销大.
线程开销稍微的小一些.

进程:通俗的理解:就是一个运行的程序或者软件.

新建  (启动) --> 就绪(只等cpu) <--> 运行 --> 死亡
ready:  分配时间片  到运行状态
running: 时间片用完 到ready就绪状态
时间片:cpu给每个进程分配的执行时间
等待(阻塞):等待条件<recv(),time.sleep(),input() 阻塞了时间片就会让出去给其他任务>  --> blocked 阻塞状态就是等待状态,等条件,等数据.
运行 --> 等待,就没有时间片了

就绪态:等cpu分配时间片
等待态:等数据,条件
运行态:执行

线程是依附于进程里面的,没有进程就没有线程.
进程是os资源分配的基本单位
线程是os资源执行的基本单位

ps -aux | grep python3: 查看python3的相关进程
ps -aux: process statue 进程状态 ,查看当前系统的进程
kill -9 67960:发信号 立刻退出  让67960进程立刻退出  9号信号:绝对终止

"""
import multiprocessing
import time
import os


def func(age, height, love):
	"""子进程会执行 的函数"""

	for i in range(10):
		# os.getpid() 获取当前进程的PID
		# os.getppid() 获取当前进程的父进程的PID  parent process id
		print('子进程的PID:%s,父进程的PID:%s' % (os.getpid(), os.getppid()))
		print('身高:%d,年龄:%d,爱好是:%s' % (height, age, love))
		time.sleep(1)


# 默认的就是主进程
def main():
	# 这是主进程运行的范围
	# 创建一个子进程  1.创建实例对象 2.启动 start()
	# 进程编号: pid
	# os.getppid():当前进程的父进程PID

	# target里面的就是子进程运行的,kwargs是指定某个具体的项的值是多少,才使用
	pro = multiprocessing.Process(target=func, args=(18, 175), kwargs={'love': '抽烟喝酒'})

	# 主进程创建之后不会返回去执行,会直接自己继续往下走,子进程会自己去调用自己的func函数,二者独立执行,相互不影响.
	pro.start()

	for i in range(10):
		print('这是主进程的PID:', os.getpid())
		time.sleep(1)


if __name__ == '__main__':
	main()
"""
主进程负责监护子进程,回收分给子进程的各种资源.但是主进程和子进程之间不存在关联,杀死主进程后子进程依然正常运行.

实际上在上面的程序运行过程中可以看到,当主进程运行至timesleep(1)的时候,子进程并没有停下休眠,而是继续运行,所以我们
才会看到主进程和子进程是一起出现在终端,,看起来就是并行的现象.这其实就是利用主进程休眠的空余时间来执行子进程,这样
避免了cpu资源的时间浪费.尽可能多的利用cpu.不闲置,不空置.


"""
