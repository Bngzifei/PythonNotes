# 具体实现的功能

# 1.显示主界面
# 2.新建名片
# 3.全部显示
# 4.查询名片(输入名字后查询)
# 		4.1修改
# 		4.2删除
# 		4.3返回至主界面
# 5.退出系统
import os

card_list = []


def show_menu():
	"""主界面"""
	print('*' * 30)
	print('欢迎使用[名片管理系统 V1.0]!')
	print('1-->新建名片,2-->显示全部,3-->查询名片,4-->退出系统')
	print('*' * 30)


def add_card():
	"""新建名片"""
	str_name = input('姓名:')
	str_qq = input('QQ:')
	str_phone = input('电话:')
	str_mail = input('邮箱:')

	# 使用字典类型保存
	card_dict = {
		'name': str_name,
		'qq': str_qq,
		'phone': str_phone,
		'mail': str_mail
	}

	# 将每个字典类型数据保存到list列表中
	card_list.append(card_dict)
	save_data()
	print('%s的信息保存成功!' % str_name)


def show_all():
	"""显示全部"""
	# 对list表进行判断,是否有数据
	if len(card_list) == 0:
		print('表中无数据,请重新输入')
	else:
		biaotou()
		for card_info in card_list:
			print(card_info['name'], card_info['qq'], card_info['phone'], card_info['mail'], sep='\t\t')


def seek_card():
	"""查找名片"""
	# TODO 加一个判断,直接给用户提示是否是空表,避免用户无效操作
	# 接收用户输入的姓名:
	cmd_name = input('输入需要查询的姓名:')
	# 循环遍历card_list表,看是否有
	for card in card_list:  # 如果不使用for...else...语句,则外部使用布尔变量,for内部记录变化,初始值设为False,如果找到了,设为True.然后在for外部使用if 判断是否需要输出提示信息.
		# if 判断是否有
		if cmd_name == card['name']:
			print('%s的信息是:' % cmd_name)
			biaotou()
			print(card['name'], card['qq'], card['phone'], card['mail'], sep='\t\t')
			# 找到了之后进行修改操作
			deal_card(card)  # TODO 找到之后进行的操作
			break  # 找到了就结束这个for循环
		# else:
		# 	pass
	else:  # for 的else只在循环结束之后提示一次,如果else是if的,则每次没找到都会输出找不到的提示信息
		print('%s的信息不存在' % cmd_name)


def exit():
	"""退出系统"""
	print('欢迎下次使用[名片管理系统]!')


def biaotou():
	print('姓名', 'QQ', '电话', '邮箱', sep='\t\t')
	print('-' * 30)


def deal_card(card_dict):
	while True:
		cmd_str = int(input('输入您需要的操作:1.修改 / 2.删除 / 3.返回主界面'))
		# if 判断
		if cmd_str == 1:
			reprocess(card_dict)  # TODO 对四种信息分别处理
		# str_name = input('姓名:')
		# str_qq = input('QQ:')
		# str_phone = input('电话:')
		# str_mail = input('邮箱:')
		#
		# # 将原来字典的key对应的value分别替换掉
		# card_dict['name'] = str_name
		# card_dict['qq'] = str_qq
		# card_dict['phone'] = str_phone
		# card_dict['mail'] = str_mail
		# print('%s的信息修改成功' % card_dict['name'])
		# break
		elif cmd_str == 2:
			card_list.remove(card_dict)  # 删除
			save_data()
			print('%s的信息删除成功' % card_dict['name'])
			break
		elif cmd_str == 3:  # break跳出这个循环,返回到主界面
			break
		else:
			print('输入的指令错误,请重新输入')  # 这个不加break就是为了让这个提示一直出现


def reprocess(card_dict):

	while True:
		cmd_str = int(input('输入您需要的操作:1.修改姓名 / 2.修改QQ / 3.修改电话 / 4.修改邮箱 / 5.返回上一级'))
		if cmd_str == 1:
			print('您当前的操作是修改姓名')
			str_name = input('请输入新的姓名:')
			card_dict['name'] = str_name
			save_data()
			print('姓名修改成功,新的姓名是%s' % card_dict['name'])
			break
		elif cmd_str == 2:
			print('您当前的操作是修改QQ')
			str_qq = input('请输入新的QQ:')
			card_dict['qq'] = str_qq
			save_data()
			print('QQ修改成功,新的QQ是%s' % card_dict['qq'])
			break
		elif cmd_str == 3:
			print('您当前的操作是修改电话')
			str_phone = input('请输入新的电话:')
			card_dict['phone'] = str_phone
			save_data()
			print('电话修改成功,新的电话是%s' % card_dict['phone'])
			break
		elif cmd_str == 4:
			print('您当前的操作是修改邮箱')
			str_mail = input('请输入新的邮箱:')
			card_dict['mail'] = str_mail
			save_data()
			print('邮箱修改成功,新的邮箱是%s' % card_dict['mail'])
			break
		elif cmd_str == 5:  # 返回上一级界面
			break
		else:
			print('输入的操作错误,请重新输入')  # 这个不加break就是为了让它循环输出提示用户


# eval:重新运算求出参数的内容,就是将字符串转回对应的原来的数据类型
def load_data():
	"""读取数据"""
	# if判断文件是否存在
	if os.path.exists('cards.txt'):
		# 打开文件
		f = open('cards.txt', 'rb')  # 二进制方式的才可以支持中文
		global card_list
		# 读取内容 列表/元组 格式的字符串 转回 列表/元组的类型,使用eval()
		card_list = eval(f.read().decode('utf-8'))  # 支持读取中文字符
		# 关闭文件
		f.close()


def save_data():
	"""保存数据"""
	print('功能:保存数据')
	# 打开文件
	f = open('cards.txt', 'wb')  # 二进制方式的才可以支持中文
	# 写入数据
	f.write(str(card_list).encode("utf-8"))  # 支持写入中文字符
	# 关闭文件
	f.close()
	print('保存数据成功!')
