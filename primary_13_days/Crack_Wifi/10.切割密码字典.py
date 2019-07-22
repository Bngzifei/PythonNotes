with open(r'F:\黑马Python21期基础班\Crack_Wifi\密码字典.txt', 'r') as file:
	while True:
		res = file.readline().strip()
		print(res)
		if res == '852963':
			break
		with open(r'F:\黑马Python21期基础班\Crack_Wifi\8位以上密码字典.txt', 'a') as f1:
			if len(res) < 8:
				continue
			f1.write(res + '\n')


# try:
# 	pass
# except Exception as e:
# 	pass
# else:
# 	pass
# finally:
# 	pass
