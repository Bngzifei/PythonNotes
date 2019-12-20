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

	show_table_head()

	# 4.变量名片列表,取出每个字典,按格式输出
	for card_dict in card_list:
		print(card_dict['name'],
			  card_dict['phone'],
			  card_dict['qq'],
			  card_dict['email'],
			  sep='\t\t')
	print('-' * 30)


def search_card():
	"""查询名片"""
	# 1. 提示用户当前选择的功能
	print('功能:查询名片')
	# 2.让用户输入要查询的姓名
	target_name = input('输入要查询的姓名:')
	# 3.遍历列表,取出每一个字典,拿字典的name和要查询的姓名作比较
	for card_dict in card_list:
		if card_dict['name'] == target_name:
			# 3.如果查询到之后 输出表头及查询到的名片字典
			show_table_head()
			print(card_dict['name'],
				  card_dict['phone'],
				  card_dict['qq'],
				  card_dict['email'],
				  sep='\t\t')
			print('-' * 30)

			# TODO 对查询到名片进行高级处理 修改 删除

			del_card(card_dict)

			# while True:
			# 	# 1.让用户输入对名片的操作
			# 	cmd_num = int(input('对名片的操作:1.修改/ 2.删除/ 0.返回上一级:'))
			# 	if cmd_num == 1:  # 修改
			# 		card_dict['name'] = input('输入姓名:')
			# 		card_dict['phone'] = input('输入电话:')
			# 		card_dict['qq'] = input('输入qq:')
			# 		card_dict['email'] = input('输入邮箱:')
			# 		print('%s的名片修改成功' % card_dict['name'])  # 这么做,列表中的dict也会变化(存的都是地址) 不要去删除了之后再添加新的dict进来(引用列表.字典中一个元素都是引用一个元素对应的内存地址)
			# 		break  # 每个执行了都停掉循环
			# 	elif cmd_num == 2:  # 删除
			# 		card_list.remove(card_dict)  # 删除也是删除了list列表对dict的引用,如果不引用了也就自动删除了
			# 		print('删除名片成功')
			# 		break   # 每个执行了都停掉循环
			# 	elif cmd_num == 0:  # 返回上一级
			# 		break
			# 	else:
			# 		print('输入错误,请重新输入')




			break  # 当查询到名片后结束for 循环并且让else后面的内容不再执行
		# else:  # 如果在这里,因为是在for循环的里面了,所以提示会出现多次
	else:  # 如果在这里只会提示一次
		# 如果没有查询到,返回提示信息
		print('没有找到%s' % target_name)


def show_table_head():
	"""显示表头"""
	print('姓名', '电话', 'qq', '邮箱', sep='\t\t')
	print('-' * 30)


# 把一个真实数据赋值给形参时候,是内存地址的传递(引用的传递)
def del_card(card_dict):
	"""处理名片"""
	while True:
		# 1.让用户输入对名片的操作
		cmd_num = int(input('对名片的操作:1.修改/ 2.删除/ 0.返回上一级:'))
		if cmd_num == 1:  # 修改
			card_dict['name'] = input('输入姓名:')
			card_dict['phone'] = input('输入电话:')
			card_dict['qq'] = input('输入qq:')
			card_dict['email'] = input('输入邮箱:')
			print('%s的名片修改成功' % card_dict[
				'name'])  # 这么做,列表中的dict也会变化(存的都是地址) 不要去删除了之后再添加新的dict进来(引用列表.字典中一个元素都是引用一个元素对应的内存地址)
			break  # 每个执行了都停掉循环
		elif cmd_num == 2:  # 删除
			card_list.remove(card_dict)  # 删除也是删除了list列表对dict的引用,如果不引用了也就自动删除了
			print('删除名片成功')
			break  # 每个执行了都停掉循环
		elif cmd_num == 0:  # 返回上一级
			break
		else:
			print('输入错误,请重新输入')

# 全局变量也可以传值,参数传递.尽量使用参数传递.降低内存占用

# 全局变量的写起来简单.方便.1.多个地方(函数)使用2.列表数据不能释放(局部变量函数执行结束就释放了)我们的程序需要一直使用card_list,所以选择card_list列表.优先使用参数传递(1.降低耦合度 2.用完了就释放)  主要是为了以后的习惯问题(考虑内存占用的问题,这样就会以后轻松了)
