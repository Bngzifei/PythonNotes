import optparse  # 解析命令行的命令
import socketserver
from conf import settings

# import server  # 1.main不是启动文件,所以这样不行.两条路径都找不到server文件
from core import server  # 2. 必须是这样


class ArgvHandler():
	"""处理参数"""
	def __init__(self):
		self.op = optparse.OptionParser()
		# -s:代表server
		# self.op.add_option('-s','--s',dst='server')
		# self.op.add_option('-P','--port',dst='port')

		options, args = self.op.parse_args()

		self.verify_args(options, args)  # 校验参数

	def verify_args(self, options, args):
		"""校验参数"""
		cmd = args[0]

		# 使用反射进行一一对应的关系判断 :  if / 使用字典对应 / 反射 <最好使用>易扩展
		# 目的:根据用户输入的命令,找到对应的函数去处理

		if hasattr(self, cmd):  # 判断self实例对象是否有cmd start 这个方法
			func = getattr(self, cmd)
			func()

	def start(self):
		"""启动方法"""
		print(' the server is working...')
		s = socketserver.ThreadingTCPServer((settings.IP,settings.PORT), server.ServerHandler)
		s.serve_forever()

	def help(self):
		pass

	# print(options)
	# print(type(options))
	# print(options.server)
	# print(options.port)
	# print(args)
