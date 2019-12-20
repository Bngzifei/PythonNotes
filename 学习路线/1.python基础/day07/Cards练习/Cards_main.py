# 主函数main 用来实现整体功能,具体的每个功能的细节不写
import Cards练习.Cards_tools  # 导入工具模块


def main():
	# while True 循环 if 判断输入的指令
	while True:
		Cards练习.Cards_tools.show_menu()  # 显示主菜单
		cmd_str = int(input('输入你需要执行的指令(输入1/2/3/4):'))
		if cmd_str == 1:  # 新建名片
			Cards练习.Cards_tools.create_card()
		elif cmd_str == 2:  # 显示全部
			Cards练习.Cards_tools.show_all()

		elif cmd_str == 3:  # 查询名片
			Cards练习.Cards_tools.seek_card()

		elif cmd_str == 4:  # 退出系统
			print('欢迎再次使用[名片管理系统]')
			break
		else:
			print('输入错误,请重新输入')


main()
