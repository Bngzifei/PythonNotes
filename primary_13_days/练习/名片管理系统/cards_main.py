# 程序的主函数 不写每个功能的具体细节
import card_tools

card_tools.load_data()

while True:
	card_tools.show_menu()
	cmd_str = int(input('输入操作:'))
	if cmd_str == 1:
		card_tools.add_card()
	elif cmd_str == 2:
		card_tools.show_all()
	elif cmd_str == 3:
		card_tools.seek_card()
	elif cmd_str == 4:
		card_tools.exit()  # 只有这里有break,用来实现退出系统,其他地方没有
		break
	else:
		print('输入的操作指令错误,请重新输入')
