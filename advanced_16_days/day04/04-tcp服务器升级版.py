"""
tcp服务器:
1.>socket()买个手机

2.>bind()绑定10086

3.>listen()安装客户服务系统,设定等待服务区的大小,从等待区域中取出一个客户(和客户建立连接)

4.>accept()并转接到分机,具体的同事使用分机和客户交流

5.>close()分机挂机

总计挂机

总机不会挂机
分机会挂机
实际在交流信息的时候是和分机交流
总机只是和客户建立连接,分到等待区

服务器分为两种socket,一种专门来接受客户的连接请求,一种才是和客户进行数据交流

服务器是被动的
"""
import socket

# 创建服务器socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定,如果不绑定,别人就找不到这个地址了
tcp_server_socket.bind(('', 9999))  # ip为空,意味着绑定了这台主机上面的所有网卡,一台机子上面不是只有一个网卡,至少是2个网卡

# 监听等待  安装客户服务系统 --->1.将socket设置为被动socket<被动接受连接  默认是主动连接>  2.设置等待服务区的大小为128
tcp_server_socket.listen(128)
print('服务器已建立连接')

# 就是领导接活,下面的小弟只管干活
while True:
	# 转到分机接收     从等待服务区取出一个客户端来服务
	# 返回值是一个元组,两个元素,第一个元素是客户端socket<分机>,第二个是客户端的(ip,port)<地址>
	tcp_client_socket, client_info = tcp_server_socket.accept()  # 无参数,只有返回值,返回值是socket和 address_info
	print('接受到客户%s的连接请求' % str(client_info))

	while True:
		# 使用分机和客户端进行交流    ----> 数据收发
		recv_data = tcp_client_socket.recv(1024)

		# 服务器返回给客户信息,  接收到的是gbk的编码数据流,需要解码后再次编码为utf-8
		tcp_client_socket.send(recv_data.decode('gbk').encode())
		if recv_data:
			print('接收到的客户数据:', recv_data.decode('gbk'))
		else:  # b''
			print('客户端下线了')
			break

	# 分机关闭
	tcp_client_socket.close()
	# # 总机关闭
	# tcp_server_socket.close()

	# 我需要被别人找到,就要使用bind()

	# 想要接受连接,必须先listen()
	# 收发数据都是client_socket
	# accept() 接受:被动的
	# close() 断开连接请求
	# 0字节长度 ---> 对方断开连接了
	# 解阻塞:由卡死到不卡的状态变化.
