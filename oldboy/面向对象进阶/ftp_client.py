class Ftpclient:
	"""ftp客户端,但是还没有实现具体功能"""

	def __init__(self, addr):
		print('正在连接服务器%s' % addr)
		self.addr = addr
	# 过了一段时间后,put()方法实现了,alex使用者就可以调用 了
	def put(self):
		print('正在上传文件')
