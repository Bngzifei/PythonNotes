"""tcp粘包:  面试一般不会问
为了解决tcp数据发送过程中多个数据一次被对方接收到而取法区分开.简称数据粘包
struct(结构体)模块pack和unpack方法进行打包和拆包

# 把数据长度打包成四个字节,发送给对方
tcp_socket.send(strunct.pack('i',len(data))

tcp_socket.send(data)

data_len = struct.unpack('i',client_socket.recv(4))[0]
data = client_socket.recv(data_len)
"""
"""
try:
	可能出错的代码
except Exception as e:
	#出错
	pass
else:
	#不出错
	pass
finally:
	# 不管有没有错,都可以执行这里的代码
	pass

with 可以在文件出现异常的情况下自动关闭文件,防止文件资源泄露.

"""

