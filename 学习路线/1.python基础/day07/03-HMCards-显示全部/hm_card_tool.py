"""写每个功能的实现细节"""
# 定义一个全局列表变量,用来保存所有的名片字典
card_list = []


def show_menu():
	"""显示菜单"""
	print('*' * 30)
	print('欢迎使用[名片管理系统]')
	print()  # 空一行
	print('1.新建名片')
	print('2.显示全部')
	print('3.查询名片')
	print('4.退出系统')
	print()  # 空一行
	print('*' * 30)


def new_card():
	"""新建名片(保存数据)"""

	# 1.1提示用户当前的功能
	print('功能:新建名片')

	# 2.让用户输入名片信息(姓名.电话.qq.邮箱)
	name_str = input('请输入姓名:')
	phone_str = input('请输入电话:')
	qq_str = input('请输入qq:')
	email_str = input('请输入邮箱:')

	# 3.保存名片数据  (字典格式)
	card_dict = {'name': name_str,  # 记得这里的name_str是一个变量值(value),前面的name才是key,所以key需要自己给命名,见名知义即可
				 'phone': phone_str,
				 'qq': qq_str,
				 'email': email_str}

	# 3.1 把名片字典添加到列表中
	# 当用=号方式在函数内部给全局变量赋值时候,一定要提前global声明
	card_list.append(card_dict)  # 存的是内存地址(存了字典的内存地址),局部变量的字典销毁之后,列表的存的地址还在,里面的数据也还在()
	# 无变量引用了才会销毁

	# 4.提示用户名片添加成功
	print('添加%s的名片成功' % name_str)


def show_all():
	"""显示全部(取数据)"""
	# 1.提示用户当前选择的功能
	print('功能:显示全部')

	# 2.判断列表中是否有名片信息
	if len(card_list) == 0:
		print('提示:没有任何名片信息')
		# 法1:return结束函数
		return  # 提前让函数结束



	# 法2:缩进到else里面
	# else:
	# 	# 3.输出表头信息
	# 	# print('姓名\t\t电话\t\t姓名\t\t姓名\t\t')
	# 	print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
	# 	print('-' * 30)
	#
	# 	# 4.变量名片列表,取出每个字典,按格式输出
	# 	for card_dict in card_list:
	# 		print(card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email'], sep='\t\t')
	# 	print('-' * 30)
	# 3.输出表头信息
	# print('姓名\t\t电话\t\t姓名\t\t姓名\t\t')
	print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
	print('-' * 30)

	# 4.变量名片列表,取出每个字典,按格式输出
	for card_dict in card_list:
		print(card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email'], sep='\t\t')
	print('-' * 30)
