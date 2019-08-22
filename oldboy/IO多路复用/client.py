# ----------------------IO多路复用 client端:------------->
# import socket
#
# sk = socket.socket()
#
# sk.connect(('127.0.0.1', 8080))
#
# while True:
# 	inp = input(">>>").strip()
# 	sk.send(inp.encode('utf8'))
# 	data = sk.recv(1024).decode('utf8')
# 	print(data)
"""
IO多路:
1.>select 效率最低
2.>poll
3.>epoll 最好的

ngix就是使用了epoll实现多连接

利用的是IO空闲的时间

epoll不是异步的没什么意思.
异步:没有任何阻塞

异步:全程无阻塞

只要有一丁点阻塞,那么它就是同步IO.就是需要一直等,直到IO操作结束

异步是一点阻塞都不会有才叫异步

非阻塞IO:也是同步

epoll 实际上也是同步的.


"""
# ------------------------并发实现client 没有使用多线程---------------->
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
	inp = input('>>>')
	sk.sendall(bytes(inp, 'utf8'))
	data = sk.recv(1024)
	print(str(data, 'utf8'))
