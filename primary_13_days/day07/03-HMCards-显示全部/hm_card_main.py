import hm_card_tool

# 加前缀是为了降低文件出现同名的情况
"""写主逻辑,不写实现的细节"""

# 以后会给效果图,然后参照着写


"""
1.显示主菜单
2.接收用户的输入
3.根据用户输入做相应操作
4.重复1-3的步骤

先易后难的书写步骤
"""

while True:
	# 1.显示主菜单

	hm_card_tool.show_menu()

	# 2.接收用户输入
	cmd_num = input('请选择执行的操作:')

	# 2.1 提示用户选择的指令
	print('您选择的功能是:%s' % cmd_num)

	# 3.进行判断
	if cmd_num == '1':  # 新建名片
		hm_card_tool.new_card()
	elif cmd_num == '2':  # 显示全部
		hm_card_tool.show_all()
	elif cmd_num == '3':  # 查询名片
		pass
	elif cmd_num == '0':  # 退出系统
		print('欢迎再次使用[名片管理系统]')
		break
	else:
		print('输入错误,请重新输入')
