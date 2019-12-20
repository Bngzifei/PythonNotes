import socketserver,os,json,configparser,hashlib,shutil
from conf import settings


STATUS_CODE = {
	250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
	251: "Invalid cmd ",
	252: "Invalid auth data",
	253: "Wrong username or password",
	254: "Passed authentication",
	255: "Filename doesn't provided",
	256: "File doesn't exist on server",
	257: "ready to send file",
	258: "md5 verification",

	800: "the file exist,but not enough ,is continue? ",
	801: "the file exist !",
	802: " ready to receive datas",

	900: "md5 valdate success"

}


class ServerHandler(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			# conn = self.request
			data = self.request.recv(1024).strip()
			data = json.loads(data.decode('utf-8'))

			'''
			{'action':'auth',
			'username':'yuan',
			'pwd':123}
			'''

			if data.get('action'):
				if hasattr(self, data.get('action')):
					func = getattr(self, data.get('action'))
					func(**data)  # 字典形式传进来
				else:
					print('invalid cmd')
			else:
				print('invalid cmd')

	def send_response(self, state_code):
		response = {'status_code': state_code}
		self.request.sendall(json.dumps(response).encode('utf-8'))

	def auth(self, **data):
		username = data['username']
		password = data['password']
		user = self.authenticate(username, password)

		if user:  # 如果有值,没有就是None,会去执行else
			self.send_response(254)
		else:
			self.send_response(253)

	def authenticate(self, user, pwd):
		cfg = configparser.ConfigParser()
		cfg.read(settings.ACCOUNT_PATH)

		if user in cfg.sections():
			if cfg[user]['Password'] == pwd:
				self.user = user
				self.mainPath = os.path.join(settings.BASE_DIR, 'home', self.user)
				print('passed authentication')
				return user
			# {1:'success',0:'fail'} 发送状态码,是最简单的

	def put(self, **data):
		print('data', data)
		file_name = data.get('file_name')
		file_size = data.get('file_size')
		target_path = data.get('target_path')

		abs_path = os.path.join(self.mainPath, target_path, file_name)

		# 1.文件有没有
		# 2.有
		# 3.完整不完整
		# ----------------------------------------------->
		has_received = 0
		if os.path.exists(abs_path):
			file_has_size = os.stat(abs_path).st_size
			if file_has_size < file_size:
				"""断点续传"""
				self.request.sendall('800'.encode('utf-8'))
				choice = self.request.recv(1024).decode('utf-8')

				if choice == 'Y':
					self.request.sendall(str(file_has_size).encode('utf-8'))
					has_received += file_has_size
					f = open(abs_path, 'ab')  # 追加内容
				else:
					f = open(abs_path,'wb')

			else:
				"""文件完整存在"""
				self.request.sendall('801'.encode('utf-8'))

				return  # 结束了

		else:
			self.request.sendall('802'.encode('utf-8'))
			f = open(abs_path, 'wb')

		while has_received < file_size:  # 没收完
			try:
				data = self.request.recv(1024)
			except Exception as e:
				break
			f.write(data)
			has_received += len(data)

		f.close()

	def ls(self,**data):

		file_list = os.listdir(self.mainPath)

		file_str = '\n'.join(file_list)
		if not len(file_list): # 如果为空
			file_str = '<empty dir>'
		self.request.sendall(file_str.encode('utf-8'))

	def cd(self,**data):

		dir_name = data.get('dir_name')

		if dir_name == '..':
			self.mainPath = os.path.dirname(self.mainPath)
		else:
			self.mainPath = os.path.join(self.mainPath,dir_name)

		self.request.sendall(self.mainPath.encode('utf-8'))

	def mkdir(self, **data):
		dir_name = data.get('dir_name')

		path = os.path.join(self.mainPath,dir_name)

		if not os.path.exists(path):  # 如果不在的时候创建
			if '/' in dir_name:  # 说明是多级目录
				os.makedirs(path)  # 创建多个文件夹
			else:
				os.mkdir(path)  # 创建单个目录
			self.request.sendall('create dir sucessed'.encode('utf-8'))
		else:
			self.request.sendall('dirname exist'.encode('utf-8'))


	def rmdir(self,**data):
		dir_name = data.get('dir_name')

		path = os.path.join(self.mainPath, dir_name)

		if os.path.exists(path):  # 如果存在<文件或者是文件夹>
			if os.path.isfile(path):  # 如果是文件
				os.remove(path)  # 是文件就删除
			else:
				shutil.rmtree(path)
			self.request.sendall('removed successed!'.encode('utf-8'))
		else:  # 不存在
			self.request.sendall('the file or dir does not exist!'.encode('utf-8'))

	def pwd(self,**data):
		self.request.sendall(self.mainPath.encode('utf-8'))

	def put_md5(self,**data):
		file_name = data.get('file_name')
		file_size = data.get('file_size')
		target_path = data.get('target_path')
		print(file_name,file_size,target_path)
		abs_path = os.path.join(self.mainPath,target_path,file_name)
		print('abs_path',abs_path)

		has_received = 0

		if os.path.exists(abs_path):
			has_file_size = os.stat(abs_path).st_size
			if has_file_size < file_size:
				self.request.sendall(b'800')

				is_continue = str(self.request.recv(1024)).encode('utf-8')

				if is_continue == 'Y':
					self.request.sendall(str(has_file_size).encode('utf-8'))
					has_received+=has_file_size
					f = open(abs_path,'ab')
				else:
					f = open(abs_path, 'wb')
			else:
				self.request.sendall(b'801')
				return
		else:
			self.request.sendall(b'802')
			f = open(abs_path,'wb')

		if data.get('md5'):
			print('hhhhh')
			md5_obj = hashlib.md5()

			while has_received<file_size:
				try:
					data = self.request.recv(1024)
					if not data:
						raise Exception
				except Exception:
					break

				f.write(data)
				has_received+=len(data)
				recv_file_md5 = md5_obj.update(data)
				print('bbbbbbbbbbbbbb')
			else:
				self.request.sendall(b'ok')  # 解决粘包
				send_file_md5 = self.request.recv(1024).decode('utf-8')
				print('send_file_md5',send_file_md5)
				self.request.sendall('900'.encode('utf-8'))
		else:
			while has_received<file_size:
				try:
					data = self.request.recv(1024)
					if not data:
						raise Exception
				except Exception:
					break

			f.write(data)
			has_received+=len(data)

		f.close()













