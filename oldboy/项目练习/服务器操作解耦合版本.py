import os

"""
实现增.删.改.查.功能
height:权重
maxconn:最大连接数
"""
"""
# strip() 默认是去除输入字符串两边的回车,空格,如果想要去除指定的字符,在strip()里面传参数即可,例如:x.strip('*')就是把x两边的*号去除
"""


def file_handler(backend_data, res=None, type='fetch'):
	if type == 'fetch':
		with open('haproxy.conf', 'r') as read_f:
			tag = False  # 标识没找到这种情况
			ret = []
			# 遍历每一行数据,看是否能找到用户查询的那一条
			for read_line in read_f:
				if read_line.strip() == backend_data:
					tag = True  # 标识找到了
					continue  # 直接进行下一次操作
				if tag and read_line.startswith('backend'):
					break
				if tag:
					print('\033[1;45m%s\033[0m' % read_line, end='')
					ret.append(read_line)
		return ret
	elif type == 'change':
		with open('haproxy.conf', 'r') as read_f, open('haproxy.conf_new', 'w') as write_f:
			tag = False
			has_write = False
			for read_line in read_f:  # server
				if read_line.strip() == backend_data:
					tag = True
					continue
				if tag and read_line.startswith('backend'):
					tag = False
				if not tag:
					write_f.write(read_line)
				else:
					if not has_write:
						for record in res:
							write_f.write(record)
						has_write = True
		os.rename('haproxy.conf', 'haproxy.conf.bak')  # 源文件 进行备份 -->.bak 备份文件
		os.rename('haproxy.conf_new', 'haproxy.conf.')  # 新写入的文件再换成原来的文件名
		os.remove('haproxy.conf.bak')  # 删除旧文件


def fetch(data):
	"""查询"""

	backend_data = 'backend %s' % data  # 拼接成文本中需要的形式
	return file_handler(backend_data)


def add():
	"""增加"""
	pass


def change(data):
	"""修改"""

	backend = data[0]['backend']  # 文件中的一条记录   找 www.oldboy1.org
	backend_data = 'backend %s' % backend  # backend www.oldboy1.org

	#        server 2.2.2.5 2.2.2.5 weight 30 maxconn 4000
	old_server_record = '%sserver %s %s weight %s maxconn %s\n' % (' ' * 8, data[0]['record']['server'],
																   data[0]['record']['server'],
																   data[0]['record']['weight'],
																   data[0]['record']['maxconn'])

	new_server_record = '%sserver %s %s weight %s maxconn %s\n' % (' ' * 8, data[0]['record']['server'],
																   data[0]['record']['server'],
																   data[0]['record']['weight'],
																   data[0]['record']['maxconn'])

	print('用户需要修改的记录是:', old_server_record)
	res = fetch(backend)  # fetch(www.oldboy1.org)
	print('来自修改-->>', res)
	if not res or old_server_record not in res:
		return '你要修改的记录不存在'
	else:  # 存在的情况
		index = res.index(old_server_record)
		res[index] = new_server_record
		print('列表中的值已修改')

	res.insert(0, '%s\n' % backend_data)
	file_handler(backend_data, res=res, type='change')


def delete():
	"""删除"""
	pass


if __name__ == '__main__':
	msg = '''
	1:查询
	2:添加
	3:修改
	4:删除
	5:退出
	'''
	msg_dict = {
		'1': fetch,
		'2': add,
		'3': change,
		'4': delete,
	}

	while True:
		print(msg)
		choice = input('请输入选项:').strip()
		if not choice: continue
		if choice == '5': break

		data = input('输入要查询的数据:')

		if choice != '1':
			data = eval(data)  # 从字符串形式转为列表格式  <从字符串中提取原本的数据类型>

		res = msg_dict[choice](data)  # 实际上对应的就是fetch()函数了
		print('最终结果是-->:', res)
