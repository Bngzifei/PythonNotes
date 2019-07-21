"""
广播:一对多
"""
import socket
while True:

	# 创建socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 设置socket选项      选项是socket层面          广播选项       1:设置,0:取消设置
	udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	udp_socket.sendto('你大爷'.encode(), ('255.255.255.255', 8080))

	udp_socket.close()
