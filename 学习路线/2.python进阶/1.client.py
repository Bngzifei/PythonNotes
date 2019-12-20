"""
广播:一对多
先发送,后接收
"""
import socket, time


def main():
	msg = input('输入想要发送的消息:').strip().encode()
	while True:
		# 创建socket
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# 设置socket选项      选项是socket层面          广播选项      1:设置,0:取消设置
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		udp_socket.sendto(msg, ('255.255.255.255', 8080))
		time.sleep(1)
		# data, addr = udp_socket.recvfrom(1024)
		# print(data)
		# print(addr)

		udp_socket.close()


if __name__ == '__main__':
	main()
