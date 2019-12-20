import socket


def menu():
	print('-' * 30)
	print('1-->发送,2-->接收,3-->退出')
	print('-' * 30)


def send_msg(udp_socket):
	"""发送"""
	data = input('数据:')
	ip = input('ip:')
	port = int(input('port:'))
	udp_socket.sendto(data.encode(), (ip, port))


def recv_msg(udp_socket):
	"""接收"""
	udp_socket.bind(('', 8888))
	data, address = udp_socket.recvfrom(1024)
	print('来自%s的消息:%s' % (str(address), data.decode() ) )


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		menu()

		op = int(input('选择操作>>>'))

		if op == 1:
			send_msg(udp_socket)
		elif op == 2:
			recv_msg(udp_socket)
		elif op == 3:
			print('bye')
			break
		else:
			print('输入错误,重来')
	# 关闭
	udp_socket.close()


if __name__ == '__main__':
	main()
