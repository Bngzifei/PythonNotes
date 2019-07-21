"""
开始一个项目,首先是要创建规范的目录

接着开始写大体思路



bin:启动文件,就是可执行文件的地方,bin表示二进制的意思


"""
import optparse, socket,json, os, sys, hashlib,time

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
	801: "the file is already verify_md5 !",
	802: " ready to receive datas",

	900: "md5 valdate success"

}


class ClientHandler:
	"""客户端"""

	def __init__(self):
		self.op = optparse.OptionParser()
		self.op.add_option('-s', '--server', dest='server')
		self.op.add_option('-P', '--port', dest='port')
		self.op.add_option('-u', '--username', dest='username')
		self.op.add_option('-p', '--password', dest='password')

		self.options, self.args = self.op.parse_args()

		self.verify_args(self.options, self.args)
		self.make_connection()
		self.mainPath = os.path.dirname(os.path.abspath(__file__))
		self.last = 0
		self.sock = socket.socket()

	def verify_args(self, options, args):
		"""校验参数"""
		server = options.server
		port = options.port

		if 0 < int(port) < 65535:
			return True
		else:
			exit('the port is in 0-65535')

	def make_connection(self):
		"""连接"""
		self.sock.connect((self.options.server, int(self.options.port)))

	def interactive(self):
		"""交互"""
		print('begin to interactive......')

		if self.authenticate():  # 验证通过
			while True:
				cmd_info = input('[%s]' % self.current_dir).strip()  # put 12.png images
				cmd_list = cmd_info.split()

				if hasattr(self, cmd_list[0]):
					func = getattr(self, cmd_list[0])
					func(*cmd_list)

	def put(self, *cmd_list):
		"""上传"""
		# put 12.png images
		action, local_path, target_path, md5_required = cmd_list
		local_path = os.path.join(self.mainPath, local_path)

		file_name = os.path.basename(local_path)
		file_size = os.stat(local_path).st_size

		data = {'action': 'put', 'file_name': file_name, 'file_size': file_size, 'target_path': target_path}

		self.sock.send(json.dumps(data).encode('utf-8'))

		is_exist = self.sock.recv(1024).decode('utf-8')
		# ---------------------------------------------------------------------->
		has_sent = 0
		if is_exist == '800':
			# 文件不完整
			choice = input('the file exist,but not enough,is continue?[Y/N]').strip()
			if choice.upper() == 'Y':
				self.sock.sendall('Y'.encode('utf-8'))
				continue_position = self.sock.recv(1024).decode('utf-8')
				has_sent += int(continue_position)

			else:
				self.sock.sendall('N'.encode('utf-8'))

		elif is_exist == '801':
			# 文件完全存在
			print('the file exist')
			return
		else:
			pass

		f = open(local_path, 'rb')

		f.seek(has_sent)  # 定位光标位置

		while has_sent < file_size:
			data = f.read(1024)
			self.sock.sendall(data)
			has_sent += len(data)
			self.show_process(has_sent, file_size)

		f.close()
		print('put success')

	def show_process(self, has, total):
		"""进度条"""
		rate = float(has) / float(total)
		rate_num = int(rate * 100)

		if self.last != rate_num:  # \r 行首显示
			sys.stdout.write('%s%% %s\r' % (rate_num, '>' * rate_num))
		self.last = rate_num

	def ls(self, *cmd_list):
		"""查看"""
		data = {
			'action': 'ls',
		}
		self.sock.sendall(json.dumps(data).encode('utf-8'))  # 查看文件
		data = self.sock.recv(1024).decode('utf-8')
		print(data)

	def cd(self, *cmd_list):
		# cd images
		data = {
			'action': 'cd',
			'dir_name': cmd_list[1]
		}
		self.sock.sendall(json.dumps(data).encode('utf-8'))  # 查看文件
		data = self.sock.recv(1024).decode('utf-8')
		# print(os.path.basename(data))
		self.current_dir = os.path.basename(data)

	def mkdir(self, *cmd_list):
		data = {
			'action': 'mkdir',
			'dir_name': cmd_list[1]
		}
		self.sock.sendall(json.dumps(data).encode('utf-8'))
		data = self.sock.recv(1024).decode('utf-8')
		print(data)

	def rmdir(self, *cmd_list):
		data = {
			'action': 'rmdir',
			'dir_name': cmd_list[1]
		}
		self.sock.sendall(json.dumps(data).encode('utf-8'))
		data = self.sock.recv(1024).decode('utf-8')
		print(data)

	def pwd(self, *cmd_list):
		data = {
			'action': 'pwd',
		}
		self.sock.sendall(json.dumps(data).encode('utf-8'))
		data = self.sock.recv(1024).decode('utf-8')
		print(data)

	def authenticate(self):
		"""认证"""
		if self.options.username is None or self.options.password is None:
			username = input('username:')
			password = input('password:')
			return self.get_auth_result(username, password)

		return self.get_auth_result(self.options.username, self.options.password)

	def response(self):
		"""响应"""
		data = self.sock.recv(1024).decode('utf-8')
		data = json.loads(data)

		return data

	def get_auth_result(self, user, pwd):
		"""认证结果"""

		data = {
			'action': 'auth',
			'username': user,
			'password': pwd,
		}

		self.sock.send(json.dumps(data).encode('utf-8'))
		response = self.response()
		print('response:', response['status_code'])

		if response['status_code'] == 254:
			self.user = user  # 一定记得
			self.current_dir = user
			print(STATUS_CODE[254])
			return True
		else:
			print(STATUS_CODE[response['status_code']])

	def put_md5(self, *cmd_list):
		"""文件校验"""
		if len(cmd_list) == 3:
			action, local_path, target_path = cmd_list
		else:
			action, local_path, target_path, is_md5 = cmd_list
		if '/' in local_path:
			local_path = os.path.join(self.mainPath, local_path.split('/'))
		local_path = os.path.join(self.mainPath, local_path)

		file_name = os.path.basename(local_path)
		file_size = os.stat(local_path).st_size

		data = {
			'action': 'put_md5',
			'file_name': file_name,
			'file_size': file_size,
			'target_path': target_path
		}

		if self.md5_required(*cmd_list):
			data['md5'] = True
		self.sock.sendall(json.dumps(data).encode('utf-8'))
		is_exist = self.sock.recv(1024).decode('utf-8')
		has_sent = 0

		if is_exist == '800':
			choice = input('the file exist,is continue?[Y/N]').strip()
			if choice.upper() == 'Y':
				self.sock.sendall('Y'.encode('utf-8'))
				continue_position = self.sock.recv(1024).decode('utf-8')
				has_sent = int(continue_position)

			else:
				self.sock.sendall('N'.encode('utf-8'))

		elif is_exist == '801':

			print(STATUS_CODE[801])
			return

		file_obj = open(local_path,'rb')
		file_obj.seek(has_sent)
		start = time.time()

		if self.md5_required(*cmd_list):
			md5_obj = hashlib.md5()

			while has_sent<file_size:
				data = file_obj.read(1024)
				self.sock.sendall(data)
				has_sent += len(data)
				md5_obj.update(data)
				self.show_process(has_sent,file_size)
			else:
				print('put sucessed!')
				md5_val = md5_obj.hexdigest()
				self.sock.recv(1024)
				self.sock.sendall(md5_val.encode('utf-8'))
				response = self.sock.recv(1024).decode('utf-8')
				print('response',response)
				if response == '900':
					print(STATUS_CODE[900])
		else:
			while has_sent<file_size:
				data = file_obj.read(1024)
				self.sock.sendall(data)
				has_sent += len(data)
				self.show_process(has_sent,file_size)
			else:
				file_obj.close()
				end = time.time()
				print('\ncost %s s' % (end - start))
				print('put successed !')

	def md5_required(self, *cmd_list):
		"""检查命令是否需要进行md5校验"""
		if '--md5' in cmd_list:
			return True


ch = ClientHandler()  # ch是一个实例对象

ch.interactive()
