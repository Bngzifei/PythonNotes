has_ticket = True  # 有票
knife_length = 15  # 刀长度

if has_ticket:
	print('准备安检')
	if knife_length >= 20:  # 判断刀长度
		print('走一趟,小黑屋聊一聊')
	else:
		print('上车走了')
else:  # else后面也可以加if的缩进块
	print('去买票')

	if knife_length == 20:
		print('stuff')

