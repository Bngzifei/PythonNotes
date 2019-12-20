"""
UDP:User Datagram Protocol 简称用户数据报协议,无连接,不可靠

特点: 1.无连接 2.资源开销小3.传输速度快 4.每个数据包最大是64K

优点:传输速度快,不需要连接,资源开销小
缺点:传输数据不可靠,容易丢包
	没有流量控制,当对方没有及时接收数据,发送方一直发送数据会导致缓冲区数据占满了
	电脑出现卡死的情况,所有接收方需要及时接收数据.

使用场景:1.对网络通讯质量要求不高 2.要求通讯速度尽可能的快.
例如: qq视频,共屏软件,发送广播消息.


意思就是无需确认对方是否存在,发送端只管发送就行.


"""
"""
socket:数据传输就需要使用socket,也就是进程之间通信需要使用socket.

进程:运行的程序或者软件

进程通信:运行的程序之间的数据共享

socket 简称套接字,是进程间通信的一个工具,它能实现把数据从一方传输到另外一方.
完成不同电脑上进程之间的通信.  好比是数据的搬运工


基于UDP的网络程序流程:
1.创建UDP套接字
2.发送/接收数据
3.关闭套接字



import socket  # 先导入socket模块
socket.socket(AddressFamily,Type)  # 使用socket模块下的socket()函数

说明:
函数socket.socket()创建一个socket,该函数带有两个参数
AddressFamily:IP地址类型,就是IPV4和IPv6.这两种区别.

AF_INET:ipv4类型的IP
AF_INET6:ipv6类型的IP

Type:套接字类型

分为SOCK_STREAM(流式套接字,多用于TCP协议)
SOCK_DGRAM(数据报套接字,多用于UDP协议)

"""

# import socket
#
# # 创建udp的套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 接收方的地址
# dest_addr = ('192.168.14.26', 8080)  # 注意:是元祖类型,ip是字符串,端口是数字
#
# # local_addr = ('',7788)  # 本机操作
# # s.bind(dest_addr)  # 绑定本地相关信息
# # 获取数据
# send_data = input('输入发送的数据:')
#
# # 发送到指定电脑 指定的程序
# s.sendto(send_data.encode('utf-8'), dest_addr)
#
# # 不用的时候,关闭套套接字
# s.close()

"""
编码和解码:
str -> bytes:encode 编码
bytes -> str: decode 解码

即字符串通过编码成为字节码,字节码通过解码成为字符串

decode() 和 encode() 方法可以接受参数,格式为:

bytes.decode(encoding='utf-8',errors='strict')
str.encode(encoding='utf-8',errors='strict')


strict:严格按照指定编码方式编码/解码
ignore:忽略编码/解码不成功的字符

"""
# text = '我说'
# print(text)  # 我说
# bytesText = text.encode()  # 编码
# print(bytesText)  # b'\xe6\x88\x91\xe8\xaf\xb4'
#
# print(type(text))  # str 类型
# print(type(bytesText))  # bytes类型
#
# textDecode = bytesText.decode()  # 解码
# print(textDecode)


"""UDP发送广播消息:

广播地址最常用的是255.255.255.255
"""

# import socket
#
# # 创建socket
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 设置socket的选项,允许发送广播消息
# udp_socket.sendto('hello python'.encode('utf-8'), ('255.255.255.255',80))
#
# # 关闭socket
# udp_socket.close()


"""UDP聊天器:"""
import socket

# def send_msg(udp_socket):
# 	"""获取数据,发送给对方"""
# 	msg = input('输入数据:')
#
# 	dest_ip = input('\n对方IP:')
#
# 	dest_port = input('\n对方端口:')
#
# 	udp_socket.sendto(msg.encode(), (dest_ip, int(dest_port)))
#
#
# def recv_msg(udp_socket):
# 	"""接收数据"""
# 	recv_msg = udp_socket.recvfrom(1024)
#
# 	recv_ip = recv_msg[1]
# 	recv_msg = recv_msg[0].decode('utf-8')
#
# 	print('>>>%s:%s' % (str(recv_ip), recv_msg))
#
#
# def main():
# 	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# 	udp_socket.bind(('', 8088))  # bind() 绑定的是一个元组数据类型
# 	while True:
# 		print('-' * 30)
# 		print('1:发送消息')
# 		print('2:接收消息')
# 		print('-' * 30)
# 		option_num = input('输入选择的功能:')
#
# 		if option_num == '1':
# 			send_msg(udp_socket)
# 		elif option_num == '2':
# 			recv_msg(udp_socket)
# 		else:
# 			print('输入有误,请重新输入...')
#
#
# main()
import time

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_addr = ('192.168.14.26', 8081)

# send_data = input('输入数据:')

# udp_socket.sendto(send_data.encode(),send_addr)
while True:
	time.sleep(10)
	recv_data, dest_addr = udp_socket.recvfrom(1024)
	print(recv_data.decode())
