"""
提供了  创建资源/销毁资源  就是上下文管理器

"""

# class myFile:
# 	"""文件类,取代open类,和open类相似"""
#
# 	def __init__(self, name, mode):
# 		self.name = name
# 		self.mode = mode
#
# 	def __enter__(self):  # 获取资源
# 		"""这是提供资源的上文环境,提供资源 给as后面的变量"""
# 		print('正在进入上文获取资源')
# 		self.file = open(self.name, self.mode)
# 		return self.file
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):  # 关闭资源
# 		"""提供下文,关闭资源
# 		exc_type:类型
# 		exc_val:类型值
# 		exc_tb:跟踪返回值
# 		 """
# 		print('正在进入下文,关闭资源')
# 		# print(exc_type)  # <class 'io.UnsupportedOperation'>
# 		# print(exc_val)  # read
# 		# print(exc_tb)  # <traceback object at 0x0000024BC9F1F748>
# 		self.file.close()
#
#
# if __name__ == '__main__':
# 	with myFile('app.txt', 'wb') as file:  # 就是把上下文资源管理起来
# 		print(file.read(8))
# -----------------------第二种  @contextmanager-------------------------------->

# 迭代器 生成器 装饰器 上下文管理器

from contextlib import contextmanager  # 导入上下文管理器


@contextmanager
def myopen(name, mode):
	"""生成器函数 + 装饰器 = 上下文管理器:进入上文,获取资源"""
	print('正在进入上文获取资源')
	file = open(name, mode)
	yield file  # 暂停在这里,不能使用return,这样会直接把资源全部关闭

	# 进入下文 关闭资源
	print('正在进入下文关闭资源')
	file.close()


if __name__ == '__main__':
	with myopen('app.txt', 'rb') as file:
		print(file.read(8))
