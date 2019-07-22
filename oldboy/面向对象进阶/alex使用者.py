from ftp_client import Ftpclient  # 记得先要去导模块

f1 = Ftpclient('192.1.1.1')
# 上传,但是不能调用
# f1.put()

if hasattr(f1,'put'):
	func_get = getattr(f1,'put')
	func_get()  # 调用put()方法
else:
	print('其他的逻辑')