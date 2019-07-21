"""
注意:udp/tcp的服务器都需要进行绑定端口,这样才能让客户端找到是哪个程序在进行通信
创建socket
绑定端口
发送数据
关闭socket
"""
import socket

while True:
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 使用固定端口,bind()绑定端口,ip为空代表本机的任意ip
	#  绑定 - > 使用固定端口  需要被其他人使用的时候就要绑定
	udp_socket.bind(('', 8888))  # 反正我绑定本机上面的8888端口了,所以本机上面的其他程序不能用8888口
	# 注意:必须要先绑定端口,然后才能进行收发数据的操作

	# 进行收数据  将收到的数据返回去 ---> 这样模式的服务器称之为 echo 服务器(echo:反射,回复)
	recv_data, address = udp_socket.recvfrom(1024)  # 阻塞等待recvfrom,一直会等待接收数据,一旦数据到达才会继续往下执行.
	# window -> Pycharm:gbk/gb2312   Pychram -> window : utf-8
	print('接收到来自%s的消息:%s' % (address, recv_data.decode('gbk')))
	recv_data = recv_data.decode('gbk').encode()  # 将gbk编码对应的str进行utf-8格式编码,再发过去给window
	# 回复数据  这里的编码问题,注意下
	udp_socket.sendto(recv_data, address)  # 注意:这里的recv_data是bytes类型,只能解码decode(),没有encode()的属性,
# window下面的调试助手显示乱码的原因是需要那边显示的部分进行解码

# 关闭  死循环,程序执行不到这里
udp_socket.close()
