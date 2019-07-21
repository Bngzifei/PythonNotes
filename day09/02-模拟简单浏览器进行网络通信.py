# 0.创建socket
# 1.输入网址 域名解析 获取服务器ip
# 2.和服务器建立连接
# 3.发送 请求报文
# 4.接收 响应报文

# \r\n记得一定要带,否则会出错
import socket
# 创建socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
tcp_socket.connect(('www.jd.com', 80))
# 请求行
request_line = 'GET / HTTP/1.1\r\n'
# 请求头
request_header = 'User-Agent:%s\r\n' % (
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36')
# 拼接请求数据
request_data = request_line + request_header + '\r\n'
# 转成bytes字节类型进行发送
tcp_socket.send(request_data.encode())
# 返回服务器回送的数据
response_data = tcp_socket.recv(4096)
# 输出
print(response_data.decode())
