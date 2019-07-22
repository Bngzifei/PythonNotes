# 设置tag,对tag进行状态标识判断,可以实现每一层逐级跳出循环,还可以实现一次就跳出多层循环
tag = True
while tag:
	print('level1')
	choice = input('level1>:').strip()
	if choice == 'quit': break
	if choice == 'quit_all': tag = False
	while tag:
		print('level2')
		choice = input('level2>>:').strip()
		if choice == 'quit': break
		if choice == 'quit_all': tag = False
		while tag:
			print('level3')
			choice = input('level3>>>:').strip()
			if choice == 'quit': break
			if choice == 'quit_all': tag = False
