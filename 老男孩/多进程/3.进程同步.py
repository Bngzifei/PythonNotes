# coding:utf8
"""
同步:处于阻塞等待的状态.

线程是因为共用了数据,为了避免竞争,所以使用锁,所以产生同步<阻塞等待>

但是多个进程也会面临一个共用资源的问题,比如屏幕显示的问题
"""
from multiprocessing import Process, Lock
import time

def f(l, i):
	# with l.acquire():  --> 这样写是不对的,自动会调用acquire()方法
	# with l:  # 使用with之后就不用再去写l.release()方法了
	# 	print('hello world %s' % i)
	l.acquire()
	time.sleep(1)
	print('hello world %s'%i)
	l.release()


if __name__ == '__main__':
	lock = Lock()

	for num in range(10):
		Process(target=f, args=(lock, num)).start()

"""
虽然进程与进程之间是数据独立,内存地址独立的,但是并不意味着所有的资源都独立.有一些资源还是共用的.

输出:
F:\黑马Python20期就业班\oldboy\多进程>python2 3.进程同步.py
hhello world 6
hhello world 5
hello world 0
ello world 2ello world 1
hello world 7
h
ello world 3
hello world 8
hello world 4
hello world 9


可以看到输出乱行了,原因是多个进程在同一个时刻都要在屏幕上面显示输出,谁也不会让谁,就产生了输出在同一行的效果.这样就说明了显示屏幕对于进程之间而言是一个公共的资源.所以在使用的时候会产生资源竞争的问题,所以也就产生了进程同步.
所以想正常输出显示,加锁,按次序来


加锁之后就显示正常了:加锁之后就把屏幕控制了,自己用完之后才会释放
这样加锁之后就是串行的方式了,意思就是一次只能有一个使用,一个一个来使用.
之前没加锁的情况下是并行的,意思就是在同一时刻,大家一起使用这个资源,谁抢到了谁使用,谁也不让谁.

hello world 4
hello world 1
hello world 2
hello world 5
hello world 0
hello world 6
hello world 8
hello world 7
hello world 3
hello world 9

"""
"""
进程池

"""
