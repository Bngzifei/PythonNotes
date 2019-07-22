"""
PWS3.0目的:在用户每次访问的时候,会根据用户的请求,返回对应的资源

1.>接收请求报文
2.>解析请求报文-得到用户需求
3.>根据用户的需求找到对应的资源
4.>资源打包到HTTP响应报文

最开始肯定是最简单的,一步一步的加多,慢慢地才会出来
PWS2.0:Python Web Server 2.0

主从
master slave

主:接受用户数据
从:干活

leader:
follower:



"""
import socket
import re


def main():
	# 1. 创建tcp服务器的socket  设置选项 绑定 监听
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('', 8999))  # 这里绑定的是服务器的固定端口,目的是让客户端能连接到了我的机器上面之后,可以找到我的这个程序
	server_socket.listen(128)

	while True:
		# 2.接受用户连接
		client_socket, client_addr = server_socket.accept()
		print('接受到%s的连接请求' % str(client_addr))

		# 3.接收用户请求报文
		request_data = client_socket.recv(4096)
		# 解码 bytes  --> str
		request_data_str = request_data.decode()
		print(request_data)
		# ps:当用户的请求路径为/时候,表示其请求的是首页homepage
		# 解析用户请求 获取到用户的资源请求路径
		# 正则匹配 只要是有/ 提取请求路径
		# GET /index.html
		result = re.search(r'^\w+ (/\S*)', request_data_str)
		# 判断是否提取成功  成功就取出这个值,不成功结束程序
		if not result:  # 路径为空
			print('请求报文格式错误')
			client_socket.close()
			continue  # 跳过一次循环,继续执行if判断
		# 尽量扁平结构 不要使用else缩进去,那样的是嵌套结构,小技巧
		# 获取请求路径  资源路径<static> + /index.html
		# 如果执行到这里,一定是匹配成功了,因为失败的已经跳过了
		path_info = result.group(1)
		# 4.返回用户指定的文件数据作为响应体   打包到响应报文中  static + /index.html
		# static 是文件夹,open打不开 潜规则 :所有的web服务器 不写路径默认是主页

		# 如果path_info 是/ ,返回 index首页
		if path_info == '/':
			path_info = '/index.html'

		with open('static' + path_info, 'rb') as file:
			html_data = file.read()  # html_data 是二进制bytes字节类型的数据

		# .encode()先把前面的str类型转成bytes字节类型,然后拼接
		response_data = ('HTTP/1.1 200 OK\r\nServer: PWS3.0\r\n\r\n').encode() + html_data
		client_socket.send(response_data)

		# 5.一次请求/响应 就关闭连接  --> 短连接
		client_socket.close()


if __name__ == '__main__':
	main()
