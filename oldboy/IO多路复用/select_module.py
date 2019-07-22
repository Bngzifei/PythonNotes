import selectors
import socket

# 创建一个对象    day36 selectors模块
sel = selectors.DefaultSelector()

"""
socket就是一个文件描述符

缓存IO又被称作标准库IO,大多数文件系统的默认IO操作都是缓存IO.在Linux的缓存IO中,操作系统会将IO的数据缓存在文件系统的页缓存(page cache)中.也就是说,数据会先被拷贝到操作系统内核的缓存区中,然后才会从操作系统内核的缓冲区拷贝到应用程序的地址空间.用户空间没法直接访问内核空间的,内核态到用户态的数据拷贝

缓存IO的缺点:数据在传输过程中需要程序地址空间和内核进行多次数据拷贝操作,这些数据拷贝所带来的cpu以及内存开销是非常大的.
"""

def accept(sock, mask):
	conn, addr = sock.accept()
	print('accepted', conn, 'from', addr)
	conn.setblocking(False)
	sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
	data = conn.recv(1000)
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)
	else:
		print('closing', conn)
		# 解除连接
		sel.unregister(conn)
		conn.close()


sock = socket.socket()

sock.bind(('localhost', 8090))

sock.listen(100)

# 设置非阻塞
sock.setblocking(False)
# 注册就是一个绑定操作,就是与之关联的意思
sel.register(sock, selectors.EVENT_READ, accept)
print('server....')
while True:

	events = sel.select()
	# print("events",events)

	for key, mask in events:
		# print("key",key)
		# print("mask",mask)
		callback = key.data
		print("callback",callback)
		# key.fileobj 就是一个socket对象
		callback(key.fileobj, mask)
