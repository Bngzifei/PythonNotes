import socket
import threading


# 主线程 ---> 负责接受客户端连接
# 子线程 ---> 负责接收数据
def client_services(tcp_client_socket):
	"""为客户端服务"""
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


def main():
	# 创建服务器socket
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 地址重用     意思就是在socket选项中设置socket的地址可以重用  处理 address is already in used这个问题,用完地址就释放,地址重用
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
		# 启动线程为客户端服务
		thd = threading.Thread(target=client_services, args=(tcp_client_socket,))
		thd.start()

	# 总机关闭
	tcp_server_socket.close()


if __name__ == '__main__':
	main()
