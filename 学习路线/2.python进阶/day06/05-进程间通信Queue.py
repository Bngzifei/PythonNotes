"""
因为独立空间,不共享数据
所以要进程之间通信,使用双方都要使用的资源


queue:队列,先到先得,先进先出.能够满足先进先出的数据结构就是队列  FIFO --> first in first out

queue:采用多任务操作,put之后的有可能有时间延迟,某些操作可能会因此出错

如果队列中没有东西了,会进入阻塞等待状态

如果满了还往里面继续放,会出现卡,就是阻塞等待状态

如果为空,阻塞等待取数据
如果为满,阻塞等待队列有空位置

参数:block,默认为True,表示是否为阻塞等待,tineout表示阻塞等待的时间
.get(block=True,timeout=None)
.get(block=True,timeout=1)   阻塞等待 1秒
.get(False)  == .get_nowait()  不能取值就直接结束

.put(data,block=True,timeout=None) None表示一直等下去,永久
.put(4,False,3):3秒之内4放不进去就结束

"""

import multiprocessing
import time

# 创建一个队列,10代表队列的长度,里面可以存10条信息
q = multiprocessing.Queue(3)  # 如果Queue()的参数为空,就是无限长度,直到挤爆内存
print('当前队列是否为空', q.empty())
# 向队列里面放数据
q.put(1)
q.put(2)
q.put(3)
time.sleep(0.1)
# 当前队列里面的数据长度 ,这个方法有问题,mac系统下会出错,linux没问题.一般不建议使用(nowait也会有bug)
print('当前队列的长度:', q.qsize())
# 查看队列是否已经满了
print('当前队列满了吗?', q.full())

# 从队列取数据
print('取出的数据是:', q.get())
print('当前队列的长度:', q.qsize())
print('取出的数据是:', q.get())
print('当前队列的长度:', q.qsize())
print('当前队列空了吗?', q.empty())
print('取出的数据是:', q.get())
print('当前队列空了吗?', q.empty())

# 查看队列是否为空
# print(q.empty())
