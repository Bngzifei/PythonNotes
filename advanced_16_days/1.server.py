"""
创建socket
绑定端口
发送数据
关闭socket
"""
import socket, time


def main():
	while True:
		# 创建socket
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		# 绑定端口
		udp_socket.bind(('', 8080))
		# 接收广播消息
		recv_data, address = udp_socket.recvfrom(1024)
		print('接收到来自%s的消息:%s' % (address, recv_data.decode()))
		time.sleep(1)

		cmd = input('继续接收请按c>>>,退出接收请按q>>>')
		if cmd == 'c':
			continue
		if cmd == 'q':
			break


	# 关闭 socket
	udp_socket.close()


if __name__ == '__main__':
	main()


