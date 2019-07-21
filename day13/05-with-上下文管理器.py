"""
不用管是不是close()文件了
文件太大,比如FAT323格式,最大4G,如果超过了,就写不进去,这样会在close()前面会
抛出异常,这样文件就一直没有关闭,会导致文件资源会一直被占用,造成资源泄露,这样就会出现
一直打开文件的现象
资源泄露:
解决方法:
try:
	pass
except:
	错误
else:
	正确
finally:
	close()

打开文件/关闭文件 的中间把资源保存/标价起来了
这样就称之为上下文

格式:
打开
资源保存/标记
关闭

"""
"""
自己写一个类,完成with的操作

只要一个类实现上下文管理器,with才能支持

"""


class myFile:
	"""文件类,取代open类,和open类相似"""
	def __init__(self, name, mode):
		self.name = name
		self.mode = mode

	def __enter__(self):
		"""这是提供资源的上文环境,提供资源 给as后面的变量"""
		print('正在进入上文获取资源')
		self.file = open(self.name, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""提供下文,关闭资源"""
		print('正在进入下文,关闭资源')
		self.file.close()


if __name__ == '__main__':
	"""
	1.>obj = myFile('app.txt','rb') 执行,调用类初始化完成一个对象obj
	2.>通过调用对象obj的__enter__方法获取资源<上文>  --->给 as 后面的file
	3.>with正常代码中可以正常使用获取到的资源
	4.>在退出with语句块的时候,关闭资源的时候调用obj的__exit__方法,进入下文,释放资源
	
	"""

	with myFile('app.txt', 'rb') as file:
		print(file.read(8))

"""
总结:
实现支持with操作的类--->叫上下文管理器  同理 __iter__/__next__的叫 迭代器类
实现__enter__方法  上文  提供资源
实现__exit__方法   下文  关闭资源

"""
