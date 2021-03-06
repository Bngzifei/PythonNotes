print('多任务...')

"""
多任务:同时执行多个任务

并发:同一时间段<并不是同一时刻,是一段时间,有范围的>(一个cpu)内,多个程序轮流地执行,交替执行.这是多任务的一种方式.
<理解:就是一会儿做这个,一会儿做那个,轮着做>
并行:同一时刻同时在执行.(多个cpu)多个任务在不同cpu上同时执行.这也是多任务的一种方式

线程:多任务实现方式1:

自上而下:一个分支,所以都是单任务,单线程.

分个叉继续执行 ---> 就是多线程了

增加一个分支,执行一个任务的同时又去执行另外一个任务,就是多线程.

time.sleep():sleep()可以让当前程序休眠,相当于暂停一会儿,并不是死掉

https://www.cnblogs.com/hongfei/p/3862620.html

"""

import time


def sing():
	for i in range(3):
		print('正在唱歌...%d' % i)
		time.sleep(1)


def dance():
	for i in range(3):
		print('正在跳舞...%d' % i)
		time.sleep(1)


if __name__ == '__main__':
	sing()
	dance()
