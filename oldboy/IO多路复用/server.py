import socket
import select
"""
触发方式:

1.>水平触发:也就是只有高电平1或则低电平0时候才触发通知.只要在这两种状态就能得到通知.
上面提到的只要有数据可读,那么水平触发的epoll就立即返回


2.>边缘触发:只有电平发生变化<从高电平到低电平,或者低电平到高电平>的时候才触发通知,上面提到的即使有数据可读,
但是没有新的IO活动到来,epoll也不会立即返回.

理解:
水平触发就是在一段时间内一直触发,一直执行
边缘是在状态发生变化的时候才会触发

IO多路复用优势:同时可以监听多个连接.

select 在三大平台上面都支持
select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制<即最大只能同时监听1024个连接>,在linux上一般为1024,
不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制,另外,select()所维护的存储大量文件描述符的数据结构.随着文件描
述符数量的增大,其复制的开销也线性增长.同时,由于网络响应时间的延迟使得大量tcp连接处于非活跃状态.但调用select()会对所有
socket进行一次线性扫描<即遍历>,所以这也浪费了一定的开销

poll:它和select在本质上没有多大差别,但是poll没有最大文件描述符数量的限制.

epoll:直到linux2.6才出现了由内核直接连接支持的实现方法.那就是epoll.被公认为Linux2.6下性能最好的多路IO就绪通知方法.Windows不支持

没有最大文件描述符数量限制.
比如100个连接,有两个活跃了<就是有两个客户端请求链接了>,
epoll会告诉用户这两个活跃了,直接去取就好了<实际上就是这两个活跃的会自己报上自己的姓名,说自己请求连接了>,
而select是轮询一遍,因为就绪活跃的不会自己自报家门.

epoll可以同时支持水平触发和边缘触发.只告诉进程哪些文件描述符刚刚变为就绪状态.它只说一遍,如果我们没有采取行动,
那么它将不会再次告诉,这种方式称为边缘触发.理论上边缘触发的性能要更高一些.但是,代码实现相当复杂.
另一个本质的改进在于epoll采用基于事件的就绪通知方式.在select/poll中,进程只有在调用一定的方法后,内核才对所有监视的文件
描述符进行扫描,而epoll事先通过epoll_ctl()来注册一个文件描述符,一旦基于某个文件描述符就绪时,内核会采用类似callback的回调
机制,迅速激活这个文件描述符,当进程调用epoll_wait()时便得到通知.

所以市面上见到的异步IO,比如Nginx,tornado等,我们叫它异步IO,实际上是IO多路复用
"""

# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen(5)
# inp = [sk, ]
#
# while True:
# 	# 监听select,5表示隔5秒监听 每隔5秒打印一次,等待client连接
# 	r, w, e = select.select(inp, [], [], 5)
#
# 	# 连接过来之后
# 	for i in r:  # [sk,conn]
# 		conn, addr = i.accept()
# 		print(conn)
# 		print('hello')
# 		inp.append(conn)
# 	conn.recv(1024)
# 	print('>>>>')

# ---------------------并发实现 server----------------->

import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
inputs = [sk, ]

while True:
	r, w, e = select.select(inputs, [], [], 5)

	for obj in r:  # [sk,]
		"""判断是sk还是conn"""
		if obj == sk:
			conn, add = obj.accept()
			print(conn)
			inputs.append(conn)
		else:
			data_byte = obj.recv(1024)
			print(str(data_byte, 'utf8'))
			inp = input('回答%s号客户>>>' % inputs.index(obj))
			obj.sendall(bytes(inp, 'utf8'))
	print('>>', r)
