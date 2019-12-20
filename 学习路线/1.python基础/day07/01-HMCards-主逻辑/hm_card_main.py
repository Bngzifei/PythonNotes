import hm_card_tool
# 加前缀是为了降低文件出现同名的情况
"""写主逻辑,不写实现的细节"""

# 以后会给效果图,然后参照着写


"""
1.显示主菜单
2.接收用户的输入
3.根据用户输入做相应操作
4.重复1-3的步骤

"""


while True:
	# 1.显示主菜单

	hm_card_tool.show_menu()

	# 2.接收用户输入
	cmd_num = input('输入执行的操作:')

	# 3.进行判断
	if cmd_num == '1':  # 新建名片
		print('新建名片')
	elif cmd_num == '2':
		print('显示全部')
	elif cmd_num == '3':
		print('')
	elif cmd_num == '0':
		print('欢迎再次使用[]')
		break
	else:
		print('输入错误,请重新书写')
