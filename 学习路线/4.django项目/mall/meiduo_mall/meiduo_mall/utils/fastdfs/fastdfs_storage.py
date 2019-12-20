from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client


class FastDFSStorage(Storage):
	"""自定义django文件管理系统类"""

	def __init__(self,client_conf=None,base_url=None):  # 变成默认参数.
		"""初始化方法:官方要求这个必须可以不传参数.所以我们就得把形参换成默认参数.这样就可以不传参数了"""

		# 原始版
		# self.client_conf = client_conf  # 别人传了,就使用别人的,没有,就使用我这里默认的
		#
		# if self.client_conf == None:
		# 	self.client_conf = settings.FDFS_CLIENT_CONF

		# 升级版
		self.client_conf = client_conf or settings.FDFS_CLIENT_CONF
		self.base_url = base_url or settings.FDFS_BASE_URL

	def _open(self, name, mode='rb'):
		"""
		存储类,用于打开文件的,因为我们只做上传文件,所以此方法重写后什么也不做.官方要求写这个方法.
		:param name: 要打开的文件名
		:param mode: 文件读取模式
		:return:
		工作之后,尽量使用rb.r方式对换行符号等等处理会丢失数据
		"""
		pass

	def _save(self, name, content):
		"""
		让django把图片用FDFS进行图片的上传存储
		:param name: 要存储的文件名字
		:param content: 要存储的文件的对象.  在已经把文件变成一个对象了
		:return: file_id: 文件在fdfs唯⼀一标识（file_id）
		"""

		# 1.加载fdfs的客户端配置文件来创建一个fdfs客户端:对接django程序
		# client = Fdfs_client('meiduo_mall/utils/fastdfs/client.conf')
		# client = Fdfs_client(settings.FDFS_CLIENT_CONF)
		client = Fdfs_client(self.client_conf)

		# 下面这种上传方式需要知道当前要上传文件的绝对路径.此方式上传的图片在storage里面会有后缀
		# ret = client.upload_by_filename('/home/python/Desktop/pic.png')

		# 2.就是把文件数据当做一个对象来上传.因为file的方式是一个文件的本地路径上传,但是我们又不知道这个文件的在本地的具体路径.
		# 所以:
		# 使用buffer方式上传 文件对象.read(): 以二进制方式去读取
		# buffer:以文件对象来上传,数据流 .此方式上传的图片无后缀
		ret = client.upload_appender_by_buffer(content.read())

		# 3.取出当前图片上传后是否成功的状态
		status = ret.get('Status')
		# 判断文件上传是否成功
		if status != 'Upload successed.':
			raise Exception('Upload file failed!!')  # 文件上传失败

		# 如果可以执行到这里,说明文件上传成功
		file_id = ret.get('Remote file_id')  # 拿到file_id:其实就是文件存储路径
		return file_id

	def exists(self, name):
		"""
		判断要上传的文件在storage服务器中是否已经存在
		:param name: 要判断的文件名
		:return: True(文件已经存在,就不会再上传了)False(文件不存在,需要上传,然后马上调用save)
		"""
		return False

	def url(self, name):
		"""
		返回要下载的图片的绝对路径
		:param name: file_id 文件存储在storage中的路径(文件在storage中的相对路径)
		:return:返回文件的绝对路径  http://192.168.17.128:8888/group1/M00/00/00/wKgRgFv_U2aAQN55AADnHm9Se_c269.png
		"""
		# return 'http:/192.168.17.128:8888' + name
		# return settings.FDFS_BASE_URL + name
		# 优化版:
		return self.base_url + name








"""
>>> from fdfs_client.client import Fdfs_client
>>> client = Fdfs_client('meiduo_mall/utils/fastdfs/client.conf')
>>> ret = client.upload_by_filename('/home/python/Desktop/pic.png')

>>> ret
{'Uploaded size': '57.00KB',
'Remote file_id': 'group1/M00/00/00/wKgRgFv_U2aAQN55AADnHm9Se_c269.png',
'Storage IP': '192.168.17.128',
'Local file name': '/home/python/Desktop/pic.png',
'Group name': 'group1',
'Status': 'Upload successed.'}


当在模板文件中执行.url的时候,就会调用这里的url方法.

上传图片的工作不是我们做的.
"""



# ------------------------原来的:------------
# class FastDFSStorage(Storage):
#     """自定义Django文件存储系统"""
#
#     def __init__(self, client_conf=None, base_url=None):
#         self.client_conf = client_conf or settings.FDFS_CLIENT_CONF
#         self.base_url = base_url or settings.FDFS_BASE_URL
#
#     def _open(self, name, mode='rb'):
#         """打开文件时调用的,目前用不到,但是必须实现,所以pass"""
#         pass
#
#     def _save(self, name, content):
#         """
#         保存文件时调用的
#         :param name: 要保存的文件名字
#         :param content: 要保存的文件内容
#         :return: 文件在fdfs的唯一标识(fild_id)
#         """
#         client = Fdfs_client(self.client_conf)
#         ret = client.upload_by_buffer(content.read())
#         # 判断上传是否成功
#         if ret.get('Status') != 'Upload successed.':
#             raise Exception('fastfds upload failed')
#         # 返回结果
#         file_id = ret.get('Remote file_id')
#         return file_id
#
#     def exists(self, name):
#         """判断文件是否存在时调用的,返回False告诉Django每次都是新的文件"""
#         return False
#
#     def url(self, name):
#         """返回文件全路径"""
#         return self.base_url + name
