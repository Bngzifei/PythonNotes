print('-------------------')
"""
生产者消费者模型:
1.>为什么要使用生产者和消费者模式:
	在线程世界里,生产者就是生成数据的线程,消费者就是消费数据的线程.在多线程开发当中,如果生产者处理速度很快,而消费者处理速度很慢,那么生产者就必须等待消费者处理完,才能继续生产数据.同样的道理,如果消费者的处理能力大于生产者,那么消费者就必须等待生产者.为了解决这个问题于是引入了生产者和消费者模式.

2.>什么是生产者消费者模式:
	生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题.生产者和消费者之间不直接通信,而通过阻塞队列来进行通信,所以生产者生产完数据之后不用等待消费者处理,直接扔给阻塞队列.消费者不找生产者要数据,而是直接从阻塞队列里面取,阻塞队列就相当于一个缓冲区,平衡了生产者和消费者的处理能力.
	
理解:这就像,在餐厅,厨师做好菜,不需要直接和客户交流,而是交给前台,而客户取饭菜也不需要找厨师,直接去前台领取即可.这也是解耦合的过程.
"""
"""
队列就是那个中介,实现解耦合的作用

阻塞队列:就是起到一个缓冲的作用.

过程应该是:包子一边做一边吃.

task_done 和join就是一个通讯的作用,task_done是任务做完之后发一个信号给队列进行通知,join在没有接受到task_done的信号之前,会一直进行等待操作,直到接收到task_done的信号.




"""
import time, random
import queue, threading

q = queue.Queue()


def producer(name):
	count = 0
	while count < 10:
		print('making......')
		time.sleep(5)
		# time.sleep(random.randrange(3))  # 产生1,2两个随机数,不会产生3.表示sleep 1秒或者2秒
		q.put(count)
		print('Producer %s has produced %s 包子...' % (name, count))
		count += 1
		# q.task_done()  # 厨师做完之后通知队列,包子已经放进去了
		q.join()

		print('ok......')


def consumer(name):
	count = 0
	while count < 10:
			time.sleep(random.randrange(4))

		# if not q.empty():
		# 	print('waiting......')
			# q.join()
			data = q.get()
			print('eating........')
			time.sleep(4)
			q.task_done()
			# print(data)
			# q.join()  # 客人一直在等待包子

			print('\033[32;1mConsumer %s has eat %s 包子...\033[0m' % (name, data))
		# else:
		# 	print('-------no 包子 anymore-------')

			count += 1


p1 = threading.Thread(target=producer, args=('A 君',))
p2 = threading.Thread(target=consumer, args=('B 君',))
p3 = threading.Thread(target=consumer, args=('C 君',))
p4 = threading.Thread(target=consumer, args=('D 君',))
p1.start()
p2.start()
p3.start()
p4.start()

# print(random.randrange(3))  就是输出随机的0,1,2三个数字,不可能取到3
