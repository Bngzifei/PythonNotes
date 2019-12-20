"""
socket就是一个手机,这么理解即可

1.创建socket(买个手机)
2.建立连接(拨号)
3.发送数据(通话)
4.关闭socket(挂掉)

"""

import socket

# 创建
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接
tcp_client_socket.connect(('192.168.14.26', 8089))

while True:

	# 发送数据
	send_data = input('输入发送给服务器的数据:')
	tcp_client_socket.send(send_data.encode())  # 参数是一个字节流bytes类型的数据

	# 接收返回 ,面向连接的(地址肯定是连接的对方的地址)不再需要对方的地址,只需要对方发送的数据
	# 阻塞等待的接收返回
	# recv()返回值的含义:
	# recv()正常情况下是接收到的数据<bytes类型>
	# 如果对方断开连接,返回值就是b''<空字节>,不是对方发送的数据,是系统提示对方断开的标志
	recv_data = tcp_client_socket.recv(1024)  # recv()返回一个数据(bytes类型)即可,没有地址信息
	# print(recv_data.decode('gbk'))  # 解码解得是调试助手发来的数据,而调试助手发送的时候是gbk的编码格式
	# 断开连接输出:b''  <空字节>
	# print(recv_data)  # 解码解得是调试助手发来的数据,而调试助手发送的时候是gbk的编码格式
	# recv_data != None and recv_data !=''
	if recv_data:  # 如果recv_data不为空,为真
		print(recv_data.decode('gbk'))
	else:  # 为空,终止
		print('服务器断开连接')
		break
# 关闭
tcp_client_socket.close()

