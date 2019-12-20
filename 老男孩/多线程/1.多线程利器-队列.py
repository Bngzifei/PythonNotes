print('多线程队列')
"""
1.>在多线程中,列表是不安全的数据结构


"""
# import threading
# import time
#
# li = [1, 2, 3, 4, 5]  # 本身就是线程不安全的,多线程不可以选择这种<只有加锁处理>
#
#
# def pri():
# 	while li:
# 		a = li[-1]
# 		print(a)
# 		time.sleep(1)
# 		try:
# 			li.remove(a)
# 		except Exception as e:
# 			print('--->', a, e)
#
#
# t1 = threading.Thread(target=pri, args=())
# t1.start()
# t2 = threading.Thread(target=pri, args=())
# t2.start()

# ----------------------------FIFO模式--------------------->
# import queue  # 线程队列
#
# # 创建一个queue对象  3表示最大可以放入3个数据
# q = queue.Queue(3)  # 三种模式:FIFO先进先出/先进后出/优先级顺序,默认是先进先出
#
# # 放入数据
# q.put(12)
# q.put('hello')
# q.put({'name': 'yuan'})
# # q.put({'name': 'yuan'},False)  # queue.Full True表示无提示
#
#
# # 取值
# while True:
# 	data = q.get(False)  # 参数是 False 的时候queue.Empty  取完了会报错
# 	print(data)
# 	print('--- --- ---')

# ------------------------先进后出<就是后进先出>--------------------->
# import queue
#
# q = queue.LifoQueue()  # 后进先出  later in first out
#
# # 放入数据
# q.put(12)
# q.put('hello')
# q.put({'name': 'yuan'})
# # q.put({'name': 'yuan'},False)  # queue.Full True表示无提示
#
#
# # 取值
# while True:
# 	data = q.get()  # 默认参数是True,不报错. 参数是 False 的时候queue.Empty  取完了会报错
# 	print(data)
# 	print('--- --- ---')

# ------------------------优先级顺序  数字越低,级别越高----------------------->
"""
q.task_done() 在完成一项工作之后,q.task_done()函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空,再执行别的操作.

"""
import queue

q = queue.PriorityQueue(3)
# 放入数据
q.put([3, 12])
q.put([2, 'hello'])
q.put([4, {'name': 'yuan'}])
# q.put({'name': 'yuan'},False)  # queue.Full True表示无提示
q.put_nowait([9,112])  # queue.Full 相当于q.put(block=False)
print(q.qsize())
print(q.empty())
print(q.full())

# 取值
while True:
	data = q.get()  # 默认参数是True,不报错. 参数是 False 的时候queue.Empty  取完了会报错
	# data=q.get_nowait()  相当于 q.get(block=False)
	print(data[0])  # 优先级编号
	print(data[1])  # 对应的数据
	print(data)  # 优先级和数据
	print('--- --- ---')

