# 具体实现每个功能模块
card_list = []  # 空列表,用来添加后面的名片字典


# 1.显示主界面 show_menu()
def show_menu():
	"""主菜单栏"""
	print('*' * 30)
	print()
	print('欢迎使用[名片管理系统]')
	print('1.新建名片')
	print('2.显示全部')
	print('3.查询名片')
	print('4.退出系统')
	print()
	print('*' * 30)


# 2.创建新名片 create_card()
def create_card():
	"""创建新名片"""
	print('当前的操作是:创建名片')
	# 输入名片信息
	str_name = input('请输入姓名:')
	str_phone = input('请输入电话:')
	str_qq = input('请输入qq:')
	str_mail = input('请输入邮箱:')
	#  用字典来保存这些信息
	card_dict = {
		'name': str_name,
		'phone': str_phone,
		'qq': str_qq,
		'mail': str_mail
	}
	# 多个人的信息字典类型,使用一个list来添加保存
	card_list.append(card_dict)

	print('新建的名片信息成功!')


# print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
# print(str_name, str_phone, str_qq, str_mail, sep='\t\t')


# 3.显示全部名片 show_all()
def show_all():
	"""显示全部"""
	print('当前的操作是:显示全部')
	# 2.判断是否有列表中是否有名片信息
	if len(card_list) == 0:
		print('提示:没有任何名片记录')
		return  # 如果没有结束掉这个函数
	print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
	print('-' * 30)
	for card_dict in card_list:  # 逐一取出card_list中的每个字典元素key对应的value
		print(card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['mail'], sep='\t\t')
	print('-' * 30)


# 4.查询名片信息 seek_card()
def seek_card():
	"""查询名片"""
	print('当前的操作是:查找名片')
	# 输入用户需要查询的姓名
	target_name = input('输入您要查找的姓名:')

	for card_dict in card_list:
		if card_dict['name'] == target_name:
			print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
			print('-' * 30)
			print(card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['mail'], sep='\t\t')
			print('-' * 30)
			handle_card(card_dict)
			break
	else:
		print('没有找到%s' % target_name)


def handle_card(card_dict):
	while True:
		deal_str = int(input('请输入对该名片的操作:1.修改/2.删除/3.返回上一级'))
		if deal_str == 1:  # 修改
			card_dict['name'] = input('请输入姓名:')
			card_dict['phone'] = input('请输入电话:')
			card_dict['qq'] = input('请输入qq:')
			card_dict['mail'] = input('请输入邮箱:')
			print('%s的名片信息修改成功' % card_dict['name'])
			break
		elif deal_str == 2:  # 删除
			card_list.remove(card_dict)
			print('删除%s名片成功...' % card_dict['name'])
			break
		elif deal_str == 3:  # 返回上一级
			break
		else:
			print('输入有误,请重新输入')
