import socket
import threading

"""实现收和发各自独立运行,相互之间互不影响"""


def menu():
	print('-' * 30)
	print('1-->发送,2-->退出')
	print('-' * 30)


def send_msg(udp_socket):
	"""发送"""
	data = input('数据:')
	ip = input('ip:')
	port = int(input('port:'))
	udp_socket.sendto(data.encode(), (ip, port))


def recv_msg(udp_socket):
	"""接收"""
	while True:
		# udp_socket.bind(('', 8888))  放到主线程里面去绑定
		data, address = udp_socket.recvfrom(1024)
		print('来自%s的消息:%s' % (str(address), data.decode('gbk')))


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp_socket.bind(('', 8888))
	# 在主线程中创建一个子线程,专门来接收(recv_msg)数据
	thd = threading.Thread(target=recv_msg, args=(udp_socket,))
	thd.setDaemon(True)  # 子线程会随着主线程的退出而退出
	thd.start()

	while True:
		menu()
		op = int(input('选择操作>>>'))

		if op == 1:
			send_msg(udp_socket)
		# elif op == 2:
		# 	recv_msg(udp_socket)
		elif op == 2:
			print('bye')
			break
		else:
			print('输入错误,重来')
	# 关闭
	udp_socket.close()


if __name__ == '__main__':
	main()
"""

线程是操作系统进行资源调度的基本单位.
可能是并行,也可能是并发.

"""